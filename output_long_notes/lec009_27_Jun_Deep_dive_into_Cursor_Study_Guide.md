**Lecture Notes**

# Introduction to No-code Tools for AI Agent Building

No-code tools have become popular for building AI agents without deep coding knowledge. Two notable tools are n8n and LangFlow.

* n8n: An open-source tool providing automation and integration between multiple services like Slack, Jira, Notion, and others. Allows AI model integration to build AI workflows and agents with drag-and-drop tools.
* LangFlow: Visual AI application builder akin to n8n but specifically designed for LangChain environments.

# Understanding How Cursor Understands the Codebase

Cursor does not fully understand your entire project codebase. Instead, it uses a retrieval augmented generation (RAG) approach:

* It indexes your project files and creates embeddings (vector representations) for code snippets using tools like tree-sitter to parse folders, files, classes, and functions.
* When you ask a question, it performs semantic similarity search on these embeddings to find relevant files or functions.
* Based on the selected files, Cursor provides only relevant snippets (limited by the model's context window) as context to the language model to generate responses.

# Context Window and Modes in Cursor

Cursor operates under the constraint of a context window size, which limits the amount of code it can process at once:

* The Normal Mode takes approximately 250 lines of code per file.
* The Max Mode can take about 750 lines per file by making multiple calls to the model to incrementally include more context.

# Managing and Providing Context to Cursor

How you provide context to Cursor affects the quality of code generation or debugging:

* Attach relevant project files or folders.
* Create markdown files like project.md describing your project's architecture, key entities, and database schema.
* Use screenshots with annotations to explain UI errors or issues visually.
* For API integrations, first test APIs interactively in Jupyter notebooks or playgrounds, then feed working samples as context to Cursor.

# Handling Third-Party API Integration with Cursor

Integrating third-party APIs directly through Cursor can be problematic due to:

* Frequent API changes and version updates.
* Subtle complexities in parameters and authentication.
* Cursor's AI model having fixed training data that may not reflect latest API docs.

Best Practice: Use a playground environment (e.g., Jupyter notebook) to interactively develop and test API code snippets. Once tested, pass the working code snippet as context to Cursor for integration into your project.

# Debugging Code with Cursor

Debugging with Cursor is enhanced by providing detailed context:

* Provide the specific function code and request Cursor to insert logging or print statements.
* Gather terminal logs (input/output data) and provide them back to Cursor for better understanding.
* Request line-by-line explanation of function logic to make debugging more transparent.

# Cursor Tools and Operational Modes

Cursor offers different operational modes and a set of tools for working with your codebase:

* Tools: Edit file, read file, delete file, terminal command run, codebase search (regex and embedding-based), web search, list directory, create diagrams, update memory, etc.
* Agent Mode: Cursor can automatically use available tools to complete assigned tasks.
* Ask Mode: Limited to search tools and answering queries without file editing or command running.

# Using Thinking Models for Test Case Generation

Generating test cases requires reasoning and creativity rather than just knowledge retrieval:

* Use specialized 'thinking' LLM models like jami 2.5 pro, o3, or clouder thinking models.
* Prompt Cursor to generate broad, functional test cases before asking it to write code.

# Advantages and Limitations of Wipe Coding with Cursor

Wipe coding allows rapid generation of MVP and application code using AI assistance but has practical limitations:

* AI may optimize or rewrite code based on its training, which might conflict with enterprise-specific design patterns or practices.
* Large enterprise projects have unique rules, data flows, and code architectures that AI cannot fully grasp.

# Best Practices for Understanding and Contributing to Open Source Projects

When contributing to real-world open-source projects:

* Use larger context window AI tools (e.g., AI.Dev with 1 million token context window) to ingest entire repositories.
* Restrict project scope by excluding irrelevant folders/files to manage token limitations.
* Use system prompts with detailed project information.

# Choosing the Right Model in Cursor Based on Your Task

Model selection affects Cursor's output quality:

* Use powerful models with larger context windows for precision tasks and large codebases (e.g., GPT-4.1, CloudA4sonnet).
* Use thinking models like jami 2.5 pro for tasks requiring reasoning such as test case generation and debugging.

# Key Skills Needed to Effectively Use Cursor and AI Coding Tools

Programming knowledge is crucial even when using AI coding assistants like Cursor:

* Understanding the language, design patterns, architecture, and project schema is necessary to interpret and validate AI outputs.
* Strong programming skills allow you to debug AI-generated code and maintain code quality.

**Additional Tips and Best Practices**

* Learning New Technologies: Watch conceptual overview videos. Use AI to explore common pitfalls and blind spots. Practice with small projects before larger implementations. Maintain hands-on coding experience.
* Workflow Optimization: Prompt sharing: Use screenshots when copy-paste limitations exist. Documentation habits: Keep learning notes and prompt templates. Skill development: Balance AI assistance with fundamental programming practice.

**Comparison: Cursor vs. Windsurf vs. VS Code**

Cursor:

* Strengths: Deep codebase understanding, RAG implementation, custom modes
* Ideal for: Complex projects requiring contextual code generation

Windsurf:

* Strengths: [Note: Specific details not provided in lecture summary]
* Ideal for: [Requires additional research for complete comparison]

VS Code with AI Extensions:

* Strengths: Extensive ecosystem, mature platform, plugin flexibility
* Ideal for: Developers preferring traditional IDE with AI augmentation