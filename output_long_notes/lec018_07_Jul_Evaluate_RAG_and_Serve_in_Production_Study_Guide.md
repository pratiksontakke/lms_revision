Here are the full lecture notes in markdown format:

**Overview of RAG (Retrieval-Augmented Generation) Workflow**
===========================================================

RAG integrates information retrieval with language models to provide contextual and informed responses. The key components of a RAG system include:

* User Query: The initial input from the user.
* Query Transformation: The user query is optimized or rewritten for better retrieval.
* Vector Search (Semantic Search): The query is used to search an embedding-based vector database to find similar context documents.
* Keyword Search: A keyword-based search to complement vector search and capture keyword-specific or domain-specific vocabulary.
* Hybrid Search: Combining vector search results and keyword search results.
* System Prompt & User Prompt: Inputs for the LLM.
* LLM (Language Model): Generates an answer based on the retrieved documents and prompts.

**Example Workflow**
-------------------

User Query -> Query Transformation -> Vector Search + Keyword Search (Hybrid Search) -> Retrieved Documents -> LLM with system and user prompts -> Generated Answer

**Query Transformation / Query Rewriting in RAG**
------------------------------------------------

Query transformation or query rewriting optimizes the user's input query before passing it to the RAG pipeline. It helps in:

* Making the query more specific by adding context from conversation history.
* Adding synonyms or related terms to improve retrieval quality.
* Removing filler or stop words to enhance vector or keyword search.
* Addressing jargon or domain-specific vocabulary to improve retrieval accuracy.

**Example Query Transformation Prompt:**
```
"Expand the following query with related terms and synonyms, keep it concise and focused on the same intent: 'tell me about JS Hero performance issue.'"
```

Pseudo Code:
```python
optimized_query = llm_rewrite_query(original_query, chat_history=None)
retrieved_docs_vector = vector_search(optimized_query)
retrieved_docs_keyword = keyword_search(optimized_query)
```

**Vector Search and Keyword Search in RAG**
------------------------------------------------

Vector Search uses embeddings to find semantically similar chunks of documents to the query. It's based on similarity metrics like cosine similarity.

Keyword Search matches keywords in the query with document chunks to capture exact terms or domain-specific vocabulary that may not be well represented in embeddings.

Hybrid Search combines results from both vector and keyword searches, prioritizes vector search results, and penalizes duplicates.

**Example Algorithm for Hybrid Search:**
```python
vector_results = vector_search(optimized_query, top_k=5)
keyword_results = keyword_search(optimized_query, top_k=3)
# Remove duplicates from keyword results
unique_keyword_results = [doc for doc in keyword_results if doc not in vector_results]
# Combine results with vector results at top
final_results = vector_results + unique_keyword_results
```

**Frameworks for Building RAG Applications**
------------------------------------------------

Several frameworks exist that simplify RAG application development:

* LangChain: Most popular, high-star GitHub repository, extensive abstraction, supports multiple LLMs, optimized implementations.
* LlamaIndex: Focuses more on data management and document parsing, stronger software principles, less popular but more specialized.
* Haystack: Production-ready, supports drag and drop for pipelines, less widely adopted.

**Choosing the Framework:**
Use LangChain if you want community support, ease, and multiple LLM compatibility. Use LlamaIndex if you need better data management. You can combine frameworks if dependency versions allow.

Example: Using LangChain
```python
from langchain.chains import RetrievalQA
qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=my_retriever)
answer = qa.run(query)
```

**Testing RAG Systems with RAGAS Framework**
------------------------------------------------

Testing RAG systems manually is infeasible for large-scale applications. RAGAS is a popular framework to automate testing using a bigger LLM as a judge. It evaluates multiple metrics:

* Faithfulness: How well the LLM's answer aligns with the retrieved context.
* Answer Relevance: How well the answer addresses the original user query.
* Context Precision: How relevant the retrieved documents/chunks are to the query.
* Context Recall: Whether the retrieved context contains all needed information.

