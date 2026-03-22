# requisitos_data.py
# Contiene todos los datos de requisitos de materias por programa

REQUISITOS_SISTEMAS = {
    1: {
        'nombre': 'Semestre I',
        'mensaje': '📚 *Semestre I*\n\nLas materias de primer semestre no tienen restricción.'
    },
    2: {
        'nombre': 'Semestre II',
        'materias': {
            1: ('Programación II', 'Para cursar Programación II, es requisito haber aprobado previamente Programación I.'),
            2: ('Física I y Laboratorio', 'Para cursar Física I y su laboratorio, es necesario haber aprobado previamente Cálculo Diferencial.'),
            3: ('Cálculo Integral', 'Para cursar Cálculo Integral, es necesario haber aprobado previamente Cálculo Diferencial.'),
            4: ('CCU 2', 'Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.'),
            5: ('CCU 3', 'Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.'),
            6: ('CCU 4', 'Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.')
        }
    },
    3: {
        'nombre': 'Semestre III',
        'materias': {
            1: ('Estructura de Datos', 'Para cursar la asignatura de Estructura de Datos, es necesario haber aprobado previamente Programación II.'),
            2: ('Electrónica', 'Para cursar la asignatura de Electrónica, es necesario haber cursado previamente Física I y su respectivo laboratorio.'),
            3: ('Cálculo Vectorial', 'Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral.'),
            4: ('Probabilidad y Estadística', 'Para cursar la asignatura de Probabilidad y Estadística, es necesario haber cursado previamente Cálculo Integral.'),
            5: ('CCU 5', 'Actualmente, la asignatura CCU 5 no presenta restricciones previas para ser cursada.'),
            6: ('Ética General', 'Actualmente, la asignatura de Ética General no presenta restricciones previas para ser cursada.')
        }
    },
    4: {
        'nombre': 'Semestre IV',
        'materias': {
            1: ('Análisis de Algoritmos', 'Para cursar la asignatura de Análisis de Algoritmos, es necesario haber aprobado previamente Estructura de Datos.'),
            2: ('Circuitos Digitales', 'Para cursar la asignatura de Circuitos Digitales, es necesario haber cursado previamente Electrónica.'),
            3: ('Bases de Datos', 'Para cursar la asignatura de Bases de Datos, es necesario haber aprobado previamente Estructura de Datos.'),
            4: ('Ecuaciones Diferenciales', 'Para cursar la asignatura de Ecuaciones Diferenciales, es necesario haber aprobado previamente Cálculo Vectorial.'),
            5: ('CCU 6', 'Actualmente, la asignatura CCU 6 no presenta restricciones previas para ser cursada.')
        }
    },
    5: {
        'nombre': 'Semestre V',
        'materias': {
            1: ('Administración de Bases de Datos', 'Para cursar la asignatura de Administración de Bases de Datos, es necesario haber cursado previamente Bases de Datos.'),
            2: ('Computación Móvil', 'Para cursar la asignatura de Computación Móvil, es necesario haber cursado previamente Bases de Datos.'),
            3: ('Arquitectura del Computador', 'Para cursar la asignatura de Arquitectura del Computador, es necesario haber cursado previamente Circuitos Digitales.'),
            4: ('Robótica y Laboratorio', 'Para cursar la asignatura de Robótica y su respectivo laboratorio, es necesario haber cursado previamente Circuitos Digitales.'),
            5: ('Seminario de Investigación I', 'La asignatura de Seminario I no presenta requisitos previos para ser cursada.')
        }
    },
    6: {
        'nombre': 'Semestre VI',
        'materias': {
            1: ('Sistemas Operativos', 'Para cursar la asignatura de Sistemas Operativos, es necesario haber cursado previamente Arquitectura del Computador.'),
            2: ('Sistemas de Información y Gestión Telemática', 'Para cursar la asignatura de Sistemas de Información y Gestión Telemática, es necesario haber cursado previamente Administración de Bases de Datos.'),
            3: ('Seminario de Investigación II', 'La asignatura de Seminario de Investigación II no presenta requisitos previos para ser cursada.'),
            4: ('Electiva Complementaria I', 'La asignatura de Electiva Complementaria I no presenta requisitos previos para ser cursada.')
        }
    },
    7: {
        'nombre': 'Semestre VII',
        'materias': {
            1: ('Auditoría de Sistemas', 'La asignatura de Auditoría de Sistemas no presenta requisitos previos para ser cursada.'),
            2: ('Electiva Complementaria II', 'La asignatura de Electiva Complementaria II no presenta requisitos previos para ser cursada.'),
            3: ('Ingeniería de Software', 'Para cursar la asignatura de Ingeniería de Software, es necesario haber cursado previamente Sistemas de Información y Gestión.'),
            4: ('Redes de Datos', 'Para cursar la asignatura de Redes de Datos, es necesario haber cursado previamente Telemática.'),
            5: ('Sistemas de Tiempo Real', 'Para cursar la asignatura de Sistemas de Tiempo Real, es necesario haber cursado previamente Sistemas Operativos.')
        }
    },
    8: {
        'nombre': 'Semestre VIII',
        'materias': {
            1: ('Computación Gráfica', 'Para cursar la asignatura de Computación Gráfica, es necesario haber cursado previamente Álgebra y Geometría Analítica.'),
            2: ('Programación Web', 'Para cursar la asignatura de Programación Web, es necesario haber cursado previamente Análisis de Algoritmos.'),
            3: ('Ética Profesional', 'La asignatura de Ética Profesional no presenta restricciones ni requisitos previos para ser cursada.'),
            4: ('Tecnología Informática en las Organizaciones', 'Para cursar la asignatura de Tecnología Informática en las Organizaciones, es necesario haber aprobado previamente Ingeniería de Software.'),
            5: ('Legislación para Ingenieros', 'La asignatura de Legislación para Ingenieros no presenta requisitos previos para ser cursada.'),
            6: ('Administración y Mantenimiento de Redes', 'Para cursar la asignatura de Administración y Mantenimiento de Redes, es necesario haber cursado previamente Redes de Datos.')
        }
    },
    9: {
        'nombre': 'Semestre IX',
        'materias': {
            1: ('Electiva Profesional I', 'La asignatura Electiva Profesional I no presenta restricciones ni requisitos previos para ser cursada.'),
            2: ('Electiva Profesional II', 'La asignatura Electiva Profesional II no presenta restricciones ni requisitos previos para ser cursada.'),
            3: ('Electiva Profesional III', 'La asignatura Electiva Profesional III no presenta restricciones ni requisitos previos para ser cursada.'),
            4: ('Práctica Empresarial', 'Para cursar la asignatura de Práctica Empresarial, es necesario haber cursado previamente Tecnología Informática en las Organizaciones.'),
            5: ('Opción de Grado', 'La asignatura de Opción de Grado no presenta restricciones ni requisitos previos para ser cursada.')
        }
    }
}

