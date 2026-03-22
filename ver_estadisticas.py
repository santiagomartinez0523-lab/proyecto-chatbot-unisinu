import sqlite3
import pandas as pd
from datetime import datetime, timedelta

def ver_estadisticas():
    conn = sqlite3.connect('chatbot_analytics.db')
    
    print("\n" + "="*40)
    print("📊 REPORTE DE ESTADÍSTICAS DEL CHATBOT")
    print("="*40)
    
    # 1. Total de interacciones
    total = pd.read_sql_query("SELECT COUNT(*) as total FROM interacciones", conn).iloc[0]['total']
    print(f"\n✅ Total de interacciones registradas: {total}")
    
    # 2. Opciones más consultadas del menú principal
    print("\n🔝 Opciones más populares del Menú Principal:")
    query_menu = """
    SELECT opcion_id, num_consultas 
    FROM estadisticas_menu 
    ORDER BY num_consultas DESC
    """
    df_menu = pd.read_sql_query(query_menu, conn)
    # Mapeo de nombres si quieres
    print(df_menu)
    
    # 3. Programas más consultados
    print("\n🎓 Programas más consultados (Pensum/Requisitos):")
    df_prog = pd.read_sql_query("SELECT nombre_programa, num_consultas FROM estadisticas_programas ORDER BY num_consultas DESC", conn)
    print(df_prog)
    
    # 4. Actividad en las últimas 24 horas
    hace_24h = (datetime.now() - timedelta(hours=24)).strftime('%Y-%m-%d %H:%M:%S')
    recientes = pd.read_sql_query(f"SELECT COUNT(*) as total FROM interacciones WHERE timestamp > '{hace_24h}'", conn).iloc[0]['total']
    print(f"\n📈 Interacciones en las últimas 24h: {recientes}")
    
    # 5. Preguntas no respondidas
    print("\n❓ Preguntas que el bot no pudo responder:")
    df_no_resp = pd.read_sql_query("SELECT pregunta, timestamp FROM preguntas_no_respondidas ORDER BY timestamp DESC LIMIT 5", conn)
    if df_no_resp.empty:
        print("¡Ninguna! El bot ha entendido todo.")
    else:
        print(df_no_resp)
        
    conn.close()
    print("\n" + "="*40 + "\n")

if __name__ == "__main__":
    try:
        ver_estadisticas()
    except Exception as e:
        print(f"Error al cargar base de datos: {e}")
        print("Asegúrese de que el bot se haya ejecutado al menos una vez para generar 'chatbot_analytics.db'")
