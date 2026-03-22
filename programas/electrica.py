from programas.numero import pedir_numero

def funcion_electrica():
    while True:
        print("\nSeleccione el semestre de Ingeniería Eléctrica:")
        print("1-9 Semestre, 10-Volver")
        semestre = pedir_numero("Ingrese opción: ", opciones_validas=list(range(1,11)))
        if semestre == 10: break
        # ... logic
