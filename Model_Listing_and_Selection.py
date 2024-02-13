import os
from openai import OpenAI

def list_and_select_gpt_model():
    # Get the API key from an environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("API key is required to authenticate with OpenAI.")
        exit(1)  # Exit with an error code if the API key is not found
    
    # Authenticate with the API key
    openai.api_key = api_key

def list_and_select_gpt_model(api_key):
    """
    Lists available GPT models and prompts the user to select one using the updated OpenAI API interface.
    """
    # Instantiate the OpenAI client with your API key
    client = OpenAI(api_key=api_key)

    try:
        # Use the client to list models
        models_response = client.models.list()
        models = models_response.data
        
        print("Available GPT models:")
        for index, model in enumerate(models):
            print(f"{index}: {model.id}")  # Note: Access attributes directly
        
        selection = int(input("Enter the number of the GPT model you wish to use: "))
        selected_model = models[selection].id  # Access attributes directly
        print(f"You have selected: {selected_model}")
        return selected_model
    except Exception as e:
        print(f"An error occurred while listing models: {e}")

if __name__ == "__main__":
    list_and_select_gpt_model()
