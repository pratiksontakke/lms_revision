Here are the full lecture notes in markdown format:

**Human:**
You are a world-class technical note-taker trained to convert full lectures into complete notes.

### Multi-Modal QA Agent

A Multi-Modal QA (Question Answering) agent is a system that can process and understand multiple types of inputs, typically combining vision (images) and language (text). It takes an image input (either uploaded directly or via a URL) and uses a vision plus language model to analyze the image and respond to user queries about it.

The agent should also allow a fallback to a text-only LLM if image processing fails. It can visualize bounding boxes or key areas of the image if the API response supports it. Example: You can use models like GPT-4o Gemini or any multi-modal capable LLM.

Sample pseudo-code:

```markdown
image_url = "http://example.com/image.png"
user_query = "What is in the image?"
response = multi_modal_llm.ask(image=image_url, prompt=user_query)
print(response)
```

### Reasoning LLMs and Chain-of-Thought

Reasoning LLMs are specialized large language models trained to generate answers along with intermediate reasoning steps or 'thoughts'. They produce sequential tokens representing both the reasoning process and the final answer.

They are trained on datasets that include explicit step-by-step reasoning. These models often have larger output token windows to accommodate longer reasoning chains. Reinforcement learning techniques like RLHF (Reinforcement Learning with Human Feedback) are frequently used to improve these models.

Example of reasoning flow:

```markdown
User input: What is 12 multiplied by 7?
Model output:
- Step 1: 10 x 7 = 70
- Step 2: 2 x 7 = 14
- Step 3: Sum these two results: 70 + 14 = 84
Answer: 84
```

Reasoning models typically generate this chain-of-thought explicitly, improving accuracy. Normal LLMs can use prompt engineering to mimic this behavior by instructing them to think step-by-step, although specialized reasoning LLMs tend to perform better.

### Test-Time Compute in LLMs

Test-time compute refers to the computational resources consumed during the inference phase of an LLM, i.e., when the model generates outputs. Certain reasoning LLMs utilize more test-time compute to generate longer, stepwise outputs during inference. This is in contrast to training-time compute, which is the computational effort during model training.

Increasing test-time compute (e.g., by allowing longer output sequences or multi-step reasoning) can improve accuracy even when the model is already trained and its training-time performance hits a plateau.

Illustration:

```markdown
Training phase: Model learns from data.
Inference phase (test-time): Model generates answers, optionally with many intermediate tokens.
More tokens generated during inference => more compute used during test-time => potentially higher accuracy.
```

### LLM Inferencing and Frameworks

LLM inferencing is the process of running a trained LLM model to generate outputs given inputs. Inference generates tokens one at a time sequentially. Each generated token is appended to the input context for generating the next token.

On servers handling multiple users, distributed inference is necessary to handle parallel requests using multiple GPUs. Inferencing frameworks:

* OLama (O-Lama): Optimized for running LLMs locally, suitable for edge devices with limited parallelism.
* VLLM: A framework optimized for fast, distributed inference on servers, handling multiple GPUs and large workloads.

Example:

```markdown
User: What is the capital of USA?
Model generation:
1. 'Washington' (append to context)
2. ' DC' (append to context)
3. '.' (end of sequence token)
Output: 'Washington DC.'
```

### Context Window in LLMs and Its Challenges

The context window refers to the maximum number of tokens an LLM can process at once. Larger context windows allow processing more input text or history. Attention mechanisms in transformers weigh tokens to focus on relevant parts of the context.

Challenges with large context windows:

* Accuracy can degrade as the context window grows very large due to token confusion.
* Larger windows slow down model inference.
* Very large training datasets containing long sequences to train on are expensive and rare.

Use cases:

* Summarization benefits from large windows to capture entire documents.
* Retrieval Augmented Generation (RAG) selectively passes relevant context to the model instead of entire documents, improving accuracy.

Example:

```markdown
Model with 8K tokens window vs. model with 120K tokens:
- 8K tokens might be insufficient to cover full document.
- 120K tokens possible but answer quality may degrade.
```

Techniques like chunking, chaining outputs, or selective input reduce token overload. Ongoing research improves models' handling of longer contexts.

### Retrieval Augmented Generation (RAG)

RAG is a technique where instead of passing the entire context to the LLM, only relevant pieces are retrieved and passed as input. It helps overcome the context window size limitations. Improves accuracy by limiting irrelevant data.

RAG systems have a retrieval module (e.g., search or vector similarity) and a generative LLM. Typical Flow:

```markdown
User asks a question.
Retriever fetches: NASA's Apollo mission summaries.
LLM generates: "The Apollo missions ran from 1961 to 1972 with Apollo 11 being the first moon landing mission in 1969."
```

RAG must be explicitly integrated into applications; base LLMs do not automatically switch to RAG.

### Function Calling in LLMs

Function calling is a mechanism that allows LLMs to request programmatic functions to be executed when an answer requires external data or operations. The LLM itself does not execute the function but decides which function to call and with what arguments.

The application executes the function and returns the results to the LLM. This allows LLMs to access real-time data (e.g., weather, calendar, email).

Steps for function calling:

1. Initialize LLM with a list of available functions (tools), each described with name, description, and parameters.
2. On user query, LLM decides if it needs to call a function.
3. LLM responds with the function name and arguments.
4. Application executes the function with arguments, returns output.
5. Output is fed back to LLM to generate the final user response.

Example: Weather Tool

```markdown
@tool
def get_current_weather(location: str) -> str:
    # Call external weather API
    return f"Sunny, 23C in {location}"

# LLM initialized with this function as tool
# User: What's the weather like in Tokyo?
# LLM: Calls get_current_weather("Tokyo")
# Application runs function, returns result
# LLM: Generates final answer to user.
```

Descriptions (docstrings) help LLM select the correct function. Multiple functions can be passed for complex applications. Function error responses are passed back to LLM, enabling graceful error handling.

***Library:** LangChain is often used to streamline function/tool integration with LLMs.

### Summary and Recommendations

The lecture covered key advanced topics in Large Language Models and AI coding tools including:

* Multi-modal LLMs for vision and language tasks.
* Reasoning-capable LLMs generating step-by-step thought processes.
* The importance of test-time compute for inference quality.
* Different frameworks optimized for LLM deployments (OLama, VLLM).
* Challenges with context window size and solutions like RAG.
* Modern LLM function calling architecture for real-time dynamic content.

For practical implementations:

* Use dedicated multi-modal models for image+text tasks.
* Use chain-of-thought prompting or reasoning LLMs for complex logical tasks.
* Optimize deployment based on expected user load.
* Avoid passing large irrelevant context; use retrieval-based techniques.
* Integrate function calling to extend LLMs beyond static knowledge.

Feedback from students indicated varying prior knowledge; the pace and detail should be balanced for better understanding.

Additional suggested resources:

* OpenAI API function calling docs: https://platform.openai.com/docs/guides/gpt/function-calling
* LangChain documentation for function and tool integration: https://python.langchain.com/docs/modules/agents/tools/
* Papers and blog posts on reasoning LLMs and chain-of-thought techniques.