REQUISITOS_INDUSTRIAL = {
    1: {
        'nombre': 'Semestre I',
        'mensaje': '📚 *Semestre I*\n\nLas materias de primer semestre no tienen restricción.'
    },
    2: {
        'nombre': 'Semestre II',
        'materias': {
            1: ('Álgebra Lineal', 'Para cursar Álgebra Lineal, es necesario haber cursado previamente Álgebra y Geometría Analítica.'),
            2: ('Cálculo Diferencial', 'La asignatura de Cálculo Diferencial no presenta restricciones ni requisitos previos para ser cursada.'),
            3: ('Electiva Administrativa I', 'La asignatura de Electiva Administrativa I no presenta requisitos ni requisitos previos para ser cursada.'),
            4: ('Curso de Libre Elección', 'La asignatura de Curso de Libre Elección no presenta requisitos previos para ser cursada.'),
            5: ('CCU 1', 'Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.'),
            6: ('CCU 2', 'Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.'),
            7: ('Constitución y Sociedad', 'La asignatura de Constitución y Sociedad no presenta requisitos previos para ser cursada.')
        }
    },
    3: {
        'nombre': 'Semestre III',
        'materias': {
            1: ('Cálculo Integral', 'Para cursar Cálculo Integral, es necesario haber cursado previamente Cálculo Diferencial.'),
            2: ('Física I y Laboratorio', 'Para cursar Física I y laboratorio, es necesario haber cursado previamente Cálculo Diferencial.'),
            3: ('Programación de Computadores', 'La asignatura de Programación de Computadores no presenta requisitos previos para ser cursada.'),
            4: ('Electiva Administrativa II', 'La asignatura de Electiva Administrativa II no presenta requisitos previos para ser cursada.'),
            5: ('CCU 3', 'Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.'),
            6: ('CCU 4', 'Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.')
        }
    },
    4: {
        'nombre': 'Semestre IV',
        'materias': {
            1: ('Estadística Descriptiva y Probabilidad', 'Para cursar Estadística Descriptiva y Probabilidad, es necesario haber cursado previamente Cálculo Integral.'),
            2: ('Cálculo Vectorial', 'Para cursar Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral.'),
            3: ('Física II y Laboratorio', 'Para cursar Física II y laboratorio, es necesario haber aprobado previamente Física I y laboratorio, así como Cálculo Integral.'),
            4: ('Materiales de Ingeniería', 'Para cursar Materiales de Ingeniería, es necesario haber aprobado previamente Química Básica.'),
            5: ('Procesos Industriales', 'Para cursar Procesos Industriales, es necesario haber aprobado previamente Química Básica, así como Física I y laboratorio.')
        }
    },
    5: {
        'nombre': 'Semestre V',
        'materias': {
            1: ('Ecuaciones Diferenciales', 'Para cursar Ecuaciones Diferenciales, es necesario haber cursado previamente Cálculo Vectorial.'),
            2: ('Estadística Inferencial', 'Para cursar Estadística Inferencial, es necesario haber cursado previamente Estadística Descriptiva y Probabilidad.'),
            3: ('Ingeniería de Métodos y Trabajo', 'Para cursar Ingeniería de Métodos y Trabajo, es necesario haber cursado previamente Estadística Descriptiva y Probabilidad.'),
            4: ('Diseño de Producto', 'Para cursar Diseño de Producto, es necesario haber cursado previamente Materiales de Ingeniería y Procesos Industriales.'),
            5: ('Calidad I', 'Para cursar Calidad I, es necesario haber cursado previamente Estadística Descriptiva y Probabilidad.'),
            6: ('Electiva Financiera I', 'La asignatura de Electiva Financiera I no presenta requisitos previos para ser cursada.')
        }
    },
    6: {
        'nombre': 'Semestre VI',
        'materias': {
            1: ('Métodos Numéricos', 'Para cursar Métodos Numéricos, es necesario haber cursado previamente Ecuaciones Diferenciales.'),
            2: ('Modelos Lineales', 'Para cursar Modelos Lineales, es necesario haber cursado previamente Estadística Inferencial.'),
            3: ('Investigación de Operaciones I', 'Para cursar Investigación de Operaciones I, es necesario haber cursado previamente Álgebra Lineal y Estadística Descriptiva y Probabilidad.'),
            4: ('Calidad II', 'Para cursar Calidad II, es necesario haber cursado previamente Calidad I y la asignatura de Ingeniería de Métodos y Trabajo.'),
            5: ('Sistema de Producción I', 'Para cursar Sistema de Producción I, es necesario haber cursado previamente Procesos Industriales.'),
            6: ('Electiva Administrativa III', 'La asignatura de Electiva Administrativa III no presenta requisitos previos para ser cursada.')
        }
    },
    7: {
        'nombre': 'Semestre VII',
        'materias': {
            1: ('Seminario de Investigación II', 'La asignatura de Seminario de Investigación II no presenta requisitos previos para ser cursada.'),
            2: ('Investigación de Operaciones II', 'Para cursar Investigación de Operaciones II, es necesario haber cursado previamente Investigación de Operaciones I.'),
            3: ('Sistemas de Producción II', 'Para cursar Sistemas de Producción II, es necesario haber cursado previamente Sistemas de Producción I.'),
            4: ('Electiva de Profundización I', 'La asignatura de Electiva de Profundización I no presenta requisitos previos para ser cursada.'),
            5: ('Seguridad y Salud en el Trabajo', 'Para cursar Seguridad y Salud en el Trabajo, es necesario haber cursado previamente Calidad II.'),
            6: ('Sistemas Avanzados de Manufactura', 'Para cursar Sistemas Avanzados de Manufactura, es necesario haber cursado previamente Sistemas de Producción I.'),
            7: ('Electiva Financiera II', 'La asignatura de Electiva Financiera II no presenta requisitos previos para ser cursada.')
        }
    },
    8: {
        'nombre': 'Semestre VIII',
        'materias': {
            1: ('Investigación de Operaciones III', 'Para cursar Investigación de Operaciones III, es necesario haber cursado previamente Métodos Numéricos e Investigación de Operaciones II.'),
            2: ('Formulación y Evaluación de Proyectos de Ingeniería', 'La asignatura de Formulación y Evaluación de Proyectos de Ingeniería no presenta requisitos previos para ser cursada.'),
            3: ('Logística I', 'Para cursar Logística I, es necesario haber cursado previamente Sistemas de Producción II.'),
            4: ('Electiva de Profundización II', 'La asignatura de Electiva de Profundización II no presenta requisitos previos para ser cursada.'),
            5: ('Fundamentos de Ingeniería Ambiental', 'Para cursar Fundamentos de Ingeniería Ambiental, es necesario haber cursado previamente Calidad II.'),
            6: ('Electiva Financiera III', 'La asignatura de Electiva Financiera III no presenta requisitos previos para ser cursada.')
        }
    },
    9: {
        'nombre': 'Semestre IX',
        'materias': {
            1: ('Legislación de Ingenierías', 'La asignatura de Legislación de Ingenierías no presenta restricciones ni requisitos previos para ser cursada.'),
            2: ('Proyecto de Grado', 'La asignatura de Proyecto de Grado no presenta restricciones ni requisitos previos para ser cursada.'),
            3: ('Simulación', 'Para cursar Simulación, es necesario haber cursado previamente Investigación de Operaciones III.'),
            4: ('Logística II', 'Para cursar Logística II, es necesario haber cursado previamente Logística I.'),
            5: ('Electiva de Profundización III', 'La asignatura de Electiva de Profundización III no presenta requisitos previos para ser cursada.'),
            6: ('Distribución de Plantas', 'Para cursar Distribución de Plantas, es necesario haber cursado previamente Sistemas de Producción II.')
        }
    }
}

