from PIL import Image
from programas.numero import pedir_numero
def funcion_matriculas():
    while True:
        print('1. Como ingresar una materia')
        print('2. Como dar de baja a una materia')
        print('3. Fechas limite')
        opcion = pedir_numero("Ingrese la opción: ", opciones_validas=[1,2,3])
        match opcion:
                case 1:
                    print('Como pincipal debes ingresar a la interfas de Elysa, una vez ingresado presiona en autoservicio.')
                    img = Image.open("image/matricula-1.jpg")
                    img.show()
                    print('Despues de haber ingresado a auto servicio presionamos carrito de compras inscripcion.')
                    img = Image.open("image/matricula-2.jpg")
                    img.show()
                    print('Justo despues de haber ingresado al carrito de compras te apareceran la interfaz en donde puedes agregar el codigo de la materia que piensas meter a tu horario.')
                    img = Image.open("image/matricula-3.jpg")
                    img.show()
                    print('Deseas saber algo mas sobre las matriculas?')
                    print('1. Si')
                    print('2. No, gracias')
                    requisito = pedir_numero('Ingrese la opcion ', opciones_validas=[1,2])
                    match requisito:
                        case 1:
                            continue
                        case 2:
                            print('Ha sido un gusto poder solucionar tus inquietudes.')
                            break
                case 2:
                    print('En proceso...')
                    break
                case 3:
                    print('En proceso...')
                    break
