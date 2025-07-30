Here are the full lecture notes in markdown format:

**Pre-training of LLMs**
=====================

* Large datasets (50+ TB) are collected and cleaned.
* Text is tokenized into manageable units (tokens can be words, subwords, or characters).
* The model predicts the next token's probability distribution.
* The predicted output is compared with the actual token to compute loss.
* Loss is backpropagated to update the weights using optimization algorithms like stochastic gradient descent.
* This process repeats billions of times to improve accuracy.

**Tokenization in LLMs**
=====================

* Tokens can be words, subwords, or characters.
* Using subwords helps the model handle unknown or rare words by combining known smaller units.
* Different models use different tokenization strategies.
* A tokenizer maps tokens to unique IDs (integers), which are fed into the neural network.

**Neural Network Training and Weight Updates**
=====================================

* Inside the LLM, training is performed by neural networks with millions/billions of parameters (weights).
* During pre-training:
	+ The input tokens are passed to the model.
	+ The model predicts the next token's probability distribution.
	+ The predicted output is compared with the actual token to compute loss.
	+ Loss is backpropagated to update the weights using optimization algorithms like stochastic gradient descent.
	+ This process repeats billions of times to improve accuracy.

**Inference Process in LLMs**
=====================

* Inference is the process of generating output from the trained LLM given input tokens.
* The model predicts one token at a time.
* After predicting a token, it appends that token to the input sequence.
* The extended sequence is fed back to the model for the next token prediction.
* This continues until a stop condition is met (like special stop tokens or max length).
* Temperature is a parameter influencing randomness in token selection. Low temperature favors high probability tokens (more deterministic), while high temperature increases diversity.

**Post-training (Supervised Fine-Tuning)**
=====================================

* Post-training is a supervised learning phase to fine-tune the pre-trained LLM, guiding it to produce more appropriate, human-like answers.
* It uses labeled datasets of inputs paired with correct outputs (e.g., question-answer pairs).
* Model predictions are compared directly against target outputs.
* Loss is computed and used to update the model weights.
* This phase takes less time than pre-training as it works on smaller, curated datasets.

**Reinforcement Learning from Human Feedback (RLHF)**
=====================================================

* RLHF aligns the model's behavior with human values and preferences by using human feedback to reward or penalize generated outputs.
* Humans rank model-generated responses for prompts.
* Rankings are used to train a reward model.
* The LLM is further fine-tuned using reinforcement learning algorithms, with the reward model guiding improvements.

**Bias and Limitations in LLMs**
=====================

* LLMs are trained on large-scale internet data, which can contain biases, outdated, or imbalanced information.
* This results in:
	+ Biases reflected in outputs (e.g., stereotypes like 'beautiful' being more probable with 'woman').
	+ Incomplete or incorrect knowledge, especially about recent or less common topics.
	+ Hallucinations where the model invents plausible but incorrect information.

**Prompt Engineering and Context Usage**
=====================================

* Prompt engineering involves crafting input prompts carefully to guide the LLM towards desired outputs, especially when the model is only pre-trained or post-trained but not fine-tuned for the exact task.
* By including examples or instructions in the prompt, the model's task understanding improves.
* Context length (number of tokens model can consider) is a limitation but varies by model.

**Common Practical Considerations in LLM Usage**
=====================================================

* Caching: To maintain consistency for repeated queries, caching previously generated responses avoids variability.
* Hardware: Large models need powerful GPUs to make sequential token predictions quickly.
* Model Size and Fine-Tuning: Bigger models are harder and costlier to fine-tune; smaller models or subsets (7B, 3B parameters) are typically used for specific tasks.
* Context Window: Different models support different maximum input lengths (e.g., GPT-4 supports up to 128k tokens).
* Attention Mechanism: Model focuses on relevant tokens to handle long and complex contexts effectively.