REQUISITOS_CIVIL = {
    1: {
        'nombre': 'Semestre I',
        'mensaje': '📚 *Semestre I*\n\nLas materias de primer semestre no tienen restricción.'
    },
    2: {
        'nombre': 'Semestre II',
        'materias': {
            1: ('Constitución y Sociedad', 'La asignatura de Constitución y Sociedad no presenta requisitos previos para ser cursada.'),
            2: ('Ética y Convivencia Ciudadana', 'La asignatura de Ética y Convivencia Ciudadana no presenta requisitos previos para ser cursada.'),
            3: ('Física I y Laboratorio', 'Para cursar la asignatura de Física I y Laboratorio, es necesario haber cursado previamente Cálculo Diferencial.'),
            4: ('Investigación en Ingeniería', 'La asignatura de Investigación en Ingeniería no presenta requisitos previos para ser cursada.'),
            5: ('Álgebra Lineal', 'Para cursar la asignatura de Álgebra Lineal, es necesario haber cursado previamente Álgebra y Geometría Analítica.'),
            6: ('Cálculo Integral', 'Para cursar la asignatura de Cálculo Integral, es necesario haber cursado previamente Cálculo Diferencial.')
        }
    },
    3: {
        'nombre': 'Semestre III',
        'materias': {
            1: ('Física II y Laboratorio', 'Para cursar la asignatura de Física II y su respectivo laboratorio, es necesario haber cursado previamente Física I y laboratorio y Cálculo Integral.'),
            2: ('Topografía y Práctica', 'Para cursar la asignatura de Topografía y su práctica, es necesario haber cursado previamente Dibujo de Ingeniería.'),
            3: ('Estática', 'Para cursar la asignatura de Estática, es necesario haber cursado previamente Física I y laboratorio.'),
            4: ('Cálculo Vectorial', 'Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral.'),
            5: ('Química Básica', 'La asignatura de Química Básica no presenta requisitos previos para ser cursada.')
        }
    },
    4: {
        'nombre': 'Semestre IV',
        'materias': {
            1: ('Física III y Laboratorio', 'Para cursar la asignatura de Física III y laboratorio, es necesario haber aprobado previamente Física II y laboratorio, y cursarla de manera simultánea con la asignatura de Ecuaciones Diferenciales.'),
            2: ('Sistema de Información Geográfica', 'Para cursar la asignatura de Sistema de Información Geográfica, es necesario haber cursado previamente Topografía y su práctica.'),
            3: ('Resistencia de Materiales', 'Para cursar la asignatura de Resistencia de Materiales, es necesario haber cursado previamente Estática.'),
            4: ('Programación de Computadores I', 'La asignatura de Programación de Computadores I no presenta requisitos previos para ser cursada.'),
            5: ('Ecuaciones Diferenciales', 'Para cursar la asignatura de Ecuaciones Diferenciales, es necesario haber aprobado previamente Cálculo Vectorial y cursarla de manera simultánea con la asignatura de Física III y laboratorio.')
        }
    },
    5: {
        'nombre': 'Semestre V',
        'materias': {
            1: ('Análisis Estructural', 'Para cursar la asignatura de Análisis Estructural, es necesario haber cursado previamente Resistencia de Materiales.'),
            2: ('Geología', 'Para cursar la asignatura de Geología, es necesario haber cursado previamente Química Básica.'),
            3: ('Mecánica de Fluidos', 'Para cursar la asignatura de Mecánica de Fluidos, es necesario haber cursado previamente Física I y laboratorio.'),
            4: ('Probabilidad y Estadística', 'Para cursar la asignatura de Probabilidad y Estadística, es necesario haber cursado previamente Cálculo Integral.'),
            5: ('Métodos Numéricos', 'Para cursar la asignatura de Métodos Numéricos, es necesario haber cursado previamente Ecuaciones Diferenciales.')
        }
    },
    6: {
        'nombre': 'Semestre VI',
        'mensaje': '⚙️ *Semestre VI*\n\nEn proceso...'
    },
    7: {
        'nombre': 'Semestre VII',
        'mensaje': '⚙️ *Semestre VII*\n\nEn proceso...'
    },
    8: {
        'nombre': 'Semestre VIII',
        'mensaje': '⚙️ *Semestre VIII*\n\nEn proceso...'
    },
    9: {
        'nombre': 'Semestre IX',
        'mensaje': '⚙️ *Semestre IX*\n\nEn proceso...'
    }
}

