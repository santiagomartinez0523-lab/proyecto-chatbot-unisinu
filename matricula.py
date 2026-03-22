from programas.numero import pedir_numero
from PIL import Image

def funcion_matriculas():
    while True:
        print("\n¿Qué deseas consultar de la matrícula?")
        print("1. Pasos de inscripción")
        print("2. Pasos para adicionar materias")
        print("3. Requisitos generales")
        print("4. Volver al menú principal")
        
        opcion = pedir_numero("Seleccione una opción: ", opciones_validas=[1,2,3,4])
        
        if opcion == 1:
            print("\nPasos de inscripción:")
            print("1. Ingresar al portal académico.")
            print("2. Ir a la sección 'Matrícula en Línea'.")
            print("3. Seleccionar las materias según tu pensum.")
            img = Image.open("image/matricula-1.jpg")
            img.show()
        elif opcion == 2:
            print("\nPasos para adicionar:")
            print("1. El proceso se realiza después de la matrícula regular.")
            print("2. Debes tener cupo disponible.")
            img = Image.open("image/matricula-2.jpg")
            img.show()
        elif opcion == 3:
             print("\nRequisitos generales...")
        elif opcion == 4:
            break
