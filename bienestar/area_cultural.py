from programas.numero import pedir_numero

def funcion_area_cultural(pedir_numero_func, enviar_mensaje):
    """
    Adaptado para WhatsApp:
    - pedir_numero_func: función que recibe mensaje y lista de opciones y devuelve la opción seleccionada.
    - enviar_mensaje: función que recibe un texto y lo envía al usuario (Twilio).
    """
    while True:
        enviar_mensaje("\n🎭 Área Cultural")
        enviar_mensaje("Actualmente existen 7 actividades, entre esas están:\n")
        enviar_mensaje('''1. Gaitas y Tambores
2. Grupo de Rock
3. Orquesta
4. Vallenato
5. Coro
6. Danza Moderna
7. Danza Folclórica
''')

        opcion_cultural = pedir_numero_func("Ingrese la opción: ", opciones_validas=[1,2,3,4,5,6,7])

        match opcion_cultural:
            case 1:
                enviar_mensaje("\n🥁 Información de Gaitas y Tambores:")
                enviar_mensaje("Instructor: Evelio Pacheco")
                enviar_mensaje("Lugar: Salón Omega")
                enviar_mensaje("Horarios:")
                enviar_mensaje("  • Lunes y Miércoles: 3:00 p.m. - 7:00 p.m.")
                enviar_mensaje("  • Martes y Viernes: 8:00 a.m. - 12:00 p.m.")
                enviar_mensaje("  • Jueves: 5:00 p.m. - 9:00 p.m.")
            case 2:
                enviar_mensaje("\n🎸 Información de Grupo de Rock:")
                enviar_mensaje("Instructor: Elvis Castillo")
                enviar_mensaje("Lugar: Sala de música, Salón Omega")
                enviar_mensaje("Horarios:")
                enviar_mensaje("  • Lunes y Miércoles: 4:00 p.m. - 8:00 p.m.")
                enviar_mensaje("  • Martes y Jueves: 8:00 a.m. - 12:00 p.m.")
                enviar_mensaje("  • Viernes: 2:00 p.m. - 6:00 p.m.")
            case 3:
                enviar_mensaje("\n🎻 Información de Orquesta:")
                enviar_mensaje("Instructor: Samir Berrocal")
                enviar_mensaje("Lugar: Sala de música")
                enviar_mensaje("Horarios:")
                enviar_mensaje("  • Lunes y Jueves: 4:00 p.m. - 8:00 p.m.")
                enviar_mensaje("  • Martes: 8:00 a.m. - 12:00 p.m. y 4:00 p.m. - 8:00 p.m.")
                enviar_mensaje("  • Viernes: 8:00 a.m. - 12:00 p.m.")
            case 4:
                enviar_mensaje("\n🎶 Información de Vallenato:")
                enviar_mensaje("Instructor: Camilo Cogollo")
                enviar_mensaje("Lugar: Sala de música")
                enviar_mensaje("Horarios:")
                enviar_mensaje("  • Lunes: 4:00 p.m. - 8:00 p.m.")
                enviar_mensaje("  • Martes y Viernes: 8:00 a.m. - 12:00 p.m.")
                enviar_mensaje("  • Miércoles: 2:00 p.m. - 6:00 p.m.")
                enviar_mensaje("  • Jueves: 3:00 p.m. - 7:00 p.m.")
            case 5:
                enviar_mensaje("\n🎤 Información de Coro:")
                enviar_mensaje("Instructora: Dayana Parra")
                enviar_mensaje("Lugar: Auditorio Zenú")
                enviar_mensaje("Horarios:")
                enviar_mensaje("  • Jueves: 2:30 p.m. - 5:00 p.m.")
            case 6:
                enviar_mensaje("\n💃 Información de Danza Moderna:")
                enviar_mensaje("Instructor: Enry Torres Martínez")
                enviar_mensaje("Lugar: Gimnasio")
                enviar_mensaje("Horarios:")
                enviar_mensaje("  • Lunes: 4:00 p.m. - 6:00 p.m.")
                enviar_mensaje("  • Martes: 10:00 a.m. - 12:00 p.m.")
                enviar_mensaje("  • Miércoles y Jueves: 6:00 p.m. - 8:00 p.m.")
            case 7:
                enviar_mensaje("\n🕺 Información de Danza Folclórica:")
                enviar_mensaje("Instructor: Enry Torres Martínez")
                enviar_mensaje("Lugar: Gimnasio")
                enviar_mensaje("Horarios:")
                enviar_mensaje("  • Lunes y Miércoles: 6:00 p.m. - 8:00 p.m.")
                enviar_mensaje("  • Martes: 8:00 a.m. - 10:00 a.m.")

        # Pregunta si quiere ver otra actividad
        enviar_mensaje("\n¿Deseas saber sobre otra actividad?")
        enviar_mensaje("1. Sí\n2. No, gracias")
        otra = pedir_numero_func("Ingrese la opción: ", opciones_validas=[1,2])

        if otra == 2:
            enviar_mensaje("Fue un gusto ayudarte, ¡espero que disfrutes de las actividades culturales!")
            enviar_mensaje("Regresando al menú principal...")
            break
