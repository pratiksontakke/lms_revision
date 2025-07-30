These are full lecture notes on LangGraph, a technical note-taking system. The notes cover various topics such as:

1. **Human Assistant Tool**: A tool that allows humans to interrupt the graph execution and provide input.
2. **Conditional Edges**: Using routing functions or built-in conditions to determine the flow of the graph.
3. **Tools**: Integrating external functions into the chatbot, such as calculators or web searches.
4. **Persistent Memory**: Using checkpointers linked by thread IDs to remember past interactions across multiple graph invocations.
5. **Interrupt and Command**: Pausing the graph execution and waiting for human input, then resuming with the provided response.

The notes also provide examples of how to implement these concepts using LangGraph, including:

1. **Chatbot Node**: Processing user queries and generating responses.
2. **Tool Node**: Executing tools called by the LLM during the agent workflow.
3. **Custom Tool Conditions**: Defining custom routing functions to determine whether to call tools or end the graph.

Overall, these notes provide a comprehensive overview of LangGraph's features and how they can be used to build complex chatbots and conversational agents.