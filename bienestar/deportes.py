from programas.numero import pedir_numero

def funcion_deportes(pedir_numero_func, enviar_mensaje):
    """
    Adaptado para WhatsApp:
    - pedir_numero_func: función que recibe mensaje y lista de opciones y devuelve la opción seleccionada.
    - enviar_mensaje: función que recibe un texto y lo envía al usuario (Twilio).
    """
    while True:
        enviar_mensaje("\n🏆 Deportes")
        enviar_mensaje("Seleccione el deporte sobre el cual desea recibir más información:\n")
        enviar_mensaje('''1. Fútbol
2. Futsala
3. Taekwondo
4. Rugby
5. Levantamiento de Pesas
6. Vóleybol
7. Baloncesto
8. Softbol
9. Tenis de Mesa
10. Gimnasio Multifuerza
''')

        opcion_deporte = pedir_numero_func("Ingrese la opción: ", opciones_validas=[1,2,3,4,5,6,7,8,9,10])

        # Solo preguntar género para Fútbol, Vóleybol y Baloncesto
        genero = None
        if opcion_deporte in [1, 6, 7]:
            enviar_mensaje("\nSeleccione su género:")
            enviar_mensaje("1. Masculino\n2. Femenino")
            genero = pedir_numero_func("Ingrese la opción: ", opciones_validas=[1,2])

        match opcion_deporte:
            case 1:
                enviar_mensaje("\n⚽ Información de Fútbol:")
                if genero == 1:
                    enviar_mensaje("Martes: 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Miércoles: 3:30 p.m. - 5:30 p.m.")
                    enviar_mensaje("Jueves: 3:30 p.m. - 5:30 p.m.")
                    enviar_mensaje("Viernes: 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Instructor: Víctor Acosta")
                    enviar_mensaje("Lugar: Cancha de fútbol 8")
                else:
                    enviar_mensaje("Lunes: 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Miércoles: 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Instructores: Víctor Acosta y Rafael Palma")
                    enviar_mensaje("Lugar: Cancha de fútbol 8")

            case 2:
                enviar_mensaje("\n🥅 Información de Futsala:")
                enviar_mensaje("Martes: 6:30 p.m. - 8:30 p.m.")
                enviar_mensaje("Jueves: 6:30 p.m. - 8:30 p.m.")
                enviar_mensaje("Viernes: 6:30 p.m. - 8:30 p.m.")
                enviar_mensaje("Instructor: Víctor Acosta")
                enviar_mensaje("Lugar: Cancha múltiple")

            case 3:
                enviar_mensaje("\n🥋 Información de Taekwondo:")
                enviar_mensaje("Lunes: 2:00 p.m. - 4:00 p.m.")
                enviar_mensaje("Martes: 6:00 p.m. - 8:00 p.m.")
                enviar_mensaje("Miércoles: 2:00 p.m. - 4:00 p.m.")
                enviar_mensaje("Jueves: 6:00 p.m. - 8:00 p.m.")
                enviar_mensaje("Viernes: 2:00 p.m. - 4:00 p.m.")
                enviar_mensaje("Instructor: Alejandra Mendoza")
                enviar_mensaje("Lugar: Kiosco Alfa")
                enviar_mensaje("\n💪 Entrenamiento de fuerza adicional:")
                enviar_mensaje("Lunes a Viernes: 10:00 a.m. - 12:00 p.m. (en el gimnasio)")

            case 4:
                enviar_mensaje("\n🏉 Información de Rugby:")
                enviar_mensaje("Martes: 6:00 p.m. - 8:00 p.m.")
                enviar_mensaje("Jueves: 6:00 p.m. - 8:00 p.m.")
                enviar_mensaje("Instructor: Juan Sierra")
                enviar_mensaje("Lugar: Cancha de fútbol 8")

            case 5:
                enviar_mensaje("\n🏋️ Información de Levantamiento de Pesas:")
                enviar_mensaje("Lunes a Viernes: 10:00 a.m. - 12:00 p.m.")
                enviar_mensaje("Lunes a Viernes: 4:00 p.m. - 6:00 p.m.")
                enviar_mensaje("Instructor: Mike Berrocal")
                enviar_mensaje("Lugar: Gimnasio")

            case 6:
                enviar_mensaje("\n🏐 Información de Vóleybol:")
                if genero == 1:
                    enviar_mensaje("Lunes: 4:00 p.m. - 6:00 p.m.")
                    enviar_mensaje("Miércoles: 4:00 p.m. - 6:00 p.m.")
                    enviar_mensaje("Viernes: 4:00 p.m. - 6:00 p.m.")
                    enviar_mensaje("Instructor: Pedro Olascoaga")
                else:
                    enviar_mensaje("Lunes: 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Miércoles: 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Viernes: 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Instructor: Pedro Olascoaga")
                enviar_mensaje("Lugar: Cancha múltiple")

            case 7:
                enviar_mensaje("\n🏀 Información de Baloncesto:")
                if genero == 1:
                    enviar_mensaje("Martes: 4:30 p.m. - 6:30 p.m.")
                    enviar_mensaje("Jueves: 4:30 p.m. - 6:30 p.m.")
                    enviar_mensaje("Instructor: Pedro Olascoaga")
                else:
                    enviar_mensaje("Lunes: 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Miércoles: 2:00 p.m. - 4:00 p.m. y 6:00 p.m. - 8:00 p.m.")
                    enviar_mensaje("Jueves: 4:00 p.m. - 6:00 p.m.")
                    enviar_mensaje("Instructor: Juan Sierra")
                enviar_mensaje("Lugar: Cancha múltiple")

            case 8:
                enviar_mensaje("\n🥎 Información de Softbol:")
                enviar_mensaje("Lunes: 4:00 p.m. - 6:00 p.m.")
                enviar_mensaje("Martes: 6:00 p.m. - 8:00 p.m.")
                enviar_mensaje("Miércoles: 4:00 p.m. - 6:00 p.m.")
                enviar_mensaje("Jueves: 4:00 p.m. - 6:00 p.m.")
                enviar_mensaje("Viernes: (en la mañana)")
                enviar_mensaje("Instructor: José Barrios Martínez")
                enviar_mensaje("Lugar: Villa Olímpica / Estadio Amín Manzur / Cancha de fútbol 8")

            case 9:
                enviar_mensaje("\n🏓 Información de Tenis de Mesa:")
                enviar_mensaje("Lunes a Viernes: 9:00 a.m. - 11:00 a.m.")
                enviar_mensaje("Instructor: José Barrios")
                enviar_mensaje("Lugar: Parque Líbano")

            case 10:
                enviar_mensaje("\n🏋️‍♂️ Información de Gimnasio Multifuerza:")
                enviar_mensaje("Lunes a Jueves: 8:00 a.m. - 12:00 p.m. / 4:00 p.m. - 8:00 p.m.")
                enviar_mensaje("Viernes: 8:00 a.m. - 12:00 p.m. / 3:00 p.m. - 7:00 p.m.")
                enviar_mensaje("Instructor: Mike Berrocal Martínez")
                enviar_mensaje("Lugar: Cerca del kiosco principal")

        # Pregunta si quiere otro deporte
        enviar_mensaje("\n¿Deseas saber de otro deporte?")
        enviar_mensaje("1. Sí\n2. No, gracias")
        otra = pedir_numero_func("Ingrese la opción: ", opciones_validas=[1,2])

        if otra == 2:
            enviar_mensaje("Fue un gusto ayudarte, ¡espero haberte brindado la información que buscabas! 😊")
            enviar_mensaje("Regresando al menú principal...")
            break
