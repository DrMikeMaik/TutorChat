import requests
import openai
import queue
import sounddevice as sd
import soundfile as sf
import numpy as np
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


def record_and_transcribe(fs=44100):
    print('Recording...')

    # Define a callback function to be called by SoundDevice
    def callback(indata, frames, time, status):
        vol_norm = np.linalg.norm(indata) * 10
        # print('Recording volume:', vol_norm)
        q.put(indata.copy())

    # Create a queue to hold the recorded chunks
    q = queue.Queue()

    # Create a stream to record audio
    stream = sd.InputStream(callback=callback, channels=1, samplerate=fs)
    with stream:
        # Wait for a keyboard interrupt to stop recording
        print('Press Ctrl+C to stop recording')
        try:
            while True:
                pass
        except KeyboardInterrupt:
            print('Recording complete.')

    # Process the recorded chunks
    myrecording = []
    while not q.empty():
        myrecording.extend(q.get())
    myrecording = np.array(myrecording)
    filename = 'myrecording.wav'
    sf.write(filename, myrecording, fs)

    with open(filename, "rb") as file:
        openai.api_key = API_KEY
        result = openai.Audio.transcribe("whisper-1", file, language="es")
    transcription = result['text']
    print_colored("You:", f"{transcription}\n\n", 'user')
    return transcription
