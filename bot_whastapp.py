from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Importamos tu código original (no lo borramos ni cambiamos)
import tesis
from services.analytics_service import AnalyticsService

app = Flask(__name__)

# Aquí guardamos el estado de cada usuario
user_state = {}
analytics = AnalyticsService()

@app.route("/webhook", methods=["POST"])
def webhook():
    user_number = request.form.get("From")       # Número de WhatsApp del usuario
    incoming_msg = request.form.get("Body").strip()  # Lo que escribe el usuario
    incoming_msg_lower = incoming_msg.lower()
    
    if user_number not in user_state:
        user_state[user_number] = "menu_principal"

    resp = MessagingResponse()
    reply = ""

    # Menú principal (lo mismo que tu while True de tesis.py)
    if user_state[user_number] == "menu_principal":
        if "pensum" in incoming_msg_lower:
            reply = (
                "¿De qué carrera quieres saber el pensum?\n"
                "Opciones: Ing. Sistemas, Ing. Industrial, Ing. Civil, Ing. Eléctrica, Ing. Electromecánica.\n"
                "Escribe el nombre del programa."
            )
            user_state[user_number] = "submenu_pensum"

        elif "matricula" in incoming_msg_lower or "matrícula" in incoming_msg_lower:
            # Aquí llamamos tu función original
            reply = "Información sobre Matrícula 📚"
            # Ejemplo: podrías usar tesis.funcion_matriculas()

        elif "posgrado" in incoming_msg_lower or "posgrados" in incoming_msg_lower:
            reply = "Información sobre Posgrados 🎓"
            # Ejemplo: podrías usar tesis.funcion_posgrados()

        elif "bienestar" in incoming_msg_lower:
            reply = (
                "¿Qué deseas saber de Bienestar?\n"
                "Opciones: Deportes, Área Cultural, Comida.\n"
                "Escribe el tema que deseas consultar."
            )
            user_state[user_number] = "submenu_bienestar"

        else:
            # Bienvenida
            reply = (
                "Bienvenido al Bot 🤖\n"
                "¿Qué deseas consultar? Puedes escribir: pensum, matrícula, posgrado o bienestar."
            )

    # Submenú de pensum
    elif user_state[user_number] == "submenu_pensum":
        if "sistemas" in incoming_msg_lower:
            reply = "Mostrando pensum de Ing. Sistemas..."
        elif "industrial" in incoming_msg_lower:
            reply = "Mostrando pensum de Ing. Industrial..."
        elif "civil" in incoming_msg_lower:
            reply = "Mostrando pensum de Ing. Civil..."
        elif "eléctrica" in incoming_msg_lower or "electrica" in incoming_msg_lower:
            reply = "Mostrando pensum de Ing. Eléctrica..."
        elif "electromecánica" in incoming_msg_lower or "electromecanica" in incoming_msg_lower:
            reply = "Mostrando pensum de Ing. Electromecánica..."
        else:
            reply = "No entendí el programa. ¿De qué carrera quieres saber el pensum?"
            user_state[user_number] = "submenu_pensum"
            resp.message(reply)
            return str(resp)
        user_state[user_number] = "menu_principal"

    # Submenú de bienestar
    elif user_state[user_number] == "submenu_bienestar":
        if "deporte" in incoming_msg_lower:
            reply = "Deportes 🏀"
            # tesis.funcion_deportes()
        elif "cultural" in incoming_msg_lower or "cultura" in incoming_msg_lower:
            reply = "Área Cultural 🎭"
            # tesis.funcion_area_cultural()
        elif "comida" in incoming_msg_lower or "alimentación" in incoming_msg_lower or "alimentacion" in incoming_msg_lower:
            reply = "Comida 🍔"
            # tesis.funcion_comida()
        else:
            reply = "No entendí el tema. Escribe deportes, área cultural o comida."
            user_state[user_number] = "submenu_bienestar"
            resp.message(reply)
            return str(resp)
        user_state[user_number] = "menu_principal"

    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
