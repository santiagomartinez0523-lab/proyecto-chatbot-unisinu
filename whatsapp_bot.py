# whatsapp_bot.py
# Archivo de ejecución del bot en servidor (Flask + Twilio)

import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

# Importar lógica del bot
from session_manager import SessionManager
from menu_handler import MenuHandler

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de Twilio (desde variables de entorno)
# TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
# TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
# TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

# Inicializar gestores
# Usaremos un archivo JSON para persistir sesiones si el servidor se reinicia
session_manager = SessionManager(filename='sessions.json')
menu_handler = MenuHandler(session_manager)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    """Endpoint principal que recibe mensajes desde Twilio (WhatsApp)"""
    # 1. Obtener datos del mensaje entrante
    incoming_msg = request.values.get('Body', '').strip()
    sender_phone = request.values.get('From', '')

    print(f"\n📩 Mensaje recibido de {sender_phone}: '{incoming_msg}'")

    # 2. Procesar el mensaje a través del MenuHandler
    response_text, image_url = menu_handler.process_message(sender_phone, incoming_msg)

    # 3. Construir la respuesta TwiML (formato de Twilio)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(response_text)
    
    # Si hay una imagen asociada al estado actual, adjuntarla
    if image_url:
        msg.media(image_url)
        print(f"🖼️ Adjuntando imagen: {image_url}")

    return str(resp)

@app.route('/', methods=['GET'])
def index():
    """Mensaje de bienvenida en el servidor"""
    return "🚀 Servidor del ChatBot Universitario (UniSinú) funcionando correctamente."

# Para ejecutar localmente con ngrok:
# 1. Ejecutar ngrok: ngrok http 5000
# 2. Copiar la URL de ngrok (https://...)
# 3. Pegar en Twilio Console Sandbox: https://[URL-NGROK]/whatsapp

if __name__ == '__main__':
    # Obtener puerto de variable de entorno (para despliegue en la nube)
    port = int(os.environ.get('PORT', 5000))
    # En desarrollo local usaremos el puerto 5000
    app.run(host='0.0.0.0', port=port, debug=True)
