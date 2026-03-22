# test_bot_local.py
# Script para probar el bot localmente sin WhatsApp

from session_manager import SessionManager
from menu_handler import MenuHandler

def test_bot():
    """Simula una conversación con el bot en la consola"""
    
    # Inicializar componentes
    session_manager = SessionManager(filename='test_sessions.json')
    menu_handler = MenuHandler(session_manager)
    
    # Número de prueba
    test_phone = "whatsapp:+573001234567"
    
    print("=" * 60)
    print("🤖 BOT DE WHATSAPP - MODO PRUEBA LOCAL")
    print("=" * 60)
    print("\nEscribe 'salir' para terminar la prueba\n")
    print("-" * 60)
    
    # Resetear sesión de prueba
    session_manager.reset_session(test_phone)
    
    # Mostrar menú inicial
    response, image_url = menu_handler.process_message(test_phone, "inicio")
    print(f"\n🤖 Bot:\n{response}")
    if image_url:
        print(f"\n📷 Imagen: {image_url}")
    print("-" * 60)
    
    # Loop de conversación
    while True:
        try:
            # Obtener input del usuario
            user_input = input("\n👤 Tú: ").strip()
            
            if user_input.lower() == 'salir':
                print("\n👋 Prueba terminada")
                break
            
            if not user_input:
                print("❌ Por favor escribe algo")
                continue
            
            # Procesar mensaje
            response, image_url = menu_handler.process_message(test_phone, user_input)
            
            # Mostrar respuesta
            print(f"\n🤖 Bot:\n{response}")
            
            if image_url:
                print(f"\n📷 Imagen: {image_url}")
            
            # Mostrar estado actual (para debugging)
            session = session_manager.get_session(test_phone)
            print(f"\n[DEBUG] Estado actual: {session['estado']}")
            if session['datos_temporales']:
                print(f"[DEBUG] Datos temporales: {session['datos_temporales']}")
            
            print("-" * 60)
            
        except KeyboardInterrupt:
            print("\n\n👋 Prueba interrumpida")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("-" * 60)
    
    # Limpiar sesión de prueba
    session_manager.delete_session(test_phone)
    print("\n✅ Sesión de prueba eliminada")


def test_session_manager():
    """Prueba el sistema de sesiones"""
    print("\n" + "=" * 60)
    print("🧪 PROBANDO SESSION MANAGER")
    print("=" * 60)
    
    sm = SessionManager(filename='test_sessions.json')
    
    # Crear sesiones de prueba
    test_phones = [
        "whatsapp:+573001111111",
        "whatsapp:+573002222222",
        "whatsapp:+573003333333"
    ]
    
    for phone in test_phones:
        sm.update_session(phone, estado='menu_principal')
        print(f"✅ Sesión creada para {phone}")
    
    # Mostrar todas las sesiones
    print(f"\n📊 Total de sesiones: {len(sm.get_all_sessions())}")
    
    # Actualizar una sesión
    sm.update_session(test_phones[0], estado='verificar_requisito', datos_temporales={'programa': 'sistema'})
    print(f"\n✅ Sesión actualizada: {test_phones[0]}")
    
    # Mostrar sesión específica
    session = sm.get_session(test_phones[0])
    print(f"   Estado: {session['estado']}")
    print(f"   Datos: {session['datos_temporales']}")
    
    # Resetear sesión
    sm.reset_session(test_phones[1])
    print(f"\n🔄 Sesión reseteada: {test_phones[1]}")
    
    # Eliminar sesión
    sm.delete_session(test_phones[2])
    print(f"\n🗑️  Sesión eliminada: {test_phones[2]}")
    
    # Estado final
    print(f"\n📊 Total de sesiones finales: {len(sm.get_all_sessions())}")
    
    # Limpiar todas las sesiones de prueba
    for phone in test_phones:
        if phone in sm.sessions:
            sm.delete_session(phone)
    
    print("\n✅ Prueba de SessionManager completada")


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════╗
║        HERRAMIENTA DE PRUEBA DEL BOT DE WHATSAPP         ║
╚══════════════════════════════════════════════════════════╝

Selecciona una opción:

1. Probar bot completo (simular conversación)
2. Probar sistema de sesiones
3. Ejecutar ambas pruebas

""")
    
    try:
        opcion = input("Opción (1-3): ").strip()
        
        if opcion == "1":
            test_bot()
        elif opcion == "2":
            test_session_manager()
        elif opcion == "3":
            test_session_manager()
            print("\n" + "=" * 60 + "\n")
            test_bot()
        else:
            print("❌ Opción inválida")
    
    except KeyboardInterrupt:
        print("\n\n👋 Adiós")
    except Exception as e:
        print(f"\n❌ Error: {e}")
