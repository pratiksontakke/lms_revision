These are the full lecture notes on Retrieval-Augmented Generation (RAG) and Re-ranking, which is a process where documents are retrieved based on a query and the information is used to generate an answer. The notes cover various topics such as:

1. **Streaming**: receiving responses from the Language Model (LLM) token by token or in chunks as they are generated, rather than waiting for the entire response to be ready.
2. **Langchain Prompts and Templates**: using templates to create reusable prompts with placeholders that can be dynamically filled.
3. **Output Parsers**: processing the output from the LLM and structuring it into a desired format.
4. **Document Loading and Splitting**: loading documents and splitting them into manageable chunks for processing.
5. **Embeddings**: converting text into vector form suitable for similarity search.
6. **Retrieval-Augmented Generation (RAG) and Re-ranking**: retrieving documents based on a query, using the information to generate an answer, and re-ranking the retrieved documents to improve relevance.
7. **Query Decomposition**: splitting a complex query into multiple smaller queries to improve retrieval completeness.

The notes also include examples of how to use Langchain's APIs for tasks such as:

* Using OpenAI Embeddings
* Setting up a Flash Re-ranker
* Creating a RetrievalQA chain
* Query decomposition

Additionally, the notes mention some modern tools or LLMs that perform query decomposition automatically.