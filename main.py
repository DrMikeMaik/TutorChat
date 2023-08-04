import gradio as gr
from chatbot import Chatbot
from speech import transcribe
from utils import print_colored
from config import INTRO

print_colored("", f"{INTRO}\n\n", 'intro')
print("Pulsar 'Enter' para comenzar")
input()

chatbot = Chatbot()


def interact(audio, state=""):
    state = transcribe(audio, state)
    state = chatbot.generate_response(state)
    return state, state


gr.Interface(
    fn=interact,
    inputs=[
        gr.Audio(source="microphone", type="filepath", streaming=False),
        "state"
    ],
    outputs=[
        "textbox",
        "state"
    ],
    live=False
).launch(debug=True)
