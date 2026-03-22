# Script para probar el flujo del bot sin Twilio/WhatsApp
# Simula la interacción por consola

import os
from session_manager import SessionManager
from menu_handler import MenuHandler

def test_bot():
    print("--- INICIANDO TEST LOCAL DEL BOT ---")
    session_manager = SessionManager(filename='test_sessions.json')
    handler = MenuHandler(session_manager)
    
    numero_test = "whatsapp:+123456789"
    
    # Reset inicial
    session_manager.reset_session(numero_test)
    
    while True:
        print("\n" + "-"*30)
        session = session_manager.get_session(numero_test)
        print(f"[Estado: {session['estado']}]")
        
        user_input = input("Tú: ")
        if user_input.lower() in ['salir', 'exit', 'quit']:
            break
            
        # Procesar
        respuesta, imagen = handler.process_message(numero_test, user_input)
        
        print(f"\nBot: {respuesta}")
        if imagen:
            print(f"[IMAGEN]: {imagen}")

if __name__ == "__main__":
    # Limpiar archivo de test si existe
    if os.path.exists('test_sessions.json'):
        os.remove('test_sessions.json')
        
    test_bot()
