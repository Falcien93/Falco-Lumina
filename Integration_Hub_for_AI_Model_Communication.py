import json
import requests
import os

# Function to execute a prompt with the GPT model
def execute_gpt_model_prompt(api_key, model_name, prompt):
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "model": model_name,
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=payload)
    return response.json()['choices'][0]['text']

# Function to execute a prompt with the TTS model
def execute_tts_model_prompt(api_key, text):
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {
        "text": text,
    }
    # Assuming the TTS endpoint is similar to this (please adjust according to the actual API documentation)
    response = requests.post("https://api.openai.com/v1/tts", headers=headers, json=payload)
    return response.json()['audio_url']

# Main function to handle integration
def handle_integration(api_key, primary_model, secondary_model):
    primary_prompt = "Your primary model prompt here"
    primary_response = execute_gpt_model_prompt(api_key, primary_model, primary_prompt)
    print("Primary Model Response:", primary_response)

    # Assuming the primary response is suitable as input to the TTS model
    tts_audio_url = execute_tts_model_prompt(api_key, primary_response)
    print("TTS Audio URL:", tts_audio_url)

if __name__ == "__main__":
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("API key is required to authenticate with OpenAI.")
        exit(1)

    primary_model = "gpt-4-0125-preview"  # Example GPT model
    secondary_model = "tts-1-hd"  # Placeholder for the TTS model name

    handle_integration(api_key, primary_model, secondary_model)
