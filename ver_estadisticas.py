# ver_estadisticas.py
# Script para ver las estadísticas del chatbot

from services.analytics_service import AnalyticsService

def mostrar_estadisticas():
    """Muestra las estadísticas del chatbot en consola"""
    analytics = AnalyticsService()
    
    print("="*60)
    print("📊 ESTADÍSTICAS DEL CHATBOT UNIVERSITARIO")
    print("="*60)
    
    # Resumen general
    resumen = analytics.obtener_resumen_general()
    print("\n📈 RESUMEN GENERAL:")
    print(f"   Total de interacciones: {resumen['total_interacciones']}")
    print(f"   Usuarios únicos: {resumen['usuarios_unicos']}")
    print(f"   Opción más popular: {resumen['opcion_mas_popular']}")
    print(f"   Veces usada: {resumen['veces_usada']}")
    
    # Usuarios activos
    usuarios_7d = analytics.obtener_usuarios_activos(7)
    print(f"\n👥 Usuarios activos (últimos 7 días): {usuarios_7d}")
    
    # Estadísticas del menú principal
    print("\n🎯 TOP 5 OPCIONES DEL MENÚ PRINCIPAL:")
    stats_menu = analytics.obtener_estadisticas_menu_principal()
    if not stats_menu.empty:
        top_5 = stats_menu.head(5)
        for idx, row in top_5.iterrows():
            print(f"   {row['opcion']}. {row['nombre_opcion']}: {row['contador']} veces")
    else:
        print("   (Sin datos aún)")
    
    # Programas más consultados
    print("\n🎓 PROGRAMAS MÁS CONSULTADOS:")
    stats_programas = analytics.obtener_estadisticas_programas()
    if not stats_programas.empty:
        for idx, row in stats_programas.head(5).iterrows():
            print(f"   • {row['programa']}: {row['contador']} consultas")
    else:
        print("   (Sin datos aún)")
    
    # Bienestar
    print("\n🏃 ACTIVIDADES DE BIENESTAR MÁS CONSULTADAS:")
    stats_bienestar = analytics.obtener_estadisticas_bienestar()
    if not stats_bienestar.empty:
        for idx, row in stats_bienestar.head(10).iterrows():
            if row['opcion'] != 'menu':
                print(f"   • {row['tipo'].capitalize()} - {row['opcion']}: {row['contador']} veces")
    else:
        print("   (Sin datos aún)")
    
    print("\n" + "="*60)
    print("✅ Estadísticas generadas exitosamente")
    print("="*60)

if __name__ == '__main__':
    mostrar_estadisticas()
