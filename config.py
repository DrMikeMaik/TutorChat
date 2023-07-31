def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


API_KEY = open_file('openaiapikey.txt')
EL_API_KEY = open_file('elabapikey.txt')
VOICE_ID = '21m00Tcm4TlvDq8ikWAM'
INTRO = """Bienvenido, soy tu Asistente de Conversaciones en Español. 
Aquí para ayudarte a mejorar, a aprender, y a divertirte con el idioma. 
¡Vamos a disfrutar de nuestro viaje lingüístico juntos!

¿Sobre qué te gustaría hablar hoy?
"""
CHATBOT = open_file('./chatbot_languages/chatbot_es.txt')
