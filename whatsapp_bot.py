import os
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

from session_manager import SessionManager
from menu_handler import MenuHandler

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Inicializar componentes
session_manager = SessionManager()
menu_handler = MenuHandler(session_manager)

@app.route('/whatsapp', methods=['POST'])
def whatsapp_webhook():
    """Webhook para recibir mensajes de WhatsApp a través de Twilio"""
    # Obtener el mensaje y el número del remitente
    incoming_msg = request.values.get('Body', '').lower().strip()
    from_number = request.values.get('From', '')
    
    # Procesar el mensaje
    response_text, image_url = menu_handler.process_message(from_number, incoming_msg)
    
    # Crear respuesta de Twilio
    resp = MessagingResponse()
    msg = resp.message(response_text)
    
    # Agregar imagen si existe
    if image_url:
        msg.media(image_url)
        
    return str(resp)

@app.route('/test', methods=['GET'])
def test():
    """Endpoint de prueba"""
    return jsonify({
        "status": "online",
        "message": "Chatbot University Service is running"
    })

@app.route('/sessions', methods=['GET'])
def view_sessions():
    """Ver sesiones activas (solo para desarrollo/debug)"""
    return jsonify(session_manager.get_all_sessions())

if __name__ == '__main__':
    # Obtener puerto de la variable de entorno o usar 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    # Ejecutar la aplicación
    app.run(host='0.0.0.0', port=port, debug=True)
