Here is the full lecture notes in markdown format:

**Introduction to Limitations of Large Language Models (LLMs)**
===========================================================

Large Language Models (LLMs) have several limitations that impact their performance in various applications.

### Key Limitations:

* **Context Window Size**: LLMs have a limited context window (e.g., 128K tokens). This limits the model's ability to consider large amounts of data at once.
* **Knowledge Cutoff**: LLMs are trained on data up to a specific cutoff date and cannot provide accurate answers about recent events or updates.
* **Hallucination**: When LLMs do not know the correct answer, they may produce plausible but incorrect or irrelevant responses.
* **Contextual Understanding**: LLMs can struggle to fully understand and relate complex contexts, especially with new or specific data.
* **Computational Resources**: LLM inference requires significant GPU resources, especially when processing large context windows.

**Retrieval-Augmented Generation (RAG) - Basic Concept**
=====================================================

RAG is a technique to overcome some of the limitations of LLMs by augmenting their generation capabilities with a retrieval mechanism from an external memory base or knowledge source.

### How RAG works:

* Maintain a memory base or knowledge repository containing up-to-date and domain-specific information.
* When a user query arrives, retrieve relevant data chunks from this memory base.
* Pass the user query along with retrieved data to the LLM to generate answers grounded in the retrieved context.

**Benefits:**

* Solves the knowledge cutoff problem by providing the model with updated information.
* Improves contextual understanding by giving precise relevant context.
* Helps reduce hallucination by grounding responses in factual data.

**Pseudocode:**
```python
memory_base = load_organization_docs()
user_query = "When was the new analytics feature released?"
retrieved_chunks = retrieve_relevant_chunks(memory_base, user_query)
prompt = system_prompt + retrieved_chunks + user_query
answer = LLM.generate(prompt)
print(answer)
```
**Role of System Prompt in RAG**
================================

The system prompt is a crucial element in guiding the LLM to use the provided memory base and context properly.

### The system prompt instructs the LLM to:

* Answer only based on the provided knowledge base or documents.
* Avoid answering if the information is not in the memory base.
* Optionally cite sources from the memory base to improve reliability.

**Challenges with Passing Entire Document Context to LLM**
=====================================================

Passing the whole document or entire memory base as context to the LLM causes several challenges:

### Summarization Limitations:

* Retrieving limited chunks means the model may miss parts of the document necessary for full summaries.
* Solution: Increase number of chunks retrieved (at cost of latency) or pre-process document summaries.

**Inability to Impart Specific Behavioral Styles**
=====================================================

RAG cannot train or fine-tune the model to consistently exhibit complex behavior.

### Solution:

* Fine-tuning or extensive few-shot prompting with examples.

**Structured Data Challenges**
=============================

RAG is suited for unstructured text, not structured relational data from databases with multiple tables and relations.

### Solution:

* Use SQL agents that generate and execute SQL queries on structured databases based on user queries.

**API Data Handling**
=====================

When data exists behind APIs rather than text or DB, RAG cannot directly retrieve information.

### Solution:

* Use function/tool calling approaches where LLMs generate API calls with parameters that are executed to fetch results.

**Numerical Calculations**
=====================

LLMs struggle with complex calculations on retrieved numeric data.

### Solution:

* Call external calculator tools via function calling to ensure correct math.

**Example for SQL Agent:**
```python
user_query = "Provide top five customers from South region"
schema_description = "Customers(id, name, region), Orders(customer_id, amount)"
prompt = f"Given schema: {schema_description} Write SQL for: {user_query}"
sql_query = LLM.generate(prompt)
result = execute_sql(sql_query)
print(result)
```
**Example for API Calling:**
```json
{
  "function": "getAvailableCars",
  "parameters": {
    "manufacturer": "Nissan",
    "country": "India",
    "year": 2025
  }
}
```
Where the LLM generates the above JSON which triggers an API call.

**Function Calling and Tool Use to Extend LLM Capabilities**
=====================================================

Function calling allows LLMs to generate structured calls to external tools or services, bridging capability gaps.

### Example:

* A user wants the sum of sales figures extracted from documents. The LLM extracts numbers and calls a calculator function:
```json
{
  "function": "calculator",
  "operation": "add",
  "operands": [250, 300, 450]
}
```
The external system computes 1000 and returns result.

LLM answers: "The total sales are 1000 units."

This method helps overcome LLM computation and reasoning limitations.