**Basic Conceptual Example of Faithfulness Evaluation:**
```python
def faithfulness(answer, context):
    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())
    overlap = len(answer_words.intersection(context_words))
    return overlap / len(answer_words)
```

Using RAGAS: Prepare a golden dataset of query-expected answer pairs and run RAGAS to get metric scores and evaluation reports.

**Building and Expanding Evaluation Datasets**
------------------------------------------------

Creating a high-quality evaluation dataset is crucial:

* Start with a small set of queries/prompts (minimum 5) and expected answers.
* Collect feedback from stakeholders and business domain experts to expand and diversify this dataset.
* Include varied query types, multi-turn conversations, and edge cases.
* Synthetic Data Generation: Larger LLMs (like GPT-4 or Jeminai) can generate diverse or challenging queries and answers to augment the evaluation set.

Example:
```json
[
  {"query": "What are the best practices of JS Hero?", "expected_answer": "Use modular architecture and efficient state management..."},
  {"query": "Tell me about JS Hero latency.", "expected_answer": "The typical latency is under 100ms for most operations..."}
]
```

**Debugging RAG Systems**
-------------------------

Handling Concurrency, Rate Limiting, and Performance in Production:

* Large documents mean thousands of chunks needing embeddings.
* Embedding calls must be asynchronous and parallelized for speed.
* Third-party APIs like OpenAI impose rate limits (e.g., 20-80 calls per minute).
* Use rate limiters and retry mechanisms to stay within API limits.

Example: Asynchronous embedding calls using Python asyncio:
```python
import asyncio

async def embed_chunk(chunk):
    return await openai_embedding_api(chunk)

async def embed_all_chunks(chunks):
    tasks = [embed_chunk(chunk) for chunk in chunks]
    embeddings = await asyncio.gather(*tasks)
    return embeddings
```

Batch API usage example (conceptual):
```json
POST /v1/embeddings/batch
{
  "documents": ["doc1", "doc2", ...],
  "model": "text-embedding-xyz"
}
```

**Caching in RAG Applications**
--------------------------------

Caching is critical for improving response time and reducing cost:

* Cache responses to repetitive queries especially for queries like "Summarize this page" where context is the same.
* Use fast in-memory caches like Redis or internal caches.
* Cache keys can be query strings or hashes of queries.
* Cache not only user answers but also intermediate retrieval results.

Example using Redis in Python:
```python
import redis

cache = redis.Redis()

query_key = f"summary:{hash(query)}"
response = cache.get(query_key)
if response is None:
    response = llm_generate_summary(query)
    cache.set(query_key, response, ex=3600)  # cache for 1 hour
else:
    response = response.decode('utf-8')
```

**Testing AI Applications with LLM as a Judge and Metrics**
---------------------------------------------------------

RAG testing can be automated using a bigger LLM to evaluate other model's outputs.

The LLM acts as a judge or evaluator. It computes metrics such as faithfulness, answer relevance, context precision, and recall. RAGAS framework facilitates this automated evaluation process. The evaluation involves comparing generated answers against expected answers and retrieved contexts.

Example Flow:

User Query + Retrieved Documents -> Smaller LLM -> Answer
Answer + Retrieved Documents + Expected Answer -> Larger LLM as Judge -> Evaluation Scores

**Test-Driven Development in AI Application (Evolution Driven Design - EDD)**
--------------------------------------------------------------------------------

The traditional software test-driven development (TDD) concept is applied in AI as Evolution Driven Design (EDD):

* First, create a test/evaluation dataset (queries and expected results).
* Then develop features or improve models to pass those tests.
* Helps keep AI development aligned with business requirements and user intent.
* Ensures iterative quality improvement.

Example: Create a JSON dataset of queries and expected answers before developing the retrieval and generation components:
```json
[
  {"query": "What is latency of JS Hero?", "expected_answer": "Latency is under 100ms..."}
]
```

Then develop the RAG system to produce correct answers for these tests.