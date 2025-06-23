#!/usr/bin/env python3
"""
Notion AI Agent - Command Line Interface
A LinkedIn ghostwriter agent that connects to Notion via MCP server.

Code authored by: Shaw Talebi
"""

import os
import asyncio
from dotenv import load_dotenv
from agents.mcp.server import MCPServerStdio, MCPServer
from agents import Agent, Runner, gen_trace_id, trace, ModelSettings
from openai.types.responses import ResponseTextDeltaEvent


def load_environment():
    """Load environment variables and validate required keys."""
    load_dotenv()
    
    notion_key = os.getenv("NOTION_API_KEY")
    if not notion_key:
        raise ValueError(
            "NOTION_API_KEY environment variable is required. "
            "Please add it to your .env file or set it as an environment variable."
        )
    
    return notion_key


def load_instructions():
    """Load agent instructions from instructions.md file."""
    try:
        with open('instructions.md', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            "instructions.md file not found. Please ensure it exists in the current directory."
        )


async def create_mcp_server(notion_key: str) -> MCPServerStdio:
    """Create and return an MCP server connection for Notion."""
    return MCPServerStdio(
        params={
            "command": "npx",
            "args": ["-y", "@notionhq/notion-mcp-server"],
            "env": {
                "OPENAPI_MCP_HEADERS": f'{{"Authorization": "Bearer {notion_key}", "Notion-Version": "2022-06-28"}}'
            }
        }
    )


async def run_agent_conversation(mcp_server: MCPServer, instructions: str):
    """Run the main conversation loop with the Notion AI agent."""
    # Create the agent
    agent = Agent(
        name="Notion Agent",
        model="gpt-4.1-2025-04-14",
        instructions=instructions,
        mcp_servers=[mcp_server],
    )
    ModelSettings.tool_choice = "required"
    
    # Store conversation history
    input_items = []

    print("=== Notion AI Agent ===")
    print("Type 'exit', 'quit', or 'bye' to end the conversation")
    print("-" * 50)

    while True:
        # Get user input
        try:
            user_input = input("\nUser: ").strip()
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        
        # Add user input to conversation history
        input_items.append({"content": user_input, "role": "user"})
        
        # Check for exit commands
        if user_input.lower() in ['exit', 'quit', 'bye', '']:
            print("\nGoodbye!")
            break
            
        if not user_input:
            continue

        print("\nAgent: ", end="", flush=True)
        
        try:
            # Run the agent with streaming
            result = Runner.run_streamed(
                agent,
                input=input_items,
            )
            
            # Process streaming events
            async for event in result.stream_events():
                if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                    # Print text deltas as they come in
                    print(event.data.delta, end="", flush=True)
                elif event.type == "run_item_stream_event":
                    if event.item.type == "tool_call_item":
                        print(f"\n-- Calling Tool: {event.item.raw_item.name}...")
                    elif event.item.type == "tool_call_output_item":
                        print("-- Tool call completed.")
                    elif event.item.type == "message_output_item":
                        # Add assistant response to conversation history
                        input_items.append({
                            "content": f"{event.item.raw_item.content[0].text}", 
                            "role": "assistant"
                        })

            print("\n")  # Add newline after response
            
        except Exception as e:
            print(f"\nError occurred: {e}")
            print("Please try again or type 'exit' to quit.")


async def main():
    """Main entry point for the Notion AI agent."""
    try:
        # Load environment and instructions
        notion_key = load_environment()
        instructions = load_instructions()
        
        # Create MCP server connection
        async with await create_mcp_server(notion_key) as server:
            # Generate trace ID for OpenAI tracing
            trace_id = gen_trace_id()
            with trace(workflow_name="Notion Agent CLI", trace_id=trace_id):
                print(f"Trace URL: https://platform.openai.com/traces/trace?trace_id={trace_id}")
                
                # List available tools (for debugging)
                tools = await server.list_tools()
                print(f"Connected to Notion MCP server with {len(tools)} tools available")
                
                # Run the conversation loop
                await run_agent_conversation(server, instructions)
                
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    try:
        exit_code = asyncio.run(main())
        exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
        exit(0)
