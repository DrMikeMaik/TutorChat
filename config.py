from utils import open_file

API_KEY = open_file('openaiapikey.txt')
EL_API_KEY = open_file('elabapikey.txt')
VOICE_ID = {
    'Rachel': '21m00Tcm4TlvDq8ikWAM',
    'Dave': 'CYw3kZ02Hs0563khs1Fj',
    'Charlie': 'IKne3meq5aSn9XLyUdCD',
    'Elli': 'MF3mGyEYCl7XYWbV9V6O'
}

CHATBOT = {
    'Spanish': {'text': './chatbot_languages/chatbot_es.txt', 'lang': 'es'},
    'French': {'text': './chatbot_languages/chatbot_fr.txt', 'lang': 'fr'},
    'German': {'text': './chatbot_languages/chatbot_de.txt', 'lang': 'de'},
    'Polish': {'text': './chatbot_languages/chatbot_pl.txt', 'lang': 'pl'}
}
