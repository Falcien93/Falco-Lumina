try:
    import openai
except ImportError:
    print("The 'openai' module is not installed. Please install it using 'pip install openai'.")
    exit()

def authenticate_with_openai():
    api_key = input("Please enter your OpenAI API key: ").strip()
    if api_key:
        print("Authentication successful.")
    else:
        print("API key is required to authenticate with OpenAI.")
        exit()

if __name__ == "__main__":
    authenticate_with_openai()
