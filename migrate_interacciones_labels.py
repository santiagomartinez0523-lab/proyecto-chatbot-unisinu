import sqlite3

def migrar_labels():
    conn = sqlite3.connect('chatbot_analytics.db')
    cursor = conn.cursor()
    
    # Lista de mapeos para la tabla interacciones
    mapeos = [
        # Menú Principal
        ("estado = 'menu_principal' AND mensaje_usuario = '1'", "Pensum"),
        ("estado = 'menu_principal' AND mensaje_usuario = '2'", "Matrícula"),
        ("estado = 'menu_principal' AND mensaje_usuario = '3'", "Posgrados"),
        ("estado = 'menu_principal' AND mensaje_usuario = '4'", "Cursos Inglés"),
        ("estado = 'menu_principal' AND mensaje_usuario = '5'", "Bienestar"),
        ("estado = 'menu_principal' AND mensaje_usuario = '6'", "Tutorías"),
        ("estado = 'menu_principal' AND mensaje_usuario = '7'", "Semilleros"),
        ("estado = 'menu_principal' AND mensaje_usuario = '8'", "Requisitos"),
        ("estado = 'menu_principal' AND mensaje_usuario = '9'", "Reportes"),
        
        # Selección de Programa
        ("estado = 'seleccionar_programa' AND mensaje_usuario = '1'", "Ing. Sistemas"),
        ("estado = 'seleccionar_programa' AND mensaje_usuario = '2'", "Ing. Industrial"),
        ("estado = 'seleccionar_programa' AND mensaje_usuario = '3'", "Ing. Civil"),
        ("estado = 'seleccionar_programa' AND mensaje_usuario = '4'", "Ing. Eléctrica"),
        ("estado = 'seleccionar_programa' AND mensaje_usuario = '5'", "Ing. Electromecánica"),
        
        # Selección de Bienestar
        ("estado = 'seleccionar_bienestar' AND mensaje_usuario = '1'", "Deportes"),
        ("estado = 'seleccionar_bienestar' AND mensaje_usuario = '2'", "Cultura"),
        ("estado = 'seleccionar_bienestar' AND mensaje_usuario = '3'", "Comida"),
        
        # Deportes específicos
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '1'", "Fútbol"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '2'", "Futsala"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '3'", "Taekwondo"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '4'", "Rugby"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '5'", "Pesas"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '6'", "Voleibol"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '7'", "Baloncesto"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '8'", "Softbol"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '9'", "Tenis"),
        ("estado = 'bienestar_deportes' AND mensaje_usuario = '10'", "Gimnasio"),
    ]
    
    print("Iniciando migración de etiquetas en la tabla de interacciones...")
    
    for condicion, label in mapeos:
        query = f"UPDATE interacciones SET opcion_elegida = '{label}' WHERE {condicion}"
        cursor.execute(query)
        print(f"Actualizada etiqueta: {label}")
        
    conn.commit()
    conn.close()
    print("Migración completada con éxito.")

if __name__ == "__main__":
    migrar_labels()
