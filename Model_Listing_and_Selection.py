from openai import OpenAI
import os

# This function should no longer ask for user input.
# It should retrieve the API key from an environment variable.
def list_and_select_gpt_model():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("API key is required to authenticate with OpenAI.")
        exit(1)  # Exit with an error code if the API key is not found

    # Instantiate the OpenAI client with your API key
    client = OpenAI(api_key=api_key)

    try:
        # Use the client to list models
        models_response = client.models.list()
        models = models_response.data

        print("Available GPT models:")
        for index, model in enumerate(models):
            print(f"{index}: {model.id}")  # Access attributes directly

        # Since we can't interactively select a model in GitHub Actions, you might want to select a default or use an environment variable for the model.
        selected_model_index = int(os.getenv('SELECTED_MODEL_INDEX', '27'))  # Default to the first model if not specified
        selected_model = models[selected_model_index].id  # Access attributes directly
        print(f"You have selected: {selected_model}")
        return selected_model

    except Exception as e:
        print(f"An error occurred while listing models: {e}")

if __name__ == "__main__":
    list_and_select_gpt_model()
