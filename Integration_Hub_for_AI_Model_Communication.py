import os
import openai

def generate_speech_from_text(api_key, text, model="tts-1-hd", voice="alloy"):
    """
    Generate spoken audio from text using OpenAI's Text-to-Speech API.
    :param api_key: Your OpenAI API key.
    :param text: The text to convert to speech.
    :param model: The TTS model to use. Defaults to "tts-1-hd" for high quality.
    :param voice: The voice to use for the audio. Defaults to "alloy".
    """
    openai.api_key = api_key
    try:
        response = openai.Audio.create(
            model=model,
            input=text,
            voice=voice,
            response_format="mp3"
        )
        # Assuming the response contains a URL to the generated audio file
        audio_url = response['data']['url']
        print(f"Generated audio URL: {audio_url}")
    except Exception as e:
        print(f"An error occurred while generating speech: {e}")

if __name__ == "__main__":
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("API key is required to authenticate with OpenAI.")
        exit(1)
    
    # Example text to convert to speech
    text_to_speech = "This is a sample text to convert into spoken audio using OpenAI's Text-to-Speech API."
    
    generate_speech_from_text(api_key, text_to_speech)

