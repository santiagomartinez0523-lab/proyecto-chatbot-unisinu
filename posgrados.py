from programas.numero import pedir_numero

def funcion_posgrados():
    while True:
        print("\n¿Qué nivel de posgrado te interesa?")
        print("1. Especializaciones")
        print("2. Maestrías")
        print("3. Doctorados")
        print("4. Volver al menú principal")
        
        opcion = pedir_numero("Seleccione una opción: ", opciones_validas=[1,2,3,4])
        
        if opcion == 4:
            break
            
        niveles = {1: 'especializaciones', 2: 'maestrias', 3: 'doctorados'}
        print(f"\nMostrando {niveles[opcion]}...")
        # Aquí iría la lógica de mostrar los programas de posgrado
