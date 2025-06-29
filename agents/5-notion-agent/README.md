# Notion AI Agent

A LinkedIn ghostwriter agent that connects to Notion via MCP (Model Context Protocol) server. This command-line interface allows you to interact with your Notion workspace using natural language through an AI agent powered by GPT-4.

Resources:
- [Video Link](https://youtu.be/lS33W56-NGc)

## Features

- 🤖 **AI-Powered Interaction**: Uses GPT-4.1 to understand and execute Notion operations
- 🔗 **MCP Integration**: Seamless connection to Notion via Model Context Protocol
- 💬 **Interactive CLI**: Real-time streaming conversation interface
- 📝 **LinkedIn Content Creation**: Specialized for ghostwriting and content management
- 🔧 **Configurable Instructions**: Customizable agent behavior via `instructions.md`
- 📊 **OpenAI Tracing**: Built-in tracing for debugging and monitoring

## Prerequisites

- Python 3.12+
- Node.js (for `npx` command)
- Notion API Key
- OpenAI API Key

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd agent-notion
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root:
   ```env
   NOTION_API_KEY=your_notion_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Configuration

### Notion API Setup

1. Go to [Notion Developers](https://www.notion.so/my-integrations)
2. Create a new integration
3. Share your Notion pages/databases with the integration
4. Copy the API key to your `.env` file

### Agent Instructions

Customize the agent's behavior by editing the `instructions.md` file. This file contains the system prompt that defines how the agent should interact with your Notion workspace. Here I've optimized it to write LinkedIn posts in my style as decribed [here](https://youtu.be/ayGdRbMDZcU)

## Usage

### Command Line Interface

Run the interactive agent:

```bash
python notion_agent.py
```

The agent will:
- Connect to your Notion workspace via MCP
- Display available tools and trace URL
- Start an interactive conversation loop
- Stream responses in real-time

### Commands

- Type your requests in natural language
- Use `exit`, `quit`, or `bye` to end the conversation
- Press `Ctrl+C` to interrupt at any time

### Example Interaction

```
=== Notion AI Agent ===
Type 'exit', 'quit', or 'bye' to end the conversation
--------------------------------------------------

User: Create a new page about my latest blog post ideas

Agent: I'll help you create a new page for your blog post ideas...
-- Calling Tool: create_page...
-- Tool call completed.
I've created a new page titled "Blog Post Ideas" in your Notion workspace...
```

### Jupyter Notebook

For development and experimentation, check out the `notion-agent-example.ipynb` notebook.

## Project Structure

```
agent-notion/
├── notion_agent.py           # Main CLI application
├── instructions.md           # Agent system prompt/instructions
├── notion-agent-example.ipynb # Jupyter notebook example
├── requirements.txt          # Python dependencies
├── .env                     # Environment variables (create this)
└── README.md               # This file
```

## Dependencies

Key packages (see `requirements.txt` for complete list):
- `agents` - AI agent framework
- `python-dotenv` - Environment variable management
- `openai` - OpenAI API client
- `asyncio` - Asynchronous programming support

## Features in Detail

### Streaming Responses
The agent provides real-time streaming responses, showing:
- Text output as it's generated
- Tool call notifications
- Completion status updates

### Error Handling
- Graceful handling of API errors
- Keyboard interrupt support
- Missing environment variable validation
- File existence checks

### Conversation Memory
The agent maintains conversation context throughout the session, allowing for follow-up questions and references to previous interactions.