REQUISITOS_ELECTRICA = {
    1: {
        "nombre": "Semestre I",
        "materias": {
            1: ("Materias de primer semestre", "Las materias de primer semestre no tienen restricción.")
        }
    },
    2: {
        "nombre": "Semestre II",
        "materias": {
            1: ("Álgebra Lineal", "Para cursar la asignatura de Álgebra Lineal, es necesario haber cursado previamente Álgebra y Geometría Analítica."),
            2: ("Cálculo Integral", "Para cursar la asignatura de Cálculo Integral, es necesario haber cursado previamente Cálculo Diferencial."),
            3: ("Física I y Laboratorio", "Para cursar la asignatura de Física I y laboratorio, es necesario haber cursado previamente Cálculo Diferencial."),
            4: ("Programación de Computadores", "La asignatura de Programación de Computadores no presenta requisitos previos para ser cursada."),
            5: ("Ética y Convivencia Ciudadana", "La asignatura de Ética y Convivencia Ciudadana no presenta requisitos previos para ser cursada."),
            6: ("CCU", "Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas.")
        }
    },
    3: {
        "nombre": "Semestre III",
        "materias": {
            1: ("Cálculo Vectorial", "Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral."),
            2: ("Circuitos Eléctricos I y Laboratorio", "Para cursar la asignatura de Circuitos Eléctricos I y su respectivo laboratorio, es necesario haber cursado previamente Álgebra y Geometría Analítica."),
            3: ("Física II y Laboratorio", "Para cursar la asignatura de Física II y laboratorio, es necesario haber cursado previamente Física I y laboratorio."),
            4: ("Seminario de Investigación I", "La asignatura de Seminario de Investigación I no presenta requisitos previos para ser cursada."),
            5: ("CCU", "Actualmente, las asignaturas CCU no presentan requisitos previos para ser cursadas."),
            6: ("Termodinámica", "Para cursar la asignatura de Termodinámica, es necesario haber cursado previamente Física I y laboratorio.")
        }
    },
    4: {
        "nombre": "Semestre IV",
        "materias": {
            1: ("Ecuaciones Diferenciales", "Para cursar la asignatura de Ecuaciones Diferenciales, es necesario haber cursado previamente Cálculo Vectorial."),
            2: ("Física III y Laboratorio", "Para cursar la asignatura de Física III y laboratorio, es necesario haber cursado previamente Física II y laboratorio."),
            3: ("Circuitos Eléctricos II y Laboratorio", "Para cursar la asignatura de Circuitos Eléctricos II y laboratorio, es necesario haber cursado previamente Circuitos Eléctricos I y laboratorio."),
            4: ("Curso de Libre Elección", "La asignatura de Curso de Libre Elección no presenta requisitos previos para ser cursada."),
            5: ("Probabilidad y Estadística", "Para cursar la asignatura de Probabilidad y Estadística, es necesario haber aprobado previamente Cálculo Integral.")
        }
    },
    5: {
        "nombre": "Semestre V",
        "materias": {
            1: ("Métodos Numéricos", "Para cursar la asignatura de Métodos Numéricos, es necesario haber cursado previamente Ecuaciones Diferenciales."),
            2: ("Teoría Electromagnética", "Para cursar la asignatura de Teoría Electromagnética, es necesario haber cursado previamente Física II y su respectivo laboratorio."),
            3: ("Medidas Eléctricas", "La asignatura de Medidas Eléctricas no presenta requisitos previos para ser cursada."),
            4: ("Electiva Complementaria", "La asignatura de Electiva Complementaria no presenta requisitos previos para ser cursada."),
            5: ("Seminario de Investigación II", "La asignatura de Seminario de Investigacion II no presenta requisitos previos para ser cursada."),
            6: ("Análisis de Sistemas", "La asignatura de Analisis de Sistemas no presenta requisitos previos para ser cursada.")
        }
    },
    6: {
        "nombre": "Semestre VI",
        "materias": {
            1: ("Accionamientos Eléctricos y Laboratorio", "La asignatura de Accionamientos Eléctricos y su respectivo laboratorio no presenta requisitos previos para ser cursada."),
            2: ("Ingeniería de Control y Laboratorio", "La asignatura de Ingeniería de Control y Lab no presenta requisitos previos para ser cursada."),
            3: ("Instalaciones Eléctricas", "La asignatura de Instalaciones Eléctricas no presenta requisitos previos para ser cursada."),
            4: ("Máquinas Eléctricas I y Laboratorio", "Para cursar la asignatura de Máquinas Eléctricas I y laboratorio, es necesario haber cursado previamente Teoría Electromagnética."),
            5: ("Instrumentación Industrial Moderna", "La asignatura de Instrumentación Industrial Moderna no presenta requisitos previos para ser cursada."),
            6: ("Electrónica General y Laboratorio", "Para cursar la asignatura de Electrónica General y laboratorio, es necesario haber cursado previamente Circuitos Eléctricos I y laboratorio.")
        }
    },
    7: {
        "nombre": "Semestre VII",
        "materias": {
            1: ("Generación Térmica", "Para cursar la asignatura de Generación Térmica, es necesario haber cursado previamente Termodinámica."),
            2: ("Electiva Profesional I", "La asignatura de Electiva Profesional I no presenta requisitos previos para ser cursada."),
            3: ("Electrónica Digital y Laboratorio", "Para cursar la asignatura de Electrónica Digital y laboratorio, es necesario haber cursado previamente Electrónica General y laboratorio."),
            4: ("Máquinas Eléctricas II y Laboratorio", "Para cursar la asignatura de Máquinas Eléctricas II y laboratorio, es necesario haber cursado previamente Máquinas Eléctricas I y laboratorio."),
            5: ("Sistemas de Distribución de Energía", "Para cursar la asignatura de Sistemas de Distribución de Energía, es necesario haber cursado previamente Instalaciones Eléctricas.")
        }
    },
    8: {
        "nombre": "Semestre VIII",
        "materias": {
            1: ("Análisis de Sistemas de Potencia", "Para cursar la asignatura de Análisis de Sistemas de Potencia, es necesario haber cursado previamente Máquinas Eléctricas I y su respectivo laboratorio."),
            2: ("Electiva Profesional II", "La asignatura de Electiva Profesional II no presenta requisitos previos para ser cursada."),
            3: ("Subestaciones Eléctricas", "Para cursar la asignatura de Subestaciones Eléctricas, es necesario haber cursado previamente Sistemas de Distribución de Energía."),
            4: ("Generación Hidráulica", "La asignatura de Generación Hidráulica no presenta requisitos previos para ser cursada."),
            5: ("Economía Financiera", "Para cursar la asignatura de Economía Financiera, es necesario haber cursado previamente Cálculo Diferencial."),
            6: ("Fundamentos de Administración", "La asignatura de Fundamentos de Administración no presenta requisitos previos para ser cursada.")
        }
    },
    9: {
        "nombre": "Semestre IX",
        "materias": {
            1: ("Electiva Profesional III", "La asignatura de Electiva Profesional III no presenta requisitos previos para ser cursada."),
            2: ("Líneas de Transmisión Eléctrica", "Para cursar la asignatura de Líneas de Transmisión Eléctrica, es necesario haber cursado previamente Teoría Electromagnética."),
            3: ("Protección de Sistemas de Potencia", "Para cursar la asignatura de Protección de Sistemas de Potencia, es necesario haber cursado previamente Análisis de Sistemas de Potencia."),
            4: ("Tecnología de Alta Tensión", "Para cursar la asignatura de Tecnología de Alta Tensión, es necesario haber cursado previamente Análisis de Sistemas de Potencia."),
            5: ("Formulación y Evaluación de Proyectos", "Para cursar la asignatura de Formulación y Evaluación de Proyectos, es necesario haber cursado previamente Economía Financiera."),
            6: ("Proyecto de Grado", "La asignatura de Proyecto de Grado no presenta requisitos previos para ser cursada.")
        }
    }
}

