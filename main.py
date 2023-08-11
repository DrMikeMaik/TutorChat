import gradio as gr
from chatbot import Chatbot
from speech import transcribe

chatbot = Chatbot()


def interact(audio, chat_history, language, character_voice):
    if audio is not None:
        user_message = transcribe(audio, language)
        chatbot.init_voice_and_language(language, character_voice)
        chat_response = chatbot.generate_response(user_message)
        chat_history.append((user_message, chat_response))
        return None, chat_history
    else:
        return None, chat_history


def change_tab():
    return gr.Tabs.update(selected=1)


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # <div style="text-align:center">Welcome to TutorChat!</div>
        Choose your parameters and let's get started!
        """
        )
    with gr.Tabs() as tabs:
        with gr.TabItem("Configure your language preferences", id=0):
            gr.Markdown(
                """
                # Choose your parameters.
                """
            )
            language_choice = gr.Dropdown(["Spanish", "French", "German"],
                                          type="value", value="French", label="Choose a language")

            voice_choice = gr.Dropdown(["Rachel", "Dave", "Charlie", "Elli"],
                                       type="value", value="Elli", label="Choose a speaker")

            # level_choice = gr.Dropdown(["A1", "A2", "B1", "B2", "C1", "C2"],
            #                            type="value", value="A2", label="Choose a level")

        with gr.TabItem("Chat", id=1):

            gr.Markdown(
                """
                Let's chat!
                """
            )

            gradio_chatbot = gr.Chatbot()
            clear = gr.Button("Clear History")

            with gr.Row():
                voice = gr.Audio(source="microphone", type="filepath", streaming=False)

                send_voice_button = gr.Button("Send Audio", interactive=True)
                send_voice_button.click(interact,
                                        inputs=[voice, gradio_chatbot, language_choice, voice_choice],
                                        outputs=[voice, gradio_chatbot]
                                        )

            clear.click(lambda: None, None, gradio_chatbot).then(chatbot.clear_history, None, None)

    btn = gr.Button("Move to Chat")
    btn.click(change_tab, None, tabs)


demo.launch(debug=True)
