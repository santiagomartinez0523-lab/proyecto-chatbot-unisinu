from programas.numero import pedir_numero


def funcion_electrica():
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
                print("1. Álgebra Lineal\n2. Cálculo Integral\n3. Física I y Laboratorio\n4. Programación de Computadores\n5. Ética y Convivencia Ciudadana\n6. CCU")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Álgebra Lineal, es necesario haber cursado previamente Álgebra y Geometría Analítica.")
                    case 2:
                        print("Para cursar la asignatura de Cálculo Integral, es necesario haber cursado previamente Cálculo Diferencial.")
                    case 3:
                        print("Para cursar la asignatura de Física I y laboratorio, es necesario haber cursado previamente Cálculo Diferencial.")
                    case 4:
                        print("La asignatura de Programación de Computadores no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("La asignatura de Ética y Convivencia Ciudadana no presenta requisitos previos para ser cursada.")
                    case 6:
                        print("Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 3:
                print("\nMaterias disponibles en Semestre III:")
                print("1. Cálculo Vectorial\n2. Circuitos Eléctricos I y Laboratorio\n3. Física II y Laboratorio\n4. Seminario de Investigación I\n5. CCU\n6. Termodinámica")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral.")
                    case 2:
                        print("Para cursar la asignatura de Circuitos Eléctricos I y su respectivo laboratorio, es necesario haber cursado previamente Álgebra y Geometría Analítica.")
                    case 3:
                        print("Para cursar la asignatura de Física II y laboratorio, es necesario haber cursado previamente Física I y laboratorio.")
                    case 4:
                        print("La asignatura de Seminario de Investigación I no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.")
                    case 6:
                        print("Para cursar la asignatura de Termodinámica, es necesario haber cursado previamente Física I y laboratorio.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 4:
                print("\nMaterias disponibles en Semestre IV:")
                print("1. Ecuaciones Diferenciales\n2. Física III y Laboratorio\n3. Circuitos Eléctricos II y Laboratorio\n4. Curso de Libre Elección\n5. Probabilidad y Estadística")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Ecuaciones Diferenciales, es necesario haber cursado previamente Cálculo Vectorial.")
                    case 2:
                        print("Para cursar la asignatura de Física III y laboratorio, es necesario haber cursado previamente Física II y laboratorio.")
                    case 3:
                        print("Para cursar la asignatura de Circuitos Eléctricos II y laboratorio, es necesario haber cursado previamente Circuitos Eléctricos I y laboratorio.")
                    case 4:
                        print("La asignatura de Curso de Libre Elección no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("Para cursar la asignatura de Probabilidad y Estadística, es necesario haber aprobado previamente Cálculo Integral.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 5:
                print("\nMaterias disponibles en Semestre V:")
                print("1. Métodos Numéricos\n2. Teoría Electromagnética\n3. Medidas Eléctricas\n4. Electiva Complementaria\n5. Seminario de Investigación II\n6. Análisis de Sistemas")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Métodos Numéricos, es necesario haber cursado previamente Ecuaciones Diferenciales.")
                    case 2:
                        print("Para cursar la asignatura de Teoría Electromagnética, es necesario haber cursado previamente Física II y su respectivo laboratorio.")
                    case 3:
                        print("La asignatura de Medidas Eléctricas no presenta requisitos previos para ser cursada.")
                    case 4:
                        print("La asignatura de Electiva Complementaria no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("La asignatura de Seminario de Investigacion II no presenta requisitos previos para ser cursada.")
                    case 6:
                        print("La asignatura de Analisis de Sistemas no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 6:
                print("\nMaterias disponibles en Semestre VI:")
                print("1. Accionamientos Eléctricos y Laboratorio\n2. Ingeniería de Control y Laboratorio\n3. Instalaciones Eléctricas\n4. Máquinas Eléctricas I y Laboratorio\n5. Instrumentación Industrial Moderna\n6. Electrónica General y Laboratorio")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("La asignatura de Accionamientos Eléctricos y su respectivo laboratorio no presenta requisitos previos para ser cursada.")
                    case 2:
                        print("La asignatura de Ingeniería de Control y Lab no presenta requisitos previos para ser cursada.")
                    case 3:
                        print("La asignatura de Instalaciones Eléctricas no presenta requisitos previos para ser cursada.")
                    case 4:
                        print("Para cursar la asignatura de Máquinas Eléctricas I y laboratorio, es necesario haber cursado previamente Teoría Electromagnética.")
                    case 5:
                        print("La asignatura de Instrumentación Industrial Moderna no presenta requisitos previos para ser cursada.")
                    case 6:
                        print("Para cursar la asignatura de Electrónica General y laboratorio, es necesario haber cursado previamente Circuitos Eléctricos I y laboratorio.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 7:
                print("\nMaterias disponibles en Semestre VII:")
                print("1. Generación Térmica\n2. Electiva Profesional I\n3. Electrónica Digital y Laboratorio\n4. Máquinas Eléctricas II y Laboratorio\n5. Sistemas de Distribución de Energía")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Generación Térmica, es necesario haber cursado previamente Termodinámica.")
                    case 2:
                        print("La asignatura de Electiva Profesional I no presenta requisitos previos para ser cursada.")
                    case 3:
                        print("Para cursar la asignatura de Electrónica Digital y laboratorio, es necesario haber cursado previamente Electrónica General y laboratorio.")
                    case 4:
                        print("Para cursar la asignatura de Máquinas Eléctricas II y laboratorio, es necesario haber cursado previamente Máquinas Eléctricas I y laboratorio.")
                    case 5:
                        print("Para cursar la asignatura de Sistemas de Distribución de Energía, es necesario haber cursado previamente Instalaciones Eléctricas.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 8:
                print("\nMaterias disponibles en Semestre VIII:")
                print("1. Análisis de Sistemas de Potencia\n2. Electiva Profesional II\n3. Subestaciones Eléctricas\n4. Generación Hidráulica\n5. Economía Financiera\n6. Fundamentos de Administración")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("Para cursar la asignatura de Análisis de Sistemas de Potencia, es necesario haber cursado previamente Máquinas Eléctricas I y su respectivo laboratorio.")
                    case 2:
                        print("La asignatura de Electiva Profesional II no presenta requisitos previos para ser cursada.")
                    case 3:
                        print("Para cursar la asignatura de Subestaciones Eléctricas, es necesario haber cursado previamente Sistemas de Distribución de Energía.")
                    case 4:
                        print("La asignatura de Generación Hidráulica no presenta requisitos previos para ser cursada.")
                    case 5:
                        print("Para cursar la asignatura de Economía Financiera, es necesario haber cursado previamente Cálculo Diferencial.")
                    case 6:
                        print("La asignatura de Fundamentos de Administración no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 9:
                print("\nMaterias disponibles en Semestre IX:")
                print("1. Electiva Profesional III\n2. Líneas de Transmisión Eléctrica\n3. Protección de Sistemas de Potencia\n4. Tecnología de Alta Tensión\n5. Formulación y Evaluación de Proyectos\n6. Proyecto de Grado")
                materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                match materia:
                    case 1:
                        print("La asignatura de Electiva Profesional III no presenta requisitos previos para ser cursada.")
                    case 2:
                        print("Para cursar la asignatura de Líneas de Transmisión Eléctrica, es necesario haber cursado previamente Teoría Electromagnética.")
                    case 3:
                        print("Para cursar la asignatura de Protección de Sistemas de Potencia, es necesario haber cursado previamente Análisis de Sistemas de Potencia.")
                    case 4:
                        print("Para cursar la asignatura de Tecnología de Alta Tensión, es necesario haber cursado previamente Análisis de Sistemas de Potencia.")
                    case 5:
                        print("Para cursar la asignatura de Formulación y Evaluación de Proyectos, es necesario haber cursado previamente Economía Financiera.")
                    case 6:
                        print("La asignatura de Proyecto de Grado no presenta requisitos previos para ser cursada.")

                seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break

            case 10:
                print("Regresando al menú principal...")
                break
