def pedir_numero(mensaje, opciones_validas=None):
    """Función reutilizable para pedir un número y validar entrada"""
    while True:
        try:
            entrada = input(mensaje).strip()
            if not entrada:
                print("Por favor ingrese un número")
                continue

            opcion = int(entrada)
            if opciones_validas and opcion not in opciones_validas:
                print("Opción no válida, intente de nuevo.")
                continue
            return opcion

        except ValueError:
            print("Por favor ingrese un número")
