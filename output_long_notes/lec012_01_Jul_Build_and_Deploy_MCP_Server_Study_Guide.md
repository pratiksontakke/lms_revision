Here are the full lecture notes in Markdown format:

**Introduction to Model Contest Protocol (MCP)**
=====================================================

MCP is a standardized protocol designed to provide AI models access to external content such as tools, prompts, and resources. MCP defines a set of rules for how AI models get and use content, making integration across many AI applications easier and more uniform.

**Problem MCP Solves**
--------------------

Before MCP, each API provider had its unique API styles. Consumers (like AI language models or applications) had to adapt to each API separately, leading to integration overhead and instability due to frequent API updates.

MCP addresses this by:

* Defining a uniform API format called MCP style APIs.
* Encouraging API producers (vendors) to expose their APIs via MCP servers.
* Allowing consumers (AI apps) to use MCP clients to interact with any vendor's MCP server in a standardized way.

**Benefits**
------------

Ease of integration for consumers.
Vendors can increase usage and popularity of their APIs without extra integration work from the client side.

**MCP Server and Client Concept**
---------------------------------

### MCP Server

This is the server exposing APIs/tools/prompts/resources in the MCP protocol format. Built using libraries like fast-mcp. Converts vendor-specific APIs into MCP tools, prompts, or resources.

### MCP Client

Client applications use this to consume MCP servers. It acts as a mediator to call MCP tools/prompts/resources uniformly without worrying about vendor-specific implementation.

**Example of a basic MCP server initialization code snippet in Python:**
```python
from fast_mcp import MCP

mcp = MCP(name="bitbucket", description="Bitbucket MCP server to manage repos and pull requests")

@mcp.tool()
def list_repositories():
    # Implementation for listing repositories
    pass

if __name__ == "__main__":
    mcp.run_async()
```

**Example of a simple MCP client usage:**
```python
from fast_mcp import MCPClient

client = MCPClient(
    command="python",
    args=["bitbucket_mcp_server.py"]
)

response = client.list_repositories()
print(response)
```

**Bitbucket MCP Server Implementation**
--------------------------------------

A real-world implementation example covered was building an MCP server to expose Bitbucket API functionalities as MCP tools.

Key steps:

* Creating a Bitbucket client for direct API communication.
* Wrapping Bitbucket API calls as MCP tools: list repositories, get pull requests, add comments, approve pull requests.
* Using environment variables to securely store Bitbucket credentials.
* Running the MCP server asynchronously to support parallel tool calls.

**Setting environment variables example:**
```python
import os

BITBUCKET_USERNAME = os.getenv('BITBUCKET_USERNAME')
BITBUCKET_APP_PASSWORD = os.getenv('BITBUCKET_APP_PASSWORD')
BITBUCKET_WORKSPACE = os.getenv('BITBUCKET_WORKSPACE')
```

**Parallel Tool Execution in MCP Server**
-----------------------------------------

MCP servers can be made asynchronous to handle multiple tool calls in parallel. This improves efficiency, especially under multiple concurrent user requests.

Example using fast-mcp run_async:
```python
if __name__ == '__main__':
    mcp.run_async()
```

**Testing MCP Servers with MCP Clients**
------------------------------------------

Testing is essential to ensure MCP tools perform as expected. A test script using MCP client can automate sending tool calls and checking responses.

This is particularly useful during development to avoid repeatedly restarting and testing in external applications.

Example test script snippet:
```python
from fast_mcp import MCPClient

client = MCPClient(command="python", args=["bitbucket_mcp_server.py"])

def test_list_repos():
    repos = client.list_repositories()
    assert 'repositories' in repos

if __name__ == '__main__':
    test_list_repos()
    print("Test passed")
```

**Wipe Coding and AI Assisted Development with MCP**
---------------------------------------------------

Wipe coding refers to writing code assisted by AI-based tools (e.g., ChatGPT, GitHub Copilot).

MCP server development can be challenging for AI tools due to the novelty of the protocol.

To improve AI coding assistance:

* Provide documentation links as context.
* Use files like llms.tst that standardize instructions for LLMs on library usage.
* Provide test scripts so AI can test and refine code.
* Using well-structured instructions (e.g., in VSCode's copilot instructions) improves AI generated code quality by defining task divisions and rules.

**Assignment Overview: Building a Simple MCP Server**
---------------------------------------------------

For practice, build a simple MCP server with the following characteristics:

* Tools:
	+ Analyze document (e.g., get sentiment, extract keywords, readability scores)
	+ Get sentiment of a document
	+ Extract keywords
	+ Search documents
* Internal setup:
	+ Store sample documents locally or in a database.
	+ APIs perform analysis on documents, then are exposed as MCP tools.

This assignment provides a hands-on introduction to building MCP servers for practical use cases.