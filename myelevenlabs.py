import os
from elevenlabs.client import ElevenLabs
from elevenlabs import play as elevenlabs_play

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class ElevenLabsSpeech:
    def __init__(self):
        self.api_key = os.environ.get('ELEVENLABS_API_KEY')
        if not self.api_key:
            raise ValueError("ELEVENLABS_API_KEY environment variable is not set")
        
        self.client = ElevenLabs(api_key=self.api_key)
        self.default_voice_id = 'pzphoxknYixivi1H6DII'  # Default voice ID from your reference code

    def say(self, text, voice_id=None):
        """
        Synthesize and play speech from the given text.

        Args:
            text (str): The text to be spoken.
            voice_id (str, optional): The ID of the voice to use. If None, uses the default voice.
        """
        try:
            audio = self.client.generate(
                text=text,
                voice=voice_id or self.default_voice_id,
                model="eleven_multilingual_v2"
            )
            
            elevenlabs_play(audio)
        except Exception as e:
            print(f"Error synthesizing or playing speech: {str(e)}")

# Example usage
if __name__ == "__main__":
    speech = ElevenLabsSpeech()
    speech.say("Hello, this is a test of the ElevenLabs speech synthesis.")
    
    # To use a specific voice, you can do:
    # speech.say("This is another test with a different voice.", voice_id="your_voice_id_here")

