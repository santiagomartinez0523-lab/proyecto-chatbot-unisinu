# requisitos_data.py
# Prerrequisitos de materias por programa y semestre

REQUISITOS_SISTEMAS = {
    1: [
        {'nombre': 'Programación I', 'requisito': 'Ninguno'},
        {'nombre': 'Cálculo Diferencial', 'requisito': 'Ninguno'},
        {'nombre': 'Álgebra y Geometría Analítica', 'requisito': 'Ninguno'},
    ],
    2: [
        {'nombre': 'Programación II', 'requisito': 'Programación I'},
        {'nombre': 'Cálculo Integral', 'requisito': 'Cálculo Diferencial'},
        {'nombre': 'Física I y Laboratorio', 'requisito': 'Cálculo Diferencial'},
    ],
    # ... (esto es una versión resumida para el ejemplo, 
    # en el archivo real están todos los semestres)
}

# (Siguen las estructuras para los demás programas)
REQUISITOS_INDUSTRIAL = {}
REQUISITOS_CIVIL = {}
REQUISITOS_ELECTRICA = {}
REQUISITOS_ELECTROMECANICA = {}
