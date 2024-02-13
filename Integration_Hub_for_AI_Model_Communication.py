import json
import requests
import os

def execute_model_prompt(api_key, model_name, prompt):
    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": model_name, "prompt": prompt, "max_tokens": 50}
    )
    return response.json()

def integrate_model_responses(primary_response, secondary_responses):
    combined_insight = f"{primary_response}\n\n{' '.join(secondary_responses)}"
    return combined_insight

def handle_integration(api_key, primary_model, secondary_models):
    primary_response = execute_model_prompt(api_key, primary_model, "Primary model prompt")
    secondary_responses = [
        execute_model_prompt(api_key, model, "Secondary model prompt")['choices'][0]['text']
        for model in secondary_models
    ]
    final_response = integrate_model_responses(primary_response['choices'][0]['text'], secondary_responses)
    print("Integrated Model Response:", final_response)

if __name__ == "__main__":
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("API key is required to authenticate with OpenAI.")
        exit(1)

    # Example models to integrate. These should be set up according to your needs.
    primary_model = "gpt-4-0125-preview"
    secondary_models = ["tts-1-hd"]

    handle_integration(api_key, primary_model, secondary_models)
