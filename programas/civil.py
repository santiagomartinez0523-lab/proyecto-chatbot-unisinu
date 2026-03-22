from programas.numero import pedir_numero

def funcion_civil():
    while True:
        print("\nPor favor, indica el semestre en el que se encuentra la materia sobre la cual deseas obtener información.")
        print('''1. Semestre I
2. Semestre II
3. Semestre III
4. Semestre IV
5. Semestre V
6. Semestre VI
7. Semestre VII
8. Semestre VIII
9. Semestre IX
10. Salir al menú principal''')

        semestre = pedir_numero("Ingrese el semestre: ", opciones_validas=[1,2,3,4,5,6,7,8,9,10])

        match semestre:
            case 1:
                print("\nLas materias de primer semestre no tienen restricción.")
                seguir = pedir_numero("¿Desea verificar otra materia? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 2:
                print("\nMaterias disponibles en Semestre II:")
                print("1. Constitución y Sociedad\n2. Ética y Convivencia Ciudadana\n3. Física I y Laboratorio\n4. Investigación en Ingeniería\n5. Álgebra Lineal\n6. Cálculo Integral")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("La asignatura de Constitución y Sociedad no presenta requisitos previos para ser cursada.")
                    case 2:
                        print("La asignatura de Ética y Convivencia Ciudadana no presenta requisitos previos para ser cursada.")
                    case 3:
                        print("Para cursar la asignatura de Física I y Laboratorio, es necesario haber cursado previamente Cálculo Diferencial.")
                    case 4:
                        print("La asignatura de Investigación en Ingeniería no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("Para cursar la asignatura de Álgebra Lineal, es necesario haber cursado previamente Álgebra y Geometría Analítica.")
                    case 6:
                        print("Para cursar la asignatura de Cálculo Integral, es necesario haber cursado previamente Cálculo Diferencial.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 3:
                print("\nMaterias disponibles en Semestre III:")
                print("1. Física II y Laboratorio\n2. Topografía y Práctica\n3. Estática\n4. Cálculo Vectorial\n5. Química Básica")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Física II y su respectivo laboratorio, es necesario haber cursado previamente Física I y laboratorio y Cálculo Integral.")
                    case 2:
                        print("Para cursar la asignatura de Topografía y su práctica, es necesario haber cursado previamente Dibujo de Ingeniería.")
                    case 3:
                        print("Para cursar la asignatura de Estática, es necesario haber cursado previamente Física I y laboratorio.")
                    case 4:
                        print("Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral.")
                    case 5:
                        print("La asignatura de Química Básica no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 4:
                print("\nMaterias disponibles en Semestre IV:")
                print("1. Física III y Laboratorio\n2. Sistema de Información Geográfica\n3. Resistencia de Materiales\n4. Programación de Computadores I\n5. Ecuaciones Diferenciales")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Física III y laboratorio, es necesario haber aprobado previamente Física II y laboratorio, y cursarla de manera simultánea con la asignatura de Ecuaciones Diferenciales.")
                    case 2:
                        print("Para cursar la asignatura de Sistema de Información Geográfica, es necesario haber cursado previamente Topografía y su práctica.")
                    case 3:
                        print("Para cursar la asignatura de Resistencia de Materiales, es necesario haber cursado previamente Estática.")
                    case 4:
                        print("La asignatura de Programación de Computadores I no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("Para cursar la asignatura de Ecuaciones Diferenciales, es necesario haber aprobado previamente Cálculo Vectorial y cursarla de manera simultánea con la asignatura de Física III y laboratorio.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 5:
                print("\nMaterias disponibles en Semestre V:")
                print("1. Análisis Estructural\n2. Geología\n3. Mecánica de Fluidos\n4. Probabilidad y Estadística\n5. Métodos Numéricos")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Análisis Estructural, es necesario haber cursado previamente Resistencia de Materiales.")
                    case 2:
                        print("Para cursar la asignatura de Geología, es necesario haber cursado previamente Química Básica.")
                    case 3:
                        print("Para cursar la asignatura de Mecánica de Fluidos, es necesario haber cursado previamente Física I y laboratorio.")
                    case 4:
                        print("Para cursar la asignatura de Probabilidad y Estadística, es necesario haber cursado previamente Cálculo Integral.")
                    case 5:
                        print("Para cursar la asignatura de Métodos Numéricos, es necesario haber cursado previamente Ecuaciones Diferenciales.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 6:
                print("\nEn proceso...")
                seguir = pedir_numero("¿Desea verificar otra materia? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 7:
                print("\nEn proceso...")
                seguir = pedir_numero("¿Desea verificar otra materia? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 8:
                print("\nEn proceso...")
                seguir = pedir_numero("¿Desea verificar otra materia? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 9:
                print("\nEn proceso...")
                seguir = pedir_numero("¿Desea verificar otra materia? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 10:
                print("Regresando al menú principal...")
                break
