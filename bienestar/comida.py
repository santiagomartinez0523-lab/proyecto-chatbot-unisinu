from programas.numero import pedir_numero

def funcion_comida(pedir_numero_func, enviar_mensaje):
    """
    Adaptado para WhatsApp:
    - pedir_numero_func: función que recibe mensaje y lista de opciones y devuelve la opción seleccionada.
    - enviar_mensaje: función que recibe un texto y lo envía al usuario (Twilio).
    """
    while True:
        enviar_mensaje("\n🍽️ Comida")
        enviar_mensaje("En proceso...\n")

        enviar_mensaje("1. Volver al menú principal")
        opcion = pedir_numero_func("Ingrese la opción: ", opciones_validas=[1])

        if opcion == 1:
            enviar_mensaje("Regresando al menú principal...")
            break
