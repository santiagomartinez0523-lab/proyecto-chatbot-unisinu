import sqlite3


def migrar_interacciones(db_path="chatbot_analytics.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT id, estado, opcion_elegida, categoria, subcategoria, mensaje_usuario FROM interacciones")
    filas = cursor.fetchall()

    menu_labels = {
        "1": "pensum",
        "2": "matricula",
        "3": "posgrados",
        "4": "cursos_ingles_espanol",
        "5": "bienestar",
        "6": "tutorias",
        "7": "semilleros",
        "8": "requisitos",
        "9": "reportes",
    }

    bienestar_labels = {
        "1": "deportes",
        "2": "area_cultural",
        "3": "comida",
    }

    deportes_labels = {
        "1": "Futbol",
        "2": "Futsala",
        "3": "Taekwondo",
        "4": "Rugby",
        "5": "Levantamiento de Pesas",
        "6": "Voleybol",
        "7": "Baloncesto",
        "8": "Softbol",
        "9": "Tenis de Mesa",
        "10": "Gimnasio Multifuerza",
    }

    actualizados = 0

    for row in filas:
        row_id, estado, opcion, categoria, subcategoria, mensaje_usuario = row
        if opcion is None:
            continue

        opcion_str = str(opcion).strip()
        nuevo_opcion = None
        nuevo_subcategoria = subcategoria
        nuevo_mensaje = mensaje_usuario

        if estado == "menu_principal" and opcion_str in menu_labels:
            nuevo_opcion = menu_labels[opcion_str]
            if mensaje_usuario is not None and str(mensaje_usuario).strip() == opcion_str:
                nuevo_mensaje = nuevo_opcion

        if estado == "seleccionar_bienestar" and opcion_str in bienestar_labels:
            nuevo_opcion = bienestar_labels[opcion_str]
            if categoria == "bienestar" and not subcategoria:
                nuevo_subcategoria = nuevo_opcion
            if mensaje_usuario is not None and str(mensaje_usuario).strip() == opcion_str:
                nuevo_mensaje = nuevo_opcion

        if estado == "bienestar_deportes" and opcion_str in deportes_labels:
            nombre = deportes_labels[opcion_str]
            nuevo_opcion = nombre
            if categoria == "bienestar":
                nuevo_subcategoria = f"deportes_{nombre}"
            if mensaje_usuario is not None and str(mensaje_usuario).strip() == opcion_str:
                nuevo_mensaje = nombre

        if estado == "seleccionar_pensum" and opcion_str.isdigit():
            # En este flujo ya se guarda el nombre del programa en subcategoria.
            if subcategoria:
                nuevo_opcion = subcategoria
                if mensaje_usuario is not None and str(mensaje_usuario).strip() == opcion_str:
                    nuevo_mensaje = subcategoria

        if (nuevo_mensaje is None or str(nuevo_mensaje).strip() == "") and nuevo_opcion is not None:
            nuevo_mensaje = nuevo_opcion

        if nuevo_opcion is not None and (
            str(nuevo_opcion) != opcion_str or (mensaje_usuario != nuevo_mensaje)
        ):
            cursor.execute(
                "UPDATE interacciones SET opcion_elegida = ?, subcategoria = ?, mensaje_usuario = ? WHERE id = ?",
                (nuevo_opcion, nuevo_subcategoria, nuevo_mensaje, row_id),
            )
            actualizados += 1

    conn.commit()
    conn.close()

    print(f"Registros actualizados: {actualizados}")


if __name__ == "__main__":
    migrar_interacciones()
