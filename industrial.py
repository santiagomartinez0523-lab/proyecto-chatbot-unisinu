from numero import pedir_numero



def funcion_industrial():
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
                print("1. Álgebra Lineal\n2. Cálculo Integral\n3. Física I y Laboratorio\n4. CCU 2\n5. CCU 3\n6. CCU 4")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Álgebra Lineal, es necesario haber aprobado previamente Álgebra y Geometría Analítica.")
                    case 2:
                        print("Para cursar la asignatura de Cálculo Integral, es necesario haber aprobado previamente Cálculo Diferencial.")
                    case 3:
                        print("Para cursar la asignatura de Física I y su laboratorio, es necesario haber aprobado previamente Cálculo Diferencial.")
                    case _:
                        print("Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 3:
                print("\nMaterias disponibles en Semestre III:")
                print("1. Cálculo Vectorial\n2. Física II y Laboratorio\n3. Termodinámica\n4. Probabilidad y Estadística\n5. CCU 5\n6. Ética General")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Cálculo Vectorial, es necesario haber aprobado previamente Cálculo Integral.")
                    case 2:
                        print("Para cursar la asignatura de Física II y su respectivo laboratorio, es necesario haber aprobado previamente Física I y su respectivo laboratorio.")
                    case 3:
                        print("Para cursar la asignatura de Termodinámica, es necesario haber aprobado previamente Física I y su laboratorio.")
                    case 4:
                        print("Para cursar la asignatura de Probabilidad y Estadística, es necesario haber aprobado previamente Cálculo Integral.")
                    case 5:
                        print("Actualmente, la asignatura CCU 5 no presenta restricciones previas para ser cursada.")
                    case 6:
                        print("Actualmente, la asignatura de Ética General no presenta restricciones previas para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 4:
                print("\nMaterias disponibles en Semestre IV:")
                print("1. Ecuaciones Diferenciales\n2. Física III y Laboratorio\n3. Mecánica de Sólidos\n4. Programación de Computadores I\n5. CCU 6")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Ecuaciones Diferenciales, es necesario haber aprobado previamente Cálculo Vectorial.")
                    case 2:
                        print("Para cursar la asignatura de Física III y su respectivo laboratorio, es necesario haber aprobado previamente Física II y su respectivo laboratorio.")
                    case 3:
                        print("Para cursar la asignatura de Mecánica de Sólidos, es necesario haber aprobado previamente Física I y su respectivo laboratorio.")
                    case 4:
                        print("La asignatura de Programación de Computadores I no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("Actualmente, la asignatura CCU 6 no presenta restricciones previas para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 5:
                print("\nMaterias disponibles en Semestre V:")
                print("1. Investigación de Operaciones I\n2. Transferencia de Calor\n3. Procesos Industriales I y Laboratorio\n4. Electrotecnia General y Laboratorio\n5. Seminario de Investigación I")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Investigación de Operaciones I, es necesario haber aprobado previamente Álgebra Lineal.")
                    case 2:
                        print("Para cursar la asignatura de Transferencia de Calor, es necesario haber aprobado previamente Termodinámica.")
                    case 3:
                        print("Para cursar la asignatura de Procesos Industriales I y su laboratorio, es necesario haber aprobado previamente Mecánica de Sólidos.")
                    case 4:
                        print("Para cursar la asignatura de Electrotecnia General y su laboratorio, es necesario haber aprobado previamente Física II y su laboratorio.")
                    case 5:
                        print("La asignatura de Seminario I no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 6:
                print("\nMaterias disponibles en Semestre VI:")
                print("1. Investigación de Operaciones II\n2. Ingeniería Económica\n3. Procesos Industriales II y Laboratorio\n4. Seminario de Investigación II\n5. Electiva Complementaria I")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Investigación de Operaciones II, es necesario haber aprobado previamente Investigación de Operaciones I.")
                    case 2:
                        print("Para cursar la asignatura de Ingeniería Económica, es necesario haber aprobado previamente Cálculo Diferencial.")
                    case 3:
                        print("Para cursar la asignatura de Procesos Industriales II y su laboratorio, es necesario haber aprobado previamente Procesos Industriales I y su laboratorio.")
                    case 4:
                        print("La asignatura de Seminario II no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("La asignatura de Electiva Complementaria I no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 7:
                print("\nMaterias disponibles en Semestre VII:")
                print("1. Diseño de Sistemas Productivos\n2. Diseño y Análisis de Experimentos\n3. Gestión de Calidad\n4. Electiva Complementaria II\n5. Ingeniería de Software")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Diseño de Sistemas Productivos, es necesario haber aprobado previamente Investigación de Operaciones II.")
                    case 2:
                        print("Para cursar la asignatura de Diseño y Análisis de Experimentos, es necesario haber aprobado previamente Probabilidad y Estadística.")
                    case 3:
                        print("Para cursar la asignatura de Gestión de Calidad, es necesario haber aprobado previamente Probabilidad y Estadística.")
                    case 4:
                        print("La asignatura de Electiva Complementaria II no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("Para cursar la asignatura de Ingeniería de Software, es necesario haber aprobado previamente Programación de Computadores I.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 8:
                print("\nMaterias disponibles en Semestre VIII:")
                print("1. Gestión de Operaciones\n2. Ética Profesional\n3. Legislación para Ingenieros\n4. Simulación de Procesos e Inventarios\n5. Salud Ocupacional y Seguridad Industrial")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Gestión de Operaciones, es necesario haber aprobado previamente Diseño de Sistemas Productivos.")
                    case 2:
                        print("La asignatura de Ética Profesional no presenta requisitos previos.")
                    case 3:
                        print("La asignatura de Legislación para Ingenieros no presenta requisitos previos para ser cursada.")
                    case 4:
                        print("Para cursar la asignatura de Simulación de Procesos e Inventarios, es necesario haber aprobado previamente Diseño y Análisis de Experimentos.")
                    case 5:
                        print("Para cursar la asignatura de Salud Ocupacional y Seguridad Industrial, es necesario haber aprobado previamente Gestión de Calidad.")

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
                        print("Para cursar la asignatura de Práctica Empresarial, es necesario haber aprobado previamente todas las materias hasta el octavo semestre.")
                    case 5:
                        print("La asignatura de Opción de Grado no presenta restricciones ni requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 10:
                print("Regresando al menú principal...")
                break
