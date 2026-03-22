from programas.numero import pedir_numero


def funcion_electromecanica():
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
                print("1. Cálculo Diferencial\n2. Álgebra Lineal\n3. Materiales de Ingeniería\n4. Dibujo Electromecánico\n5. Gestión Financiera y Administrativa\n6. FH II")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Cálculo Diferencial, es necesario haber cursado previamente Precálculo.")
                    case 2:
                        print("La asignatura de Álgebra Lineal no presenta requisitos previos para ser cursada.")
                    case 3:
                        print("Para cursar la asignatura de Materiales de Ingeniería, es necesario haber cursado previamente Química Básica.")
                    case 4:
                        print("La asignatura de Dibujo Electromecánico no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("La asignatura de Gestión Financiera y Administrativa no presenta requisitos previos para ser cursada.")
                    case 6:
                        print("La asignatura de FH II no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 3:
                print("\nMaterias disponibles en Semestre III:")
                print("1. Cálculo Integral\n2. Física Newtoniana y Laboratorio\n3. Probabilidad y Estadística\n4. Estática\n5. Circuitos Eléctricos I y Laboratorio\n6. FH III")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Cálculo Integral, es necesario haber cursado previamente Cálculo Diferencial.")
                    case 2:
                        print("Para cursar la asignatura de Física Newtoniana y su respectivo laboratorio, es necesario haber cursado previamente Cálculo Diferencial.")
                    case 3:
                        print("La asignatura de Probabilidad y Estadística no presenta requisitos previos para ser cursada.")
                    case 4:
                        print("Para cursar la asignatura de Estática, es necesario haber cursado previamente Materiales de Ingeniería.")
                    case 5:
                        print("La asignatura de Circuitos Eléctricos I y su respectivo laboratorio no presenta requisitos previos para ser cursada.")
                    case 6:
                        print("La asignatura de FH III no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 4:
                print("\nMaterias disponibles en Semestre IV:")
                print("1. Cálculo Vectorial\n2. Física Electromagnética y Laboratorio\n3. Modelos Lineales\n4. Dinámica\n5. Circuitos Eléctricos II y Laboratorio\n6. FH VI")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral.")
                    case 2:
                        print("Para cursar la asignatura de Física Electromagnética y laboratorio, es necesario haber cursado previamente Física Newtoniana y laboratorio.")
                    case 3:
                        print("Para cursar la asignatura de Modelos Lineales, es necesario haber cursado previamente Probabilidad y Estadística.")
                    case 4:
                        print("Para cursar la asignatura de Dinámica, es necesario haber cursado previamente Estática.")
                    case 5:
                        print("Para cursar la asignatura de Circuitos Eléctricos II y laboratorio, es necesario haber cursado previamente Circuitos Eléctricos I y laboratorio.")
                    case 6:
                        print("La asignatura de FH VI no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 5:
                print("\nMaterias disponibles en Semestre V:")
                print("1. Métodos Numéricos\n2. Ecuaciones Diferenciales\n3. Termofluidos de Ingeniería I\n4. Resistencia de Materiales\n5. Teoría Electromagnética\n6. FH V")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Métodos Numéricos, es necesario haber cursado previamente Cálculo Vectorial.")
                    case 2:
                        print("La asignatura de Ecuaciones Diferenciales debe cursarse de manera simultánea con la asignatura de Métodos Numéricos.")
                    case 3:
                        print("La asignatura de Termofluidos de Ingeniería I no presenta requisitos previos para ser cursada.")
                    case 4:
                        print("Para cursar la asignatura de Resistencia de Materiales, es necesario haber cursado previamente Dinámica.")
                    case 5:
                        print("Para cursar la asignatura de Física Electromagnética y laboratorio, es necesario haber cursado previamente Física Electromagnética y laboratorio.")
                    case 6:
                        print("La asignatura de FH V no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 6:
                print("\nMaterias disponibles en Semestre VI:")
                print("1. Termofluidos de Ingeniería II\n2. Ingeniería de Fluidos\n3. Modelamiento y Simulación de Sistemas Electromecánicos\n4. Máquinas Eléctricas I\n5. Ingeniería de Mecanismos y Diseño de Máquinas\n6. Electrónica y Fundamentos de Control")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Termofluidos de Ingeniería II, es necesario haber cursado previamente Termofluidos de Ingeniería I.")
                    case 2:
                        print("Para cursar la asignatura de Ingeniería de Fluidos, es necesario haber cursado previamente Termofluidos de Ingeniería I.")
                    case 3:
                        print("La asignatura de Modelamiento y Simulación de Sistemas Electromecánicos no presenta requisitos previos para ser cursada.")
                    case 4:
                        print("Para cursar la asignatura de Máquinas Eléctricas I, es necesario haber cursado previamente Circuitos Eléctricos II y laboratorio.")
                    case 5:
                        print("Para cursar la asignatura de Ingeniería de Mecanismos y Diseño de Máquinas, es necesario haber cursado previamente Resistencia de Materiales.")
                    case 6:
                        print("La asignatura de Electrónica y Fundamentos de Control no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 7:
                print("\nMaterias disponibles en Semestre VII:")
                print("1. Proyectos de Ingeniería\n2. Transferencia de Calor\n3. Innovación en Mecanizado Avanzado\n4. Máquinas Eléctricas II\n5. Generación Hidráulica\n6. Mantenimiento de Sistemas Electromecánicos\n7. FH VI")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6,7])

                match materia:
                    case 1:
                        print("La asignatura de Proyectos de Ingeniería no presenta restricciones ni requisitos previos para ser cursada.")
                    case 2:
                        print("Para cursar la asignatura de Transferencia de Calor, es necesario haber cursado previamente Termofluidos de Ingeniería II.")
                    case 3:
                        print("Para cursar la asignatura de Innovación en Mecanizado Avanzado, es necesario haber cursado previamente Modelamiento y Simulación de Sistemas Electromecánicos.")
                    case 4:
                        print("Para cursar la asignatura de Máquinas Eléctricas II, es necesario haber cursado previamente Máquinas Eléctricas I.")
                    case 5:
                        print("Para cursar la asignatura de Generación Hidráulica, es necesario haber cursado previamente Ingeniería de Fluidos.")
                    case 6:
                        print("La asignatura de Mantenimiento de Sistemas Electromecánicos no presenta requisitos previos para ser cursada.")
                    case 7:
                        print("La asignatura de FH VI no presenta restricciones ni requisitos previos para ser cursada.")

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
                print("1. Opción de Grado\n2. Electiva Profesional II\n3. Práctica Profesional\n4. Ética Profesional")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Opción de Grado, es necesario haber cursado previamente Seminario de Investigación.")
                    case 2:
                        print("La asignatura de Electiva Profesional II no presenta requisitos previos para ser cursada.")
                    case 3:
                        print("Para cursar la asignatura de Práctica Profesional, es necesario haber cursado previamente Prototipado y Manufactura Inteligente.")
                    case 4:
                        print("La asignatura de Ética Profesional no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 10:
                print("Regresando al menú principal...")
                break
