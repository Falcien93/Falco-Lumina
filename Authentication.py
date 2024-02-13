import os
import openai

def authenticate_with_openai():
    # Get the API key from the environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if api_key:
        openai.api_key = api_key
        print("Authentication successful.")
    else:
        print("API key is required to authenticate with OpenAI.")
        exit(1)  # Exit with an error code

if __name__ == "__main__":
    authenticate_with_openai()
