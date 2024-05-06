import requests

class OpenTTSClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def speak_text(self, voice, text, cache=True):
        url = f"{self.base_url}/api/tts"
        params = {
            'voice': voice,
            'text': text,
            'cache': cache
        }
        response = requests.get(url, params=params)
        return response.content

# Initialize the OpenTTS client with the base URL of the OpenTTS API
open_tts_client = OpenTTSClient(base_url='http://localhost:5500')

# Define a function to run TTS from the command line
def run_tts():
    # Prompt the user to enter the voice and text
    voice = input("Enter the voice (e.g., espeak:en): ")
    text = input("Enter the text to convert to speech: ")

    # Call the speak_text method from the OpenTTS client to convert text to speech
    audio_data = open_tts_client.speak_text(voice=voice, text=text)

    # Save the audio data to a WAV file
    with open("output.wav", "wb") as f:
        f.write(audio_data)

# Run the TTS function
if __name__ == "__main__":
    run_tts()
