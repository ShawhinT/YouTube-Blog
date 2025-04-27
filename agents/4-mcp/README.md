# Model Context Protocol (MCP)
Fourth example in AI agents series. Here, I build a customer MCP server to give any AI app access to a toolset for an Artificial Virtual Assistant (AVA).

**Links**
- [Video](https://youtu.be/N3vHJcHBS-w)
- [Blog](https://medium.com/data-science-collective/model-context-protocol-mcp-explained-ef5c33c5fe05)

## How to run this example

1. Clone this repo
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already
```
# Mac/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
3. Test the server in dev mode
```
uv run mcp dev mcp-server-example.py
```
4. Add server config to AI app (e.g. Claude Desktop or Cursor).
```
{
  "mcpServers": {
    "AVA": {
      "command": "/Users/shawhin/.local/bin/uv", # replace with global path to your uv installation
      "args": [
        "--directory",
        "/Users/shawhin/Documents/_code/_stv/sandbox/ava-mcp/", # replace with global path to repo
        "run",
        "mcp-server-example.py"
      ]
    }
  }
}
```


## Customizing AVA's Behavior

### Update Personal Details and Preferences
1. Locate the `prompts/ava.md` file in your project directory
2. Customize the file with:
   - Communication preferences
   - Specific instructions for handling tasks
   - Any other relevant guidelines for AVA

## Environment Setup (.env)

1. Create a `.env` file in the root directory of the project with the following variables:

```env
USER_EMAIL=your_email_address

# Google OAuth Credentials
GOOGLE_CREDENTIALS_PATH=.config/ava-agent/credentials.json
GOOGLE_TOKEN_PATH=.config/ava-agent/token.json
```

### Required Environment Variables:
- `USER_EMAIL`: The Gmail address you want to use for this application
- `GOOGLE_CREDENTIALS_PATH`: Path to your Google OAuth credentials file
- `GOOGLE_TOKEN_PATH`: Path where the Google OAuth token will be stored

## Google OAuth Setup

### 1. Create Project Directory Structure

First, create the required directory structure:
```bash
mkdir -p .config/ava-agent
```

### 2. Set Up Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API:
   - In the navigation menu, go to "APIs & Services" > "Library"
   - Search for "Gmail API"
   - Click "Enable"

### 3. Create OAuth Credentials

1. In the Google Cloud Console:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop application" as the application type
   - Give it a name (e.g., "AVA Gmail Client")
   - Click "Create"

2. Download the credentials:
   - After creation, click "Download JSON"
   - Save the downloaded file as `credentials.json` in `.config/ava-agent/`
   - The file should contain your client ID and client secret

### 4. Configure OAuth Consent Screen

1. In the Google Cloud Console:
   - Go to "APIs & Services" > "OAuth consent screen"
   - Choose "External" user type
   - Fill in the required information:
     - App name
     - User support email
     - Developer contact information
   - Add the Gmail API scope: `https://www.googleapis.com/auth/gmail.modify`
   - Add your email as a test user
   - Complete the configuration

## Signing into Google

Before the server can access you Gmail account you will need to authorize it. You can do this by running `uv run oauth.py` which does the following.
1. Check for the presence of `token.json`
2. If not found, it will initiate the Google OAuth authentication flow
3. Guide you through the authentication process in your browser:
   - You'll be asked to sign in to your Google account
   - Grant the requested permissions
   - The application will automatically save the token
4. Generate and store the token automatically

## Security Notes

### File Protection
- Never commit your `.env` file or `token.json` to version control
- Keep your Google credentials secure
- Add the following to your `.gitignore`:
  ```
  .env
  .config/ava-agent/token.json
  .config/ava-agent/credentials.json
  ``` 
