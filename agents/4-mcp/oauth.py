from tools.gmail import *
import os

# check if token.json exists and initialize Gmail service if needed
if not os.path.exists(os.getenv("GOOGLE_TOKEN_PATH")):
    print("--- Token not found, starting authentication process ---")
    try:
        get_gmail_service()  # This will automatically handle the auth flow
        print("--- Authentication successful ---")
    except Exception as e:
        print(f"--- Authentication failed: {str(e)} ---")
        exit(1)