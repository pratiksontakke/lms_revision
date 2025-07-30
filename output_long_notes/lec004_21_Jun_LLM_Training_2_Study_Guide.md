**Lecture Notes on Large Language Models (LLMs)**

**Introduction**

* LLMs are trained on vast amounts of internet text data to learn language facts, grammar, reasoning, and general knowledge.
* Pre-trained models act like sophisticated autocomplete systems but are not yet helpful assistants.

**Supervised Fine-Tuning (SFT)**

* SFT is the process of further training pre-trained LLMs to behave more usefully.
* It involves providing prompt-response pairs created by humans or other LLMs, where the response demonstrates how the model should answer.
* This training helps the model learn:
	+ How to respond correctly to specific questions
	+ Appropriate behavior and manners in responses
	+ Response control such as length (e.g., writing a short poem)
	+ Language translation knowledge
	+ Safety aspects (e.g., refusing to answer harmful queries)

**Limitations of LLMs**

* Difficulty solving complex math problems due to lack of exact numeric computation patterns in training data.
* Counting and character-level tasks are unreliable due to tokenization limitations.
* Struggle with creating contextually relevant jokes, memes, or humor due to subtle subjective cultural contexts.
* Hallucination: generating factually incorrect or fabricated answers.

**Reinforcement Learning from Human Feedback (RLHF)**

* RLHF is an advanced training phase where the model learns from human preferences to align its output with human values and preferences.
* Humans provide rankings for multiple model-generated responses for a prompt.
* A separate neural network called the 'reward model' is trained to predict these human rankings.
* The LLM is then fine-tuned to generate responses that receive higher scores from the reward model.

**Challenges and Biases in RLHF**

* Bias in human feedback: if human raters have biases, the reward model will learn those biases, leading to biased model behavior.
* Gaming the reward model: the LLM may learn to produce answers that score well on the reward model but are not genuinely better (reward hacking).
* Limitations of reward model: reward model predictions are not perfect, causing occasional poor ranking and reinforcement of undesired behavior.

**Thinking Models and Chain of Thought Prompting**

* Thinking Models or Chain of Thought (CoT) prompting involves training the model to generate intermediate reasoning steps before giving a final answer.
* Helps in complex problem-solving where step-by-step reasoning is required.
* Achieved by including multi-step reasoning answers in the fine-tuning dataset.

**Model Behavior with Token Trajectories and Sequential Generation**

* LLMs generate text sequentially, token by token, where each token is conditioned on previous tokens.
* The model learns certain token trajectories representing different types of responses.
* Tokens like `<|user|>`, `<|assistant|>`, and `<|system|>` help the model distinguish between different roles in the conversation.

**Use of Tools and Agents with LLMs**

* To extend the capabilities of LLMs beyond pure language modeling, modern systems integrate LLMs with external tools resulting in agent frameworks.
* Tools include web search, code interpreters, calculators, and knowledge bases.
* When uncertain or requiring exact computation, the LLM generates commands to invoke such tools.

**Differences in Fine-Tuning Between Industry and Large Model Developers**

* Large LLM developers typically fine-tune by updating the entire model's weights, which demands significant compute and data.
* In contrast, industry and domain-specific use cases often use efficient fine-tuning methods like LoRA (Low-Rank Adaptation).

**Training Infrastructure and Data Preparation**

* Effective training of LLMs involves large-scale data preparation and human involvement.
* Data includes prompt-response pairs, ranked human preferences, safety behavior examples, and creative writing samples.
* Experts in various domains contribute to generate high-quality fine-tuning data.
* Synthetic datasets can be generated using existing models to augment training data.