# Main script for AVA (Artificial Virtual Assistant)

# imports
from tools.functions import *
from tools.for_agents import *
from tools.gmail import *

from pydantic import BaseModel
from agents import Agent, Runner, ModelSettings
from dotenv import load_dotenv
import asyncio

# import environment variables from .env file
load_dotenv()

# Planner Agent
class PlannerOutput(BaseModel):
    exec_required: bool
    exec_inst: str
    user_note: str

planner_instructions = read_instructions("ava.md") + read_instructions("planner.md")
planner_agent = Agent(
    name="Planner Agent",
    instructions=planner_instructions,
    tools=[read_dir_struct, read_file_contents],
    model_settings=ModelSettings(temperature=0.5),
    output_type=PlannerOutput,
)

# Executor Agent
executor_instructions = read_instructions("ava.md") + read_instructions("executor.md")
executor_agent = Agent(
    name="Executor Agent",
    instructions=executor_instructions,
    tools=[read_dir_struct, read_file_contents, write_email_draft, overwrite_existing_file],
    model_settings=ModelSettings(temperature=0),
)

async def main():
    # check if token.json exists and initialize Gmail service if needed
    if not os.path.exists(os.getenv("GOOGLE_TOKEN_PATH")):
        print("--- Token not found, starting authentication process ---")
        try:
            get_gmail_service()  # This will automatically handle the auth flow
            print("--- Authentication successful ---")
        except Exception as e:
            print(f"--- Authentication failed: {str(e)} ---")
            return

    # read request from request.txt
    with open("request.txt", "r") as file:
        request = file.read()

    # run planner agent
    result = Runner.run_streamed(
        planner_agent, 
        request,
    )

    # handle stream events
    print("--- Analyzing ---")
    await handle_stream_events(result)

    # print planner agent's output
    print()
    print("--- Planner Agent Output ---")
    print(result.final_output.user_note)
    print()

    # check if execution is required
    if result.final_output.exec_required:
        result = Runner.run_streamed(
            executor_agent,
            result.final_output.exec_inst
        )
    
        print("--- Executing ---")
        await handle_stream_events(result)

        print()
        print("--- Executor Agent Output ---")
        print(result.final_output)
        print()
    

if __name__ == "__main__":
    asyncio.run(main())