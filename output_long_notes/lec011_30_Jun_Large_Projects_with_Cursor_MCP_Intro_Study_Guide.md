Here is the full lecture note in markdown format:

**Introduction to MCP (Model-Constructed Protocol)**
=====================================================

MCP stands for Model-Constructed Protocol, which provides a standardized way for AI applications to interact with external tools and APIs. It acts as an intermediary layer that simplifies the integration of various services such as Notion, Google Drive, and others.

**Problem MCP Solves: Integrating Multiple External APIs**
--------------------------------------------------------

Integrating multiple external APIs requires custom API code for each integration. This results in repetitive and complex integration tasks when connecting AI applications to multiple services.

**How MCP Helps: Standardizing Communication Rules**
---------------------------------------------------------

MCP standardizes the communication rules (protocol) so that developers can use a common framework to connect to different APIs without writing custom integrations repeatedly. This democratizes API integration by making it reusable and easy to connect to multiple services.

**Example: Integrating Notion and Google Drive with MCP**
--------------------------------------------------------

Suppose you have developed a Slack clone and want to integrate Notion and Google Drive functionalities. Instead of writing separate integration code for each, you can use MCP clients and servers to communicate with these services using the same protocol, making the process reusable and simpler.

**MCP Architecture and Components**
------------------------------------

MCP consists mainly of two components:

* **MCP Client**: Runs on the AI application side (e.g., your Slack clone). It sends requests to the MCP Server following MCP protocols.
* **MCP Server**: Runs on the external tool provider's side (e.g., Notion, Google Drive). It translates MCP requests into actual API calls of the external service.

**Benefits of MCP Protocol**
-----------------------------

MCP provides several key benefits:

* Standardization: MCP protocol defines a common set of rules for communication between AI applications and external tools.
* Code Reusability: Developers write reusable code that can work with multiple APIs, only varying inputs and outputs.
* Easy Integration: No need for custom integration for every external tool; MCP servers expose standardized toolsets.
* Democratization: MCP allows external tool providers to easily expose their APIs to the AI ecosystem, increasing their reach and utility.

**Building an MCP Server with Python and FastMCP**
---------------------------------------------------

To build an MCP server, you can use the FastMCP library in Python. The server exposes tools as functions that the AI applications can call via MCP.

Basic Steps:

1. Initialize a Python project using a package manager like uv
2. Install fast-mcp library
3. Define an MCP server with tools as functions using FastMCP decorators
4. Run the server locally or remotely

**Example MCP Server (Math Tool)**
---------------------------------

```
from fast_mcp import MCP

mcp = MCP(name='MatTool', description='Tool for mathematical operations')

@mcp.tool
def add(x: int, y: int) -> int:
    '''Add two numbers'''
    return x + y

@mcp.tool
def multiply(x: int, y: int) -> int:
    '''Multiply two numbers'''
    return x * y

if __name__ == '__main__':
    mcp.run()
```

**Using MCP Server with AI Applications and Clients**
--------------------------------------------------------

To connect your AI application to an MCP server (e.g., the math tool created previously), you use an MCP client usually embedded within frameworks or SDKs such as Cloud, LangChain, or Cursor.

How to Configure Client: You tell the client how to run or access the MCP server by providing a command or URL, for example:

```
{
  "mat_tool": {
    "command": "uv",
    "args": ["run", "-m", "fast_mcp", "run", "mcp_tool/main.py"]
  }
}
```

**MCP Marketplace and Available Tools**
-----------------------------------------

MCP supports a marketplace concept where MCP servers/tools are shared or available for developers to integrate seamlessly.

Example Tools in MCP Marketplace:

* Google Drive
* Notion
* Web Search
* Various Databases

Each MCP server exposes multiple tools/functions, which can be browsed and used by AI developers.

**Benefits:**

* Instant access to a wide variety of tools without custom API coding.
* Democratization favors both tool developers (easy exposure) and AI developers (easy consumption).
* Developers can find MCP servers on platforms like Smithri and Cursor using MCP clients to consume those APIs.

**MCP Server Types: Standard I/O and HTTP Streaming**
---------------------------------------------------------

There are two main types of MCP server implementations:

* **Standard Input/Output (StdIO)**: The default type where the server reads input and writes output via the standard streams. This is generally used for local or simple setups.
* **HTTP with Streaming (STTP)**: A server running over HTTP network protocol, supporting request streaming. Useful for remote deployment or web-accessible MCP servers.

**Security Considerations in MCP**
-----------------------------------

While MCP provides standardization and ease of integration, using external MCP servers can lead to security risks if unauthorized or malicious servers are used.

Risks:

* Data leakage: External MCP servers can potentially access sensitive data passed from your AI application.
* Unauthorized servers may intercept or misuse data.

Best Practices:

* Always use MCP servers provided or authorized by trusted service providers.
* Avoid using anonymous or third-party MCP servers without proper trust.
* Be aware that using MCP servers trades some control for ease-of-integration.
* In enterprise environments, native API calls and custom integration are often preferred to maintain control and security.

**Comparison Between MCP and LangChain Tools**
---------------------------------------------------

LangChain and MCP provide ways to extend AI applications with external tools, but they have distinct scopes and usage contexts:

* **LangChain Tools**: Framework-specific toolkits. Limited to the tools supported by LangChain. Requires custom integration for unsupported APIs.
* **MCP**: Protocol applicable across multiple frameworks and clients. Provides a broad marketplace of tools easily integrated. Better for tool providers to expose APIs for wider AI ecosystem.

When to prefer MCP:

* When you want a tool to be usable by multiple AI frameworks.
* When using tools not available in LangChain.
* When to prefer LangChain tools:
	+ When working exclusively within LangChain framework.
	+ When using in-house or limited set of tools.

**MCP for Sharing Prompts and Resources (Additional Features)**
---------------------------------------------------------

Besides exposing tools, MCP can also be used to share prompts and resources across AI applications.

Prompt Sharing: Share prompt templates or chains that can be invoked remotely. For example, a resume improvement prompt library can be exposed as an MCP prompt.

Resource Sharing: Share databases, PDFs, or other resources as inputs to AI applications via MCP.

Example of Exposing Prompt via MCP:

```
@mcp.prompt
def improve_resume(text: str) -> str:
    """Prompt to improve resume"""
    # prompt template logic
    return improved_text
```