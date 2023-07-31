from chatbot import Chatbot
from speech import text_to_speech, record_and_transcribe
from utils import print_colored
from config import INTRO, VOICE_ID

print_colored("", f"{INTRO}\n\n", 'intro')
print("Pulsar 'Enter' para comenzar")
input()
chatbot = Chatbot()

while True:
    user_message = record_and_transcribe()
    response = chatbot.generate_response(user_message)
    print_colored("Julie:", f"{response}\n\n", 'agent')

    text_to_speech(response, VOICE_ID)
    print("Pulsar 'Enter' para continuar")
    input()
