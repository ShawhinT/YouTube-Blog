# LLM Workflows
Second example in AI agents series. Here, I use OpenAI's Agents SDK to create AVA, an artificial virtual assistant that can write emails for me.

**Links**
- [Video](https://youtu.be/Nm_mmRTpWLg)
- [Blog](https://shawhin.medium.com/llm-workflows-from-automation-to-ai-agents-a62f96a0f89a)

## How to run this example

1. Clone this repo
2. Navigate to downloaded folder and create new venv
```
python -m venv ava-env
```
3. Activate venv
```
# mac/linux
source ava-env/bin/activate

# windows
.\ava-env\Scripts\activate.bat
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Follow set-up instructions below
6. Run script
```
python ava.py
```

## Customizing AVA's Behavior

### Update Personal Details and Preferences
1. Locate the `instructions/ava.md` file in your project directory
2. Customize the file with:
   - Your personal details (name, role, etc.)
   - Communication preferences
   - Specific instructions for handling tasks
   - Any other relevant guidelines for AVA

## Environment Setup (.env)

1. Create a `.env` file in the root directory of the project with the following variables:

```env
OPENAI_API_KEY=your_openai_api_key_here
USER_EMAIL=your_email_address

# Google OAuth Credentials
GOOGLE_CREDENTIALS_PATH=.config/ava-agent/credentials.json
GOOGLE_TOKEN_PATH=.config/ava-agent/token.json
```

### Required Environment Variables:
- `OPENAI_API_KEY`: Your OpenAI API key for accessing GPT models
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

## First Run

When you first run the application, it will:
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
- Keep your OpenAI API key and Google credentials secure
- Add the following to your `.gitignore`:
  ```
  .env
  .config/ava-agent/token.json
  .config/ava-agent/credentials.json
  ``` 