REQUISITOS_ELECTROMECANICA = {
    1: {
        "nombre": "Semestre I",
        "materias": {
            1: ("Materias de primer semestre", "Las materias de primer semestre no tienen restricción.")
        }
    },
    2: {
        "nombre": "Semestre II",
        "materias": {
            1: ("Cálculo Diferencial", "Para cursar la asignatura de Cálculo Diferencial, es necesario haber cursado previamente Precálculo."),
            2: ("Álgebra Lineal", "La asignatura de Álgebra Lineal no presenta requisitos previos para ser cursada."),
            3: ("Materiales de Ingeniería", "Para cursar la asignatura de Materiales de Ingeniería, es necesario haber cursado previamente Química Básica."),
            4: ("Dibujo Electromecánico", "La asignatura de Dibujo Electromecánico no presenta requisitos previos para ser cursada."),
            5: ("Gestión Financiera y Administrativa", "La asignatura de Gestión Financiera y Administrativa no presenta requisitos previos para ser cursada."),
            6: ("FH II", "La asignatura de FH II no presenta requisitos previos para ser cursada.")
        }
    },
    3: {
        "nombre": "Semestre III",
        "materias": {
            1: ("Cálculo Integral", "Para cursar la asignatura de Cálculo Integral, es necesario haber cursado previamente Cálculo Diferencial."),
            2: ("Física Newtoniana y Laboratorio", "Para cursar la asignatura de Física Newtoniana y su respectivo laboratorio, es necesario haber cursado previamente Cálculo Diferencial."),
            3: ("Probabilidad y Estadística", "La asignatura de Probabilidad y Estadística no presenta requisitos previos para ser cursada."),
            4: ("Estática", "Para cursar la asignatura de Estática, es necesario haber cursado previamente Materiales de Ingeniería."),
            5: ("Circuitos Eléctricos I y Laboratorio", "La asignatura de Circuitos Eléctricos I y su respectivo laboratorio no presenta requisitos previos para ser cursada."),
            6: ("FH III", "La asignatura de FH III no presenta requisitos previos para ser cursada.")
        }
    },
    4: {
        "nombre": "Semestre IV",
        "materias": {
            1: ("Cálculo Vectorial", "Para cursar la asignatura de Cálculo Vectorial, es necesario haber cursado previamente Cálculo Integral."),
            2: ("Física Electromagnética y Laboratorio", "Para cursar la asignatura de Física Electromagnética y laboratorio, es necesario haber cursado previamente Física Newtoniana y laboratorio."),
            3: ("Modelos Lineales", "Para cursar la asignatura de Modelos Lineales, es necesario haber cursado previamente Probabilidad y Estadística."),
            4: ("Dinámica", "Para cursar la asignatura de Dinámica, es necesario haber cursado previamente Estática."),
            5: ("Circuitos Eléctricos II y Laboratorio", "Para cursar la asignatura de Circuitos Eléctricos II y laboratorio, es necesario haber cursado previamente Circuitos Eléctricos I y laboratorio."),
            6: ("FH VI", "La asignatura de FH VI no presenta requisitos previos para ser cursada.")
        }
    },
    5: {
        "nombre": "Semestre V",
        "materias": {
            1: ("Métodos Numéricos", "Para cursar la asignatura de Métodos Numéricos, es necesario haber cursado previamente Cálculo Vectorial."),
            2: ("Ecuaciones Diferenciales", "La asignatura de Ecuaciones Diferenciales debe cursarse de manera simultánea con la asignatura de Métodos Numéricos."),
            3: ("Termofluidos de Ingeniería I", "La asignatura de Termofluidos de Ingeniería I no presenta requisitos previos para ser cursada."),
            4: ("Resistencia de Materiales", "Para cursar la asignatura de Resistencia de Materiales, es necesario haber cursado previamente Dinámica."),
            5: ("Teoría Electromagnética", "Para cursar la asignatura de Teoría Electromagnética, es necesario haber cursado previamente Física Electromagnética y laboratorio."),
            6: ("FH V", "La asignatura de FH V no presenta requisitos previos para ser cursada.")
        }
    },
    6: {
        "nombre": "Semestre VI",
        "materias": {
            1: ("Termofluidos de Ingeniería II", "Para cursar la asignatura de Termofluidos de Ingeniería II, es necesario haber cursado previamente Termofluidos de Ingeniería I."),
            2: ("Ingeniería de Fluidos", "Para cursar la asignatura de Ingeniería de Fluidos, es necesario haber cursado previamente Termofluidos de Ingeniería I."),
            3: ("Modelamiento y Simulación de Sistemas Electromecánicos", "La asignatura de Modelamiento y Simulación de Sistemas Electromecánicos no presenta requisitos previos para ser cursada."),
            4: ("Máquinas Eléctricas I", "Para cursar la asignatura de Máquinas Eléctricas I, es necesario haber cursado previamente Circuitos Eléctricos II y laboratorio."),
            5: ("Ingeniería de Mecanismos y Diseño de Máquinas", "Para cursar la asignatura de Ingeniería de Mecanismos y Diseño de Máquinas, es necesario haber cursado previamente Resistencia de Materiales."),
            6: ("Electrónica y Fundamentos de Control", "La asignatura de Electrónica y Fundamentos de Control no presenta requisitos previos para ser cursada.")
        }
    },
    7: {
        "nombre": "Semestre VII",
        "materias": {
            1: ("Proyectos de Ingeniería", "La asignatura de Proyectos de Ingeniería no presenta restricciones ni requisitos previos para ser cursada."),
            2: ("Transferencia de Calor", "Para cursar la asignatura de Transferencia de Calor, es necesario haber cursado previamente Termofluidos de Ingeniería II."),
            3: ("Innovación en Mecanizado Avanzado", "Para cursar la asignatura de Innovación en Mecanizado Avanzado, es necesario haber cursado previamente Modelamiento y Simulación de Sistemas Electromecánicos."),
            4: ("Máquinas Eléctricas II", "Para cursar la asignatura de Máquinas Eléctricas II, es necesario haber cursado previamente Máquinas Eléctricas I."),
            5: ("Generación Hidráulica", "Para cursar la asignatura de Generación Hidráulica, es necesario haber cursado previamente Ingeniería de Fluidos."),
            6: ("Mantenimiento de Sistemas Electromecánicos", "La asignatura de Mantenimiento de Sistemas Electromecánicos no presenta requisitos previos para ser cursada."),
            7: ("FH VI", "La asignatura de FH VI no presenta restricciones ni requisitos previos para ser cursada.")
        }
    },
    8: {
        "nombre": "Semestre VIII",
        "materias": {
            1: ("Seminario de Investigación", "Para cursar la asignatura de Seminario de Investigación, es necesario haber cursado previamente Proyectos de Ingeniería."),
            2: ("Electiva Profesional I", "La asignatura de Electiva Profesional I no presenta restricciones ni requisitos previos para ser cursada."),
            3: ("Prototipado y Manufactura Inteligente", "Para cursar la asignatura de Prototipado y Manufactura Inteligente, es necesario haber cursado previamente Innovación en Mecanizado Avanzado."),
            4: ("Sistemas Eléctricos de Potencia", "Para cursar la asignatura de Sistemas Eléctricos de Potencia, es necesario haber cursado previamente Máquinas Eléctricas I."),
            5: ("Sistemas Hidroneumáticos", "Para cursar la asignatura de Sistemas Hidroneumáticos, es necesario haber cursado previamente Generación Hidráulica."),
            6: ("Metrología e Instrumentación", "Para cursar la asignatura de Metrología e Instrumentación, es necesario haber cursado previamente Electrónica y Fundamentos de Control.")
        }
    },
    9: {
        "nombre": "Semestre IX",
        "materias": {
            1: ("Opción de Grado", "Para cursar la asignatura de Opción de Grado, es necesario haber cursado previamente Seminario de Investigación."),
            2: ("Electiva Profesional II", "La asignatura de Electiva Profesional II no presenta requisitos previos para ser cursada."),
            3: ("Práctica Profesional", "Para cursar la asignatura de Práctica Profesional, es necesario haber cursado previamente Prototipado y Manufactura Inteligente."),
            4: ("Ética Profesional", "La asignatura de Ética Profesional no presenta requisitos previos para ser cursada.")
        }
    }
}
