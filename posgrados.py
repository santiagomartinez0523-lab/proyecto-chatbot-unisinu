from programas.numero import pedir_numero
def funcion_posgrados():
    while True:

        print('de que carrera quieres saber?')
        print('''1. Ingeniería de Sistemas
2. Ingeniería Industrial
3. Ingeniería Civil
4. Ingeniería Eléctrica 
5. Ingeniería Electromecánica
    ''')
        opcion = pedir_numero("Ingrese la opción: ", opciones_validas=[1,2,3,4,5])
        match opcion:
            case 1:
                print('En ingenieria de sistemas existe Doctorado, Maestría, Especialización')
                print('De que te quieres informar?')
                print('''1. Doctorado
2. Maestría
3. Especialización''')
                opcion = pedir_numero("Ingrese la opción: ", opciones_validas=[1,2,3,4,5])
                match opcion:
                    case 1:
                        print('''Doctorado en Tecnologías de la Información
Duración: 6 semestres 
Valor total del programa: $84.000.000 COP 
Costo por semestre: $14.000.000 COP''')
                        print('Deseas saber algo mas?')
                        print('1. Si')
                        print('2. No')
                        opcion = pedir_numero("Ingrese la opción: ", opciones_validas=[1,2])
                        match opcion:
                            case 1:
                                continue
                            case 2:
                                print('Un gusto haber resolvido tus dudas')
                                break
                    
                    
                    case 2:
                        print('''Magíster en Tecnologías de la Información
Duración: 3 semestres
Valor total del programa: $34.500.000 COP''')
                        opcion = pedir_numero("Ingrese la opción: ", opciones_validas=[1,2])
                        match opcion:
                            case 1:
                                continue
                            case 2:
                                print('Un gusto haber resolvido tus dudas')
                                break
                    
                    
                    case 3:
                        print('''Especialista en Tecnologías de la Información
Duración: 1 año
Valor total del programa: $12.000.000 COP
Costo por semestre: $6.000.000 COP''')
                        print('1. Si')
                        print('2. No')
                        opcion = pedir_numero("Ingrese la opción: ", opciones_validas=[1,2])
                        match opcion:
                            case 1:
                                continue
                            case 2:
                                print('Un gusto haber resolvido tus dudas')
                                break
            case 2:
                print('En proceso...')
                break
            case 3:
                print('En proceso...')
                break
            case 4:
                print('En proceso...')
                break
            case 5:
                print('En proceso...')
                break
