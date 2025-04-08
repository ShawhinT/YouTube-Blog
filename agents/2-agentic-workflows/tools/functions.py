# Functions for AVA system

from openai.types.responses import ResponseTextDeltaEvent

async def handle_stream_events(result):
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            # # raw text generations of model
            # print(event.data.delta, end="", flush=True)
            pass
        elif event.type == "agent_updated_stream_event":
            print("-- Agent Updated.")
            print(event.new_agent.name)
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                print("-- Tool Called.")
                print(f"Tool name: {event.item.raw_item.name}")
                print(f"Arguments: {event.item.raw_item.arguments}")
            elif event.item.type == "tool_call_output_item":
                # # raw tool call outputs
                # print("-- Tool Output:")
                # print(event.item.output)
                pass
            elif event.item.type == "message_output_item":
                pass
            else:
                pass  # Ignore other event types

def read_instructions(file_name: str) -> str:
    """Read and return the contents of a file.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The complete contents of the file as a string.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there are issues reading the file.
    """
    with open(f"instructions/{file_name}", "r") as file:
        return file.read()