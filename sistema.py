
from numero import pedir_numero



def funcion_sistema():
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
9. Semestre XI
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
                print("1. Programación II\n2. Física I y Laboratorio\n3. Cálculo Integral\n4. CCU 2\n5. CCU 3\n6. CCU 4")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar Programación II, es requisito haber aprobado previamente Programación I.")
                    case 2:
                        print("Para cursar Física I y su laboratorio, es necesario haber aprobado previamente Cálculo Diferencial.")
                    case 3:
                        print("Para cursar Cálculo Integral, es necesario haber aprobado previamente Cálculo Diferencial.")
                    case _:
                        print("Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 3:
                print("\nMaterias disponibles en Semestre III:")
                print("1. Estructura de Datos\n2. Electrónica\n3. Cálculo Vectorial\n4. Probabilidad y Estadística\n5. CCU 5\n6. Ética General")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Estructura de Datos, es necesario haber aprobado previamente Programación II.")
                    case 2:
                        print("Para cursar la asignatura de Electrónica, es necesario haber cursado previamente Física I y su respectivo laboratorio.")
                    case 3:
                        print("Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral.")
                    case 4:
                        print("Para cursar la asignatura de Probabilidad y Estadística, es necesario haber cursado previamente Cálculo Integral.")
                    case 5:
                        print("Actualmente, la asignatura CCU 5 no presenta restricciones previas para ser cursada.")
                    case 6:
                        print("Actualmente, la asignatura de Ética General no presenta restricciones previas para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 4:
                print("\nMaterias disponibles en Semestre IV:")
                print("1. Análisis de Algoritmos\n2. Circuitos Digitales\n3. Bases de Datos\n4. Ecuaciones Diferenciales\n5. CCU 6")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Análisis de Algoritmos, es necesario haber aprobado previamente Estructura de Datos.")
                    case 2:
                        print("Para cursar la asignatura de Circuitos Digitales, es necesario haber cursado previamente Electrónica.")
                    case 3:
                        print("Para cursar la asignatura de Bases de Datos, es necesario haber aprobado previamente Estructura de Datos.")
                    case 4:
                        print("Para cursar la asignatura de Ecuaciones Diferenciales, es necesario haber aprobado previamente Cálculo Vectorial.")
                    case 5:
                        print("Actualmente, la asignatura CCU 6 no presenta restricciones previas para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 5:
                print("\nMaterias disponibles en Semestre V:")
                print("1. Administración de Bases de Datos\n2. Computación Móvil\n3. Arquitectura del Computador\n4. Robótica y Laboratorio\n5. Seminario de Investigación I")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Administración de Bases de Datos, es necesario haber cursado previamente Bases de Datos.")
                    case 2:
                        print("Para cursar la asignatura de Computación Móvil, es necesario haber cursado previamente Bases de Datos.")
                    case 3:
                        print("Para cursar la asignatura de Arquitectura del Computador, es necesario haber cursado previamente Circuitos Digitales.")
                    case 4:
                        print("Para cursar la asignatura de Robótica y su respectivo laboratorio, es necesario haber cursado previamente Circuitos Digitales.")
                    case 5:
                        print("La asignatura de Seminario I no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 6:
                print("\nMaterias disponibles en Semestre VI:")
                print("1. Sistemas Operativos\n2. Sistemas de Información y Gestión Telemática\n3. Seminario de Investigación II\n4. Electiva Complementaria I")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Sistemas Operativos, es necesario haber cursado previamente Arquitectura del Computador.")
                    case 2:
                        print("Para cursar la asignatura de Sistemas de Información y Gestión Telemática, es necesario haber cursado previamente Administración de Bases de Datos.")
                    case 3:
                        print("La asignatura de Seminario de Investigación II no presenta requisitos previos para ser cursada.")
                    case 4:
                        print("La asignatura de Electiva Complementaria I no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 7:
                print("\nMaterias disponibles en Semestre VII:")
                print("1. Auditoría de Sistemas\n2. Electiva Complementaria II\n3. Ingeniería de Software\n4. Redes de Datos\n5. Sistemas de Tiempo Real")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                            print("La asignatura de Auditoría de Sistemas no presenta requisitos previos para ser cursada.")
                    case 2:
                        print("La asignatura de Electiva Complementaria II no presenta requisitos previos para ser cursada.")
                    case 3:
                        print("Para cursar la asignatura de Ingeniería de Software, es necesario haber cursado previamente Sistemas de Información y Gestión.")
                    case 4:
                        print("Para cursar la asignatura de Redes de Datos, es necesario haber cursado previamente Telemática.")
                    case 5:
                        print("Para cursar la asignatura de Sistemas de Tiempo Real, es necesario haber cursado previamente Sistemas Operativos.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 8:
                print("\nMaterias disponibles en Semestre VIII:")
                print("1. Computación Gráfica\n2. Programación Web\n3. Ética Profesional\n4. Tecnología Informática en las Organizaciones\n5. Legislación para Ingenieros\n6. Administración y Mantenimiento de Redes")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Computación Gráfica, es necesario haber cursado previamente Álgebra y Geometría Analítica.")
                    case 2:
                        print("Para cursar la asignatura de Programación Web, es necesario haber cursado previamente Análisis de Algoritmos.")
                    case 3:
                        print("La asignatura de Ética Profesional no presenta restricciones ni requisitos previos para ser cursada.")
                    case 4:
                        print("Para cursar la asignatura de Tecnología Informática en las Organizaciones, es necesario haber aprobado previamente Ingeniería de Software.")
                    case 5:
                        print("La asignatura de Legislación para Ingenieros no presenta requisitos previos para ser cursada.")
                    case 6:
                        print("Para cursar la asignatura de Administración y Mantenimiento de Redes, es necesario haber cursado previamente Redes de Datos.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break
            case 9:
                print("\nMaterias disponibles en Semestre IX:")
                print("1. Electiva Profesional I\n2. Electiva Profesional II\n3. Electiva Profesional III\n4. Práctica Empresarial\n5. Opción de Grado")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("La asignatura Electiva Profesional I no presenta restricciones ni requisitos previos para ser cursada.")
                    case 2:
                        print("La asignatura Electiva Profesional II no presenta restricciones ni requisitos previos para ser cursada.")
                    case 3:
                        print("La asignatura Electiva Profesional III no presenta restricciones ni requisitos previos para ser cursada.")
                    case 4:
                        print("Para cursar la asignatura de Práctica Empresarial, es necesario haber cursado previamente Tecnología Informática en las Organizaciones.")
                    case 5:
                        print("La asignatura de Opción de Grado no presenta restricciones ni requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 10:
                print("Regresando al menú principal...")
                break
