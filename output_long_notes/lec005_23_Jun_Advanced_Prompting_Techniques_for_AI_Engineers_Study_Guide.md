**Lecture Notes on Large Language Models (LLMs) and Prompting**

### Introduction

Large language models (LLMs) are trained on vast amounts of internet data, enabling them to generate responses based on patterns learned from their training data. However, LLMs require careful guidance through **prompting** to produce desired outputs.

### Basic Rules for Effective Prompting

1. **Ensure fonts and content are clearly visible**: During demos or usage, ensure that the font size and style are legible.
2. **Interrupt politely if something is unclear**: If you don't understand a prompt or output, interrupt politely and ask for repetitions.
3. **Note down questions to handle during breaks**: To maintain session flow, note down questions to handle during breaks.

### Role Prompting

Role prompting involves instructing the LLM to adopt a particular persona or role (e.g., Shakespearean writer) to steer the style and tone of its response.

Example:

Prompt: "You are Shakespeare, write a sonnet about nature."
Output: (A sonnet written in Shakespearean style)

### Use of Delimiters in Prompts

Delimiters like XML tags, quotation marks, or special symbols can be used to explicitly define the start and end of different parts of the prompt.

Example:

<email>
Write a formal email inviting a colleague to a meeting.
</email>

### Sandwich Prompt Technique

The Sandwich Prompt Technique involves repeating key instructions at the beginning and end of the prompt to reinforce critical information.

Example:

Instruction: Provide a summary focused on environmental impacts.
Content: ...
Instruction: Please focus only on environmental impacts in the summary.

### Chain of Thought Prompting

Chain of Thought (CoT) prompting involves instructing the model to show its reasoning process step-by-step before providing a final answer.

Example:

Question: If a train travels 120 km in 2 hours, what is the average speed?
Prompt: "Answer the following question step-by-step."
Output:
Step 1: Calculate total distance = 120 km.
Step 2: Calculate total time = 2 hours.
Step 3: Average speed = distance / time = 60 km/h.

### Task Decomposition (Task Recomposition) and Query Decomposition

Task decomposition involves breaking down complex prompts or requests into smaller, manageable subtasks. This approach enhances LLM performance since handling simpler tasks individually is more effective.

Example:

User request: Analyze company financial health and forecast revenue.
Step 1 prompt to LLM: Break down 'Analyze company financial health' into 'Profitability analysis', 'Liquidity analysis', and 'Cash flow analysis'.

### Prompt Chaining and Sequencing

Prompt chaining refers to the technique where the output from one LLM prompt is fed as input to another LLM prompt, effectively chaining multiple prompts to work collaboratively on complex or multi-step tasks.

Example:

Prompt 1: Generate a 4-digit number related to the topic 'Renewable Energy'.
Output 1: 1234
Prompt 2: Validate if '1234' is related to 'Renewable Energy'. Respond with Yes or No.
Output 2: No

### Prompt Safety and Security Techniques

When deploying LLMs in enterprise or public applications, ensuring prompt safety is vital to prevent generation of unwanted, unethical, or harmful content.

Techniques include:

1. **Input Sanitization**: Use regular expressions (regex) or keyword filters to detect and reject disallowed inputs before sending to the LLM.
2. **Role-based Prompting**: Assign the LLM a restrictive role where it is explicitly instructed not to reveal sensitive data or generate unethical content.

### Visible Reasoning and Thinking in Prompts

To ensure that LLMs are genuinely reasoning about complex tasks, it is helpful to instruct them to output their 'thinking' or reasoning explicitly in the response. This makes the reasoning process visible and verifiable.

Example:

<thinking>
Step 1: Identify variables.
Step 2: Apply formula.
Step 3: Calculate result.
</thinking>

Final answer: 60 km/h

### Few-shot and Zero-shot Prompting

Few-shot prompting provides the LLM with a few example input-output pairs to demonstrate the desired task format or style. Zero-shot prompting relies on a single instruction without examples.

Example:

Few-shot:
Q: Capital of France?
A: Paris
Q: Capital of Japan?
A: Tokyo
Now answer:
Q: Capital of India?

Zero-shot:
Q: What is the capital of India?
A:

### Fine-tuning vs. Prompt Engineering

Fine-tuning is the process of training an LLM on specific datasets to specialize its behavior, while prompt engineering crafts the input prompts to steer a pre-trained LLM without further training.

Insights:

1. **Fine-tuning is costly and complex**: Compared to prompt engineering.
2. **Many use cases can be handled simply by well-designed prompt engineering**: (e.g., few-shot prompting).
3. **Fine-tuning is especially useful when domain-specific vocabularies or complex patterns are involved**: That few-shot prompting can't handle well.

### Use of Local Models and Tools

LLMs alone do not perform external tool usage such as calculations or web searches unless integrated into applications explicitly designed to provide such tools to the model.

Example: An LLM-based AI assistant might generate code to perform a calculation, run it in a separate environment, and then integrate the results in the conversation.

### Structured Output and Advanced Prompting Strategies (Preview)

Structured prompting involves instructing the LLM to return outputs in a specific format (e.g., JSON, XML) that is machine-readable and easier to parse by downstream systems.

Advanced prompt strategies discussed briefly include:

1. **Passing outputs sequentially to refine or validate responses**.
2. **Using supervisors or validators as separate agents in multi-LLM systems**.
3. **Preparing prompts to handle ethical and security concerns systematically**.

These will be covered in more detail in subsequent sessions.