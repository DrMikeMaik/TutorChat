# TutorChat README

## Description

A language conversation assistant is a tool that allows users to interact with a language model. 
Users can not only chat with the assistant but also record their voice, 
which will be transcribed and processed by the assistant to generate responses. 
Moreover, the program leverages a text-to-speech service to audibly read out the responses.

## Features

- Interaction with OpenAI's GPT language models.
- Real-time voice recording and transcription.
- Text-to-speech functionality to audibly present responses.
- Gradio interface for ease of use

## Requirements

- Python 3.9 or higher.
- Python Libraries:
  - `numpy`
  - `gradio`
  - `openai`
  - `requests`
  - `pydub`

## Installation

1. Clone this repository.
2. Install the required packages with `pip install -r requirements.txt`

## Configuration

1. Place your OpenAI API key in a file named `openaiapikey2.txt`.
2. Place your Elevenlabs API key (for the text-to-speech feature) in a file named `elabapikey.txt`.
3. (Optional) Modify `chatbot_{language}.txt` files if you wish to customize the initial behavior of the chatbot.

## Usage

1. Run the script with `python <script_name>.py`.
2. Once executed, the Gradio interface will be accessible via your local browser at: http://127.0.0.1:7860/
3. A Gradio interface will pop up, presenting a user-friendly way to interact with the chatbot.
4. Choose your preferred language for the conversation.
5. Select a response voice from the available options.
6. Start your interaction by pressing the **"Move to Chat button"**
7. Record your voice by using the **"Record from microphone"** button and send it to the chatbot with **"Send Audio"**
8. The chatbot will respond both in text and audibly using the selected voice type.
9. To end the session, simply close the Gradio interface.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a Pull Request.

## License

This project is under the MIT License. Please refer to the LICENSE file for more details.

---