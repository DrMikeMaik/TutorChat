import openai
from config import API_KEY, CHATBOT,  VOICE_ID
from speech import text_to_speech

openai.api_key = API_KEY


class Chatbot:
    def __init__(self):
        self.conversation = []

    def generate_response(self, user_input, temperature=0.9, frequency_penalty=0.2, presence_penalty=0):
        self.conversation.append({"role": "user", "content": user_input})
        messages_input = self.conversation.copy()
        prompt = [{"role": "system", "content": CHATBOT}]
        messages_input.insert(0, prompt[0])
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            temperature=temperature,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            messages=messages_input)
        chat_response = completion['choices'][0]['message']['content']
        text_to_speech(chat_response, VOICE_ID)
        self.conversation.append({"role": "assistant", "content": chat_response})
        return chat_response

    def clear_history(self):
        self.conversation = []
