from numero import pedir_numero

def funcion_industrial():
    while True:
        print("\nSeleccione el semestre de Ingeniería Industrial que desea consultar:")
        print("1. Semestre I")
        print("2. Semestre II")
        print("3. Semestre III")
        print("4. Semestre IV")
        print("5. Semestre V")
        print("6. Semestre VI")
        print("7. Semestre VII")
        print("8. Semestre VIII")
        print("9. Semestre IX")
        print("10. Regresar al menú principal")

        semestre = pedir_numero("Ingrese el semestre: ", opciones_validas=list(range(1,11)))

        match semestre:
            case 1:
                print("\nLas materias que sean de primer semestre no tienen ningún tipo de restricción.")
                seguir = pedir_numero("¿Deseas buscar otra materia? (1=Sí, 2=No): ", opciones_validas=[1,2])
                if seguir == 2:
                    break
            case 2:
                while True:
                    print("\nMaterias disponibles en Semestre II:")
                    print("1. Álgebra Lineal\n2. Cálculo Diferencial\n3. Electiva Administrativa I\n4. Curso de Libre Elección\n5. CCU 1\n6. CCU 2\n7. Constitución y Sociedad")
                    materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6,7])

                    match materia:
                        case 1:
                            print("Para cursar la asignatura de Álgebra Lineal, es necesario haber cursado previamente Álgebra y Geometría Analítica.")
                        case 2:
                            print("La asignatura de Cálculo Diferencial no presenta restricciones ni requisitos previos para ser cursada.")
                        case 3:
                            print("La asignatura de Electiva Administrativa I no presenta restricciones ni requisitos previos para ser cursada.")
                        case 4:
                            print("La asignatura de Curso de Libre Elección no presenta requisitos previos para ser cursada.")
                        case 5 | 6:
                            print("Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.")
                        case 7:
                            print("La asignatura de Constitución y Sociedad no presenta requisitos previos para ser cursada.")

                    seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                    if seguir == 2:
                        break
            case 3:
                while True:
                    print("\nMaterias disponibles en Semestre III:")
                    print("1. Cálculo Integral\n2. Física I y Laboratorio\n3. Programación de Computadores\n4. Electiva Administrativa II\n5. CCU 3\n6. CCU 4")
                    materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                    match materia:
                        case 1:
                            print("Para cursar la asignatura de Cálculo Integral, es necesario haber cursado previamente Cálculo Diferencial.")
                        case 2:
                            print("Para cursar la asignatura de Física I y laboratorio, es necesario haber cursado previamente Cálculo Diferencial.")
                        case 3:
                            print("La asignatura de Programación de Computadores no presenta requisitos previos para ser cursada.")
                        case 4:
                            print("La asignatura de Electiva Administrativa II no presenta requisitos previos para ser cursada.")
                        case 5 | 6:
                            print("Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.")

                    seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                    if seguir == 2:
                        break
            case 4:
                while True:
                    print("\nMaterias disponibles en Semestre IV:")
                    print("1. Estadística Descriptiva y Probabilidad\n2. Cálculo Vectorial\n3. Física II y Laboratorio\n4. Materiales de Ingeniería\n5. Procesos Industriales")
                    materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5])

                    match materia:
                        case 1:
                            print("Para cursar la asignatura de Estadística Descriptiva y Probabilidad, es necesario haber cursado previamente Cálculo Integral.")
                        case 2:
                            print("Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral.")
                        case 3:
                            print("Para cursar la asignatura de Física II y laboratorio, es necesario haber aprobado previamente Física I y laboratorio, así como Cálculo Integral.")
                        case 4:
                            print("Para cursar la asignatura de Materiales de Ingeniería, es necesario haber aprobado previamente Química Básica.")
                        case 5:
                            print("Para cursar la asignatura de Procesos Industriales, es necesario haber aprobado previamente Química Básica, así como Física I y laboratorio.")

                    seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                    if seguir == 2:
                        break
            case 5:
                while True:
                    print("\nMaterias disponibles en Semestre V:")
                    print("1. Ecuaciones Diferenciales\n2. Estadística Inferencial\n3. Ingeniería de Métodos y Trabajo\n4. Diseño de Producto\n5. Calidad I\n6. Electiva Financiera I")
                    materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                    match materia:
                        case 1:
                            print("Para cursar la asignatura de Ecuaciones Diferenciales, es necesario haber cursado previamente Cálculo Vectorial.")
                        case 2:
                            print("Para cursar la asignatura de Estadística Inferencial, es necesario haber cursado previamente Estadística Descriptiva y Probabilidad.")
                        case 3:
                            print("Para cursar la asignatura de Ingeniería de Métodos y Trabajo, es necesario haber cursado previamente Estadística Descriptiva y Probabilidad.")
                        case 4:
                            print("Para cursar la asignatura de Diseño de Producto, es necesario haber cursado previamente Materiales de Ingeniería y Procesos Industriales.")
                        case 5:
                            print("Para cursar la asignatura de Calidad I, es necesario haber cursado previamente Estadística Descriptiva y Probabilidad.")
                        case 6:
                            print("La asignatura de Electiva Financiera I no presenta requisitos previos para ser cursada.")

                    seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                    if seguir == 2:
                        break
            case 6:
                while True:
                    print("\nMaterias disponibles en Semestre VI:")
                    print("1. Métodos Numéricos\n2. Modelos Lineales\n3. Investigación de Operaciones I\n4. Calidad II\n5. Sistema de Producción I\n6. Electiva Administrativa III")
                    materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                    match materia:
                        case 1:
                            print("Para cursar la asignatura de Métodos Numéricos, es necesario haber cursado previamente Ecuaciones Diferenciales.")
                        case 2:
                            print("Para cursar la asignatura de Modelos Lineales, es necesario haber cursado previamente Estadística Inferencial.")
                        case 3:
                            print("Para cursar la asignatura de Investigación de Operaciones I, es necesario haber cursado previamente Álgebra Lineal, Estadística Descriptiva y Probabilidad.")
                        case 4:
                            print("Para cursar la asignatura de Calidad II, es necesario haber cursado previamente Calidad I y la asignatura de Ingeniería de Métodos y Trabajo.")
                        case 5:
                            print("Para cursar la asignatura de Sistema de Producción I, es necesario haber cursado previamente Procesos Industriales.")
                        case 6:
                            print("La asignatura de Electiva Administrativa III no presenta requisitos previos para ser cursada.")

                    seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                    if seguir == 2:
                        break
            case 7:
                while True:
                    print("\nMaterias disponibles en Semestre VII:")
                    print("1. Seminario de Investigación II\n2. Investigación de Operaciones II\n3. Sistemas de Producción II\n4. Electiva de Profundización I\n5. Seguridad y Salud en el Trabajo\n6. Sistemas Avanzados de Manufactura\n7. Electiva Financiera II")
                    materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6,7])

                    match materia:
                        case 1:
                            print("La asignatura de Seminario de Investigación II no presenta requisitos previos para ser cursada.")
                        case 2:
                            print("Para cursar la asignatura de Investigación de Operaciones II, es necesario haber cursado previamente Investigación de Operaciones I.")
                        case 3:
                            print("Para cursar la asignatura de Sistemas de Producción II, es necesario haber cursado previamente Sistemas de Producción I.")
                        case 4:
                            print("La asignatura de Electiva de Profundización I no presenta requisitos previos para ser cursada.")
                        case 5:
                            print("Para cursar la asignatura de Seguridad y Salud en el Trabajo, es necesario haber cursado previamente Calidad II.")
                        case 6:
                            print("Para cursar la asignatura de Sistemas Avanzados de Manufactura, es necesario haber cursado previamente Sistemas de Producción I.")
                        case 7:
                            print("La asignatura de Electiva Financiera II no presenta requisitos previos para ser cursada.")

                    seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                    if seguir == 2:
                        break
            case 8:
                while True:
                    print("\nMaterias disponibles en Semestre VIII:")
                    print("1. Investigación de Operaciones III\n2. Formulación y Evaluación de Proyectos de Ingeniería\n3. Logística I\n4. Electiva de Profundización II\n5. Fundamentos de Ingeniería Ambiental\n6. Electiva Financiera III")
                    materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                    match materia:
                        case 1:
                            print("Para cursar la asignatura de Investigación de Operaciones III, es necesario haber cursado previamente Métodos Numéricos e Investigación de Operaciones II.")
                        case 2:
                            print("La asignatura de Formulación y Evaluación de Proyectos de Ingeniería no presenta requisitos previos para ser cursada.")
                        case 3:
                            print("Para cursar la asignatura de Logística I, es necesario haber cursado previamente Sistemas de Producción II.")
                        case 4:
                            print("La asignatura de Electiva de Profundización II no presenta requisitos previos para ser cursada.")
                        case 5:
                            print("Para cursar la asignatura de Fundamentos de Ingeniería Ambiental, es necesario haber cursado previamente Calidad II.")
                        case 6:
                            print("La asignatura de Electiva Financiera III no presenta requisitos previos para ser cursada.")

                    seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                    if seguir == 2:
                        break
            case 9:
                while True:
                    print("\nMaterias disponibles en Semestre IX:")
                    print("1. Legislación de Ingenierías\n2. Proyecto de Grado\n3. Simulación\n4. Logística II\n5. Electiva de Profundización III\n6. Distribución de Plantas")
                    materia = pedir_numero("Seleccione la materia: ", opciones_validas=[1,2,3,4,5,6])

                    match materia:
                        case 1:
                            print("La asignatura de Legislación de Ingenierías no presenta restricciones ni requisitos previos para ser cursada.")
                        case 2:
                            print("La asignatura de Proyecto de Grado no presenta restricciones ni requisitos previos para ser cursada.")
                        case 3:
                            print("Para cursar la asignatura de Simulación, es necesario haber cursado previamente Investigación de Operaciones III.")
                        case 4:
                            print("Para cursar la asignatura de Logística II, es necesario haber cursado previamente Logística I.")
                        case 5:
                            print("La asignatura de Electiva de Profundización III no presenta requisitos previos para ser cursada.")
                        case 6:
                            print("Para cursar la asignatura de Distribución de Plantas, es necesario haber cursado previamente Sistemas de Producción II.")

                    seguir = pedir_numero("¿Desea conocer otra asignatura? (1=Sí, 2=No): ", opciones_validas=[1,2])
                    if seguir == 2:
                        break

            case 10:
                print("Regresando al menú principal...")
                break
