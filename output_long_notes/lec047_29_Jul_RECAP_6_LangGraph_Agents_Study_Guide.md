Here are the full lecture notes in markdown format:

**Introduction to LangGraph Agents**
=============================

LangGraph is a framework to build end-to-end agents, covering the entire lifecycle from building to deployment. An agent here refers to an AI-powered system which can process user inputs, perform actions like calling tools, and respond accordingly.

### State Graph and Basic Agent Flow

A core concept in LangGraph is the State Graph which represents the flow of the agent.

* Define a state which holds data such as conversation messages.
* The graph consists of nodes (e.g., chatbot node) and edges depicting flow from one node to another.
* The graph starts with a start node and ends at an end node.
* Messages are stored in a list that appends rather than overwrites, maintaining conversation context during the session but not persisting across restarts.

Example: A simple graph that takes input from the user, processes it through an LLM, and provides output.

```markdown
from langgraph import state_graph, start, end, add_messages

state = {"messages": []}  # State holding messages

graph_builder = state_graph(state)
graph_builder.add_node('chatbot_node')  # Define chatbot node
# Add start and end points
graph_builder.add_edge(start, 'chatbot_node')
graph_builder.add_edge('chatbot_node', end)

# The chatbot node calls LLM to generate response based on messages

# Loop to take user input
while True:
    user_input = input('User: ')
    if user_input.lower() in ['quit', 'exit', 'q']:
        break
    # Add user input to messages
    add_messages(state['messages'], {'role': 'user', 'content': user_input})
    # Generate response from LLM
    response = llm.invoke(state)
    add_messages(state['messages'], {'role': 'assistant', 'content': response})
    print('Assistant:', response)
```

This flow is straightforward but limited as it lacks tools and human involvement.

### Incorporating Tools Into Agents

LangGraph supports integration of external tools with agents. Tools can be any external services or APIs that the agent can invoke to get additional data or perform specific actions.

* A common example used is integration with the Tavily API for web search.
* When the LLM detects it needs external information, it can conditionally invoke a tool.
* Tools are added as nodes in the graph.
* Conditional edges allow agent flow to decide when to invoke tools or continue normal response.

Example: Adding a web search tool node to the graph and conditionally invoking it.

```markdown
from langgraph import state_graph, start, end, add_tools_node, tools_condition
from langgraph.messages import add_messages
import tavily

state = {"messages": []}

graph_builder = state_graph(state)

# Initialize LLM with tools
llm_with_tools = llm.bind_tools([tavily_search_tool])

# Add chatbot node with bound tools
graph_builder.add_node('chatbot_node', llm_with_tools)

# Add tool node
graph_builder.add_tools_node('tavily_tool')

# Conditional edge: if LLM wants to use web search tool
graph_builder.add_edge('chatbot_node', 'tavily_tool', condition=tools_condition)

# Edges for start and end
graph_builder.add_edge(start, 'chatbot_node')
graph_builder.add_edge('tavily_tool', end)
```

This improves the agent's capability by invoking tools to get real-time information.

### Conditional Edges and Decision Making

Conditional edges control the flow of execution between nodes based on conditions evaluated at runtime.

* The LLM generates a key indicating which tool or node to go to next.
* The graph uses these keys to decide which conditional edge to follow.
* This enables building complex multi-path agents where multiple tools or sub-agents are available.

Example: Conditional edge example in LangGraph

```markdown
# Conditional function to check if tool call is 'web_search'
def is_web_search_call(message):
    return message.get('tool_call') == 'web_search'

# Add conditional edge
graph_builder.add_edge('chatbot_node', 'web_search_tool', condition=is_web_search_call)
```

In larger architectures, this enables routing requests dynamically.

### Agent Architectures in LangGraph

There are several types of agent architectures:

* Single Agent: One LLM calling multiple tools.
* Network of Agents: Multiple agents sharing a common state and collaborating.
* Supervisor Agent: A top-level agent that controls sub-agents.
* Hierarchical Agents: Agents arranged in layers controlling subtasks.
* Custom Agents: Tailored agents triggered on specific events, e.g., Slack message triggers an agent that books meetings.

These architectures enable scalable and modular AI systems.

### Memory in LangGraph Agents

Two types of memory are discussed:

* Short-term memory: Stored in the agent's state during a single session.
* Long-term memory: Persisted in external databases (e.g., Postgres, SQL) that store conversation history across sessions.

Managing memory allows the agent to maintain context or learn over time.

### Time Travel Feature

Time Travel refers to the ability to revert the agent's state to a previous checkpoint in the conversation or processing flow.

* The agent stores key-value pairs with unique IDs representing each state change.
* This allows undoing incorrect LLM outputs or tool calls.

Example Scenario: If the agent generated wrong code at step 5, you can revert to state before step 5 and generate a new response.

### Human-in-the-Loop Mechanism

Human-in-the-Loop (HITL) is used when critical decisions are needed.

* The agent processes user input and generates a response or action.
* Before performing sensitive actions (e.g., sending an email), the agent requests human approval.
* Human confirms or rejects the action.
* If approved, the action proceeds; else it is aborted.

Example: Email agent flow with human approval.

```markdown
while True:
    # Generate email draft response
    draft_response = llm.invoke(state)
    print('Draft response:', draft_response)

    approval = input('Approve to send? (yes/no): ')
    if approval.lower() in ['yes', 'y']:
        send_email(draft_response)
        print('Email sent.')
        break
    else:
        print('Email sending aborted.')
        break
```

This mechanism is especially important for agents that act autonomously.

### LangGraph Platform for Deployment

LangGraph Platform enables developers to deploy their agents to production with ease.

* Allows demo deployment and scaling to production.
* Supports up to one million node executions per year with free and paid tiers.
* Developers can build, test, and deploy agents using this platform for real-world applications.

**Assignment Overview and Best Practices**
=====================================

The assignment involves building an email agent with capabilities:

* Read emails
* Compose email drafts
* Respond to emails
* Search web as needed
* Implement human-in-the-loop approval before sending emails

Students are encouraged to research documentation, understand the code, and avoid copy-pasting solutions without comprehension.

Building the habit of debugging and exploring official docs is emphasized for mastering new and evolving technologies.