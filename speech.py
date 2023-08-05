import requests
import openai
from pathlib import Path
from pydub import AudioSegment
from pydub.playback import play
from utils import print_colored
from config import API_KEY, EL_API_KEY


def text_to_speech(text, voice_id):
    url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
    headers = {
        'Accept': 'audio/mpeg',
        'xi-api-key': EL_API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'text': text,
        'model_id': 'eleven_multilingual_v1',
        'voice_settings': {
            'stability': 0.6,
            'similarity_boost': 0.85
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open('output.mp3', 'wb') as f:
            f.write(response.content)
        audio = AudioSegment.from_mp3('output.mp3')
        play(audio)
    else:
        print('Error:', response.text)


def transcribe(audio):
    myfile = Path(audio)
    myfile = myfile.rename(myfile.with_suffix('.wav'))

    with open(myfile, "rb") as file:
        openai.api_key = API_KEY
        result = openai.Audio.transcribe("whisper-1", file, language="es")
    return result['text']
