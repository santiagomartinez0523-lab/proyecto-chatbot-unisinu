# bienestar_data.py
# Contiene información de Bienestar Universitario

BIENESTAR_INFO = {
    'deportes': {
        'titulo': 'Deportes',
        'info': '''🏃‍♂️ *Deportes - Bienestar Universitario*

El área de deportes ofrece diversas actividades para el desarrollo físico y recreativo de los estudiantes.

*Deportes Disponibles:*
• Fútbol  
• Futsala  
• Taekwondo  
• Rugby  
• Levantamiento de Pesas  
• Vóleybol  
• Baloncesto  
• Softbol  
• Tenis de Mesa  
• Gimnasio Multifuerza  

Escribe el deporte que deseas consultar para conocer más detalles.
''',
        'detalles': {
            '1': {
                'masculino': '''⚽ *Fútbol Masculino*
📅 Martes y viernes: 6:00 p.m. - 8:00 p.m.
👨‍🏫 Instructores: Víctor Acosta y Rafael Palma
📍 Lugar: Cancha de fútbol 8''',
                'femenino': '''⚽ *Fútbol Femenino*
📅 Lunes y miércoles: 6:00 p.m. - 8:00 p.m.
👨‍🏫 Instructores: Víctor Acosta y Rafael Palma
📍 Lugar: Cancha de fútbol 8'''
            },

            '2': '''🥅 *Futsala*
📅 Martes, jueves y viernes: 6:30 p.m. - 8:30 p.m.
👨‍🏫 Instructor: Víctor Acosta
📍 Lugar: Cancha múltiple''',

            '3': '''🥋 *Taekwondo*
📅 Lunes, miércoles y viernes: 2:00 p.m. - 4:00 p.m.
📅 Martes y jueves: 6:00 p.m. - 8:00 p.m.
📍 Lugar: Kiosco Alfa
👩‍🏫 Instructora: Alejandra Mendoza''',

            '4': '''🏉 *Rugby*
📅 Martes y jueves: 6:00 p.m. - 8:00 p.m.
👨‍🏫 Instructor: Juan Sierra
📍 Lugar: Cancha de fútbol 8''',

            '5': '''🏋️ *Levantamiento de Pesas*
📅 Lunes a viernes: 10:00 a.m. - 12:00 p.m. y 4:00 p.m. - 6:00 p.m.
👨‍🏫 Instructor: Mike Berrocal
📍 Lugar: Gimnasio''',

            '6': '''🏐 *Vóleybol (Masculino y Femenino)*
📅 Lunes, miércoles y viernes: 4:00 p.m. - 8:00 p.m.
👨‍🏫 Instructor: Pedro Olascoaga
📍 Lugar: Cancha múltiple''',

            '7': {
                'masculino': '''🏀 *Baloncesto Masculino*
📅 Martes y jueves: 4:30 p.m. - 6:30 p.m.
👨‍🏫 Instructores: Pedro Olascoaga y Juan Sierra
📍 Lugar: Cancha múltiple''',
                'femenino': '''🏀 *Baloncesto Femenino*
📅 Lunes, miércoles y jueves: horarios varios.
👨‍🏫 Instructores: Pedro Olascoaga y Juan Sierra
📍 Lugar: Cancha múltiple'''
            },

            '8': '''🥎 *Softbol*
📅 Lunes, miércoles y jueves: 4:00 p.m. - 6:00 p.m.
📅 Martes: 6:00 p.m. - 8:00 p.m.
📅 Viernes en la mañana
👨‍🏫 Instructor: José Barrios Martínez
📍 Lugares: Villa Olímpica, estadio Amín Manzur, cancha de fútbol 8''',

            '9': '''🏓 *Tenis de Mesa*
📅 Lunes a viernes: 9:00 a.m. - 11:00 a.m.
👨‍🏫 Instructor: José Barrios
📍 Lugar: Parque Líbano''',

            '10': '''🏋️‍♂️ *Gimnasio Multifuerza*
📅 Lunes a jueves: 8:00 a.m. - 12:00 p.m. / 4:00 p.m. - 8:00 p.m.
📅 Viernes: 8:00 a.m. - 12:00 p.m. / 3:00 p.m. - 7:00 p.m.
👨‍🏫 Instructor: Mike Berrocal Martínez
📍 Ubicación: Cerca del kiosco principal'''
        }
    },

    'area_cultural': {
        'titulo': 'Área Cultural',
        'info': '''🎭 *Área Cultural - Bienestar Universitario*

El área cultural promueve el desarrollo artístico y cultural de la comunidad universitaria.

*Actividades Disponibles:*
• Gaitas y Tambores  
• Grupo de Rock  
• Orquesta  
• Vallenato  
• Coro  
• Danza Moderna  
• Danza Folclórica  

Escribe la actividad que deseas consultar para conocer más detalles.
''',
        'detalles': {
            '1': '''🥁 *Gaitas y Tambores*  
👨‍🏫 Instructor: Evelio Pacheco  
📍 Lugar: Salón Omega  
🕒 Horarios:  
• Lunes y miércoles: 3:00 p.m. - 7:00 p.m.  
• Martes y viernes: 8:00 a.m. - 12:00 p.m.  
• Jueves: 5:00 p.m. - 9:00 p.m.''',

            '2': '''🎸 *Grupo de Rock*  
👨‍🏫 Instructor: Elvis Castillo  
📍 Lugar: Sala de música (Salón Omega)  
🕒 Horarios:  
• Lunes y miércoles: 4:00 p.m. - 8:00 p.m.  
• Martes y jueves: 8:00 a.m. - 12:00 p.m.  
• Viernes: 2:00 p.m. - 6:00 p.m.''',

            '3': '''🎻 *Orquesta*  
👨‍🏫 Instructor: Samir Berrocal  
📍 Lugar: Sala de música  
🕒 Horarios:  
• Lunes y jueves: 4:00 p.m. - 8:00 p.m.  
• Martes: 8:00 a.m. - 12:00 p.m. y 4:00 p.m. - 8:00 p.m.  
• Viernes: 8:00 a.m. - 12:00 p.m.''',

            '4': '''🎶 *Vallenato*  
👨‍🏫 Instructor: Camilo Cogollo  
📍 Lugar: Sala de música  
🕒 Horarios:  
• Lunes: 4:00 p.m. - 8:00 p.m.  
• Martes y viernes: 8:00 a.m. - 12:00 p.m.  
• Miércoles: 2:00 p.m. - 6:00 p.m.  
• Jueves: 3:00 p.m. - 7:00 p.m.''',

            '5': '''🎤 *Coro*  
👩‍🏫 Instructora: Dayana Parra  
📍 Lugar: Auditorio Zenú  
🕒 Horario: Jueves de 2:30 p.m. a 5:00 p.m.''',

            '6': '''💃 *Danza Moderna*  
👨‍🏫 Instructor: Enry Torres Martínez  
📍 Lugar: Gimnasio  
🕒 Horarios:  
• Lunes: 4:00 p.m. - 6:00 p.m.  
• Martes: 10:00 a.m. - 12:00 p.m.  
• Miércoles y jueves: 6:00 p.m. - 8:00 p.m.''',

            '7': '''🕺 *Danza Folclórica*  
👨‍🏫 Instructor: Enry Torres Martínez  
📍 Lugar: Gimnasio  
🕒 Horarios:  
• Lunes y miércoles: 6:00 p.m. - 8:00 p.m.  
• Martes: 8:00 a.m. - 10:00 a.m.''',
        }
    },

    'comida': {
        'titulo': 'Comida',
        'info': '''🍽️ *Servicio de Alimentación - Bienestar Universitario*

En proceso...

_Escribe *menu* para volver al inicio_'''
    }
}
