from mcp.server.fastmcp import FastMCP
import csv
from tools.gmail import get_gmail_service
from googleapiclient.errors import HttpError
import base64
from email.message import EmailMessage
import os

# Create an MCP server
mcp = FastMCP("AVA")

# Define prompts
@mcp.prompt()
def ava(user_name: str, user_title: str) -> str:
    """Global instructions for Artificial Virutal Assistant (AVA)"""
    with open("prompts/ava.md", "r") as file:
        template = file.read()
    return template.format(user_name=user_name, user_title=user_title)

# Define resources
@mcp.resource("email-examples://3-way-intro")
def write_3way_intro() -> str:
    """Example of a 3-way intro email"""
    with open("email-examples/3-way-intro.md", "r") as file:
        return file.read()

@mcp.resource("email-examples://call-follow-up")
def write_call_followup() -> str:
    """Example of a call follow-up email"""
    with open("email-examples/call-follow-up.md", "r") as file:
        return file.read()

@mcp.resource("directory://all")
def get_directory() -> str:
    """Get the entire directory of contacts"""
    with open("directory.csv", "r") as file:
        return file.read()

# Define tools
@mcp.tool()
def write_email_draft(recipient_email: str, subject: str, body: str) -> dict:
    """Create a draft email using the Gmail API.
    
    Args:
        recipient_email (str): The email address of the recipient.
        subject (str): The subject line of the email.
        body (str): The main content/body of the email.
    
    Returns:
        dict or None: A dictionary containing the draft information including 'id' and 'message' 
                     if successful, None if an error occurs.
    
    Raises:
        HttpError: If there is an error communicating with the Gmail API.
        
    Note:
        This function requires:
        - Gmail API credentials to be properly configured
        - USER_EMAIL environment variable to be set with the sender's email address
        - Appropriate Gmail API permissions for creating drafts
    """
    try:
        # create gmail api client
        service = get_gmail_service()

        message = EmailMessage()

        message.set_content(body)

        message["To"] = recipient_email
        message["From"] = os.getenv("USER_EMAIL")
        message["Subject"] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"message": {"raw": encoded_message}}
        # pylint: disable=E1101
        draft = (
            service.users()
            .drafts()
            .create(userId="me", body=create_message)
            .execute()
        )

        print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

    except HttpError as error:
        print(f"An error occurred: {error}")
        draft = None

    return draft


if __name__ == "__main__":
    mcp.run(transport='stdio')