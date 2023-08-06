import gradio as gr
from chatbot import Chatbot
from speech import transcribe
from utils import print_colored
from config import INTRO

print_colored("", f"{INTRO}\n\n", 'intro')
print("Pulsar 'Enter' para comenzar")
input()

chatbot = Chatbot()


def interact(audio, chat_history):
    user_message = transcribe(audio)
    chat_response = chatbot.generate_response(user_message)
    chat_history.append((user_message, chat_response))
    return None, chat_history


def respond(message, chat_history):
    bot_message = "I love you"
    chat_history.append((message, bot_message))
    return "", chat_history


with gr.Blocks() as demo:
    gradio_chatbot = gr.Chatbot()
    clear = gr.Button("Clear History")

    with gr.Row():
        voice = gr.Audio(source="microphone", type="filepath", streaming=False)

        send_voice_button = gr.Button("Send Audio", interactive=True)
        send_voice_button.click(interact, inputs=[voice, gradio_chatbot], outputs=[voice, gradio_chatbot])

    clear.click(lambda: None, None, gradio_chatbot, queue=False).then(chatbot.clear_history, None, None, queue=False)


demo.launch(debug=True)
