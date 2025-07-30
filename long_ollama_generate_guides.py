# -*- coding: utf-8 -*-
"""
Lecture Processor (Phase 1) - Markdown Output Version
------------------------------------------------------
Author: [PRATIK SONTAKKE]
Date: [30-07-2025]

Description:
This script automates the creation of study guides from structured text files.
"""
import os
import re
import time
import argparse
import logging
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama import OllamaLLM

# Configure logging with timestamps
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def parse_lecture_file(filepath: str) -> dict:
    """Parses a lecture file with custom XML-like tags into a dictionary."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        return None
    tags = ["lecture-name", "transcript", "summary", "imp-concept", "notes"]
    parsed_data = {}
    for tag in tags:
        match = re.search(f'<{tag}>(.*?)</{tag}>', content, re.DOTALL)
        parsed_data[tag] = match.group(1).strip() if match else ""
    return parsed_data

def setup_vector_db(text_content: str, db_path: str):
    """Creates or loads a persistent Chroma vector store. Not used for generation in this script."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    if os.path.exists(db_path):
        logging.info(f"Verified existing database at: {db_path}")
    else:
        logging.info(f"Creating new database at: {db_path}")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
        docs = text_splitter.create_documents([text_content])
        Chroma.from_documents(
            documents=docs,
            embedding=embeddings,
            persist_directory=db_path
        )

def generate_study_guide_full_context(knowledge_packet: str) -> str:
    """
    Generates a study guide by sending the ENTIRE knowledge packet to the LLM.
    This bypasses the RAG retrieval step for maximum comprehensiveness.
    """

    template = """
    You are a world-class technical note-taker trained to convert full lectures into complete, structured notes
    that can replace watching the lecture entirely.

    🔒 STRICT INSTRUCTIONS:
    - Your ONLY source of truth is the lecture context provided below.
    - NEVER add anything from prior knowledge or outside experience.
    - Do NOT summarize. Instead, **reconstruct the lecture as complete notes** — detailed enough that a student reading it can learn everything without watching the video.

    🎯 GOAL:
    Generate highly structured and richly informative notes in Markdown format that:
    - Preserve the **full logical flow** and **depth** of the lecture.
    - Break down **every explanation**, **process**, **definition**, and **code snippet** clearly.
    - Use bullets, headings, code blocks, and examples as needed for clarity.
    - Cover **100% of the technical content** and subtle reasoning from the original lecture.

    🧠 Focus especially on:
    - Explanations, not just outcomes
    - Why things are done a certain way (reasoning)
    - Full technical clarity with no gaps

    🎨 Formatting Rules:
    - Use **Markdown headings** (`##`, `###`) to organize the lecture into logical sections and subtopics.
    - Use **bullet points** for lists, steps, or multiple ideas.
    - Use **code blocks** (` ``` `) with short explanations for commands/configs/code.
    - Use **bold** or *italics* to emphasize important terms.

    🧾 INPUT: Full Lecture Transcript
    -----------------------------
    {full_context}
    -----------------------------

    🧾 OUTPUT: Full Lecture Notes in Markdown
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    llm = OllamaLLM(model="llama3:latest", temperature=0.1)
    full_context_chain = prompt | llm | StrOutputParser()
    logging.info("Sending lecture content to LLM...")
    start_time = time.time()
    result = full_context_chain.invoke({"full_context": knowledge_packet})
    duration = time.time() - start_time
    logging.info(f"LLM response time: {duration:.2f} seconds")
    return result

def save_as_markdown(markdown_text: str, output_path: str):
    """Saves the generated markdown to file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_text)
        logging.info(f"Saved study guide to: {output_path}")
    except Exception as e:
        logging.error("Could not save markdown file.")
        logging.error(str(e))

def main(input_dir: str, output_dir: str, db_dir: str, _unused_packet_dir: str):
    """Main orchestration logic."""
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        logging.warning("GOOGLE_API_KEY not found. Embedding creation might fail.")

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(db_dir, exist_ok=True)

    try:
        lecture_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]
    except FileNotFoundError:
        logging.error(f"Input directory '{input_dir}' not found.")
        return

    logging.info(f"Found {len(lecture_files)} lecture(s) to process.")

    for filename in lecture_files:
        logging.info(f"Processing: {filename}")
        filepath = os.path.join(input_dir, filename)
        base_filename = os.path.splitext(filename)[0]

        parsed_data = parse_lecture_file(filepath)
        if not parsed_data or not parsed_data.get('transcript'):
            logging.warning(f"Skipping '{filename}' due to parsing errors or empty transcript.")
            continue

        knowledge_packet = (
            f"LECTURE TITLE: {parsed_data.get('lecture-name', 'N/A')}\n\n"
            f"TRANSCRIPT:\n{parsed_data['transcript']}\n\n"
            f"INSTRUCTOR NOTES:\n{parsed_data['notes']}\n\n"
            f"IMPORTANT CONCEPTS MENTIONED:\n{parsed_data['imp-concept']}"
        )

        lecture_db_path = os.path.join(db_dir, base_filename)
        setup_vector_db(knowledge_packet, lecture_db_path)

        generated_markdown = generate_study_guide_full_context(knowledge_packet)

        if generated_markdown and generated_markdown.strip():
            output_path = os.path.join(output_dir, f"{base_filename}_Study_Guide.md")
            save_as_markdown(generated_markdown, output_path)
        else:
            logging.error("LLM returned an empty response. Skipping file save.")

        logging.info("-" * 60)

    logging.info("All lectures processed successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A tool to generate comprehensive study guides from structured lecture text files.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-i", "--input_dir", default="lectures", help="Input directory")
    parser.add_argument("-o", "--output_dir", default="output_long_notes", help="Output directory for .md files")
    parser.add_argument("-d", "--db_dir", default="db", help="Directory for persistent vector databases")
    parser.add_argument("-p", "--packet_dir", default="knowledge_packets", help="(Ignored)")
    args = parser.parse_args()
    
    main(args.input_dir, args.output_dir, args.db_dir, args.packet_dir)
