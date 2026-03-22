# services/analytics_service.py
# Servicio para rastrear y analizar el uso del chatbot

import sqlite3
import pandas as pd
from datetime import datetime
import os

class AnalyticsService:
    """Rastrea y analiza el uso del chatbot"""
    
    def __init__(self, db_path='chatbot_analytics.db'):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Inicializa la base de datos de analítica"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabla de interacciones generales
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interacciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                estado TEXT,
                opcion_elegida TEXT,
                categoria TEXT,
                subcategoria TEXT,
                mensaje_usuario TEXT
            )
        ''')
        
        # Tabla de estadísticas del menú principal
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu_principal_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                opcion INTEGER UNIQUE,
                nombre_opcion TEXT,
                contador INTEGER DEFAULT 0,
                ultima_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Insertar opciones del menú si no existen
        opciones_menu = [
            (1, 'Pensum del programa'),
            (2, 'Matrícula'),
            (3, 'Posgrado'),
            (4, 'Cursos Inglés/Español'),
            (5, 'Bienestar'),
            (6, 'Tutorías'),
            (7, 'Semilleros de Investigación'),
            (8, 'Requisitos de Materias'),
            (9, 'Reportes y Estadísticas')
        ]
        
        for opcion, nombre in opciones_menu:
            cursor.execute('''
                INSERT OR IGNORE INTO menu_principal_stats (opcion, nombre_opcion, contador)
                VALUES (?, ?, 0)
            ''', (opcion, nombre))
        
        # Tabla de estadísticas de bienestar
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS bienestar_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tipo TEXT,
                opcion TEXT,
                contador INTEGER DEFAULT 0,
                ultima_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(tipo, opcion)
            )
        ''')
        
        # Tabla de programas consultados
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS programas_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                programa TEXT UNIQUE,
                contador INTEGER DEFAULT 0,
                ultima_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Tabla de preguntas no entendidas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS preguntas_no_entendidas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                phone_number TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                estado TEXT,
                mensaje_usuario TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ Base de datos de analytics inicializada correctamente")
    
    def registrar_interaccion(self, phone_number, estado, opcion_elegida, 
                            categoria=None, subcategoria=None, mensaje_usuario=None):
        """Registra una interacción del usuario"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO interacciones 
            (phone_number, estado, opcion_elegida, categoria, subcategoria, mensaje_usuario)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (phone_number, estado, opcion_elegida, categoria, subcategoria, mensaje_usuario))
        
        conn.commit()
        conn.close()
    
    def registrar_opcion_menu_principal(self, opcion):
        """Incrementa el contador de una opción del menú principal"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE menu_principal_stats 
            SET contador = contador + 1,
                ultima_actualizacion = CURRENT_TIMESTAMP
            WHERE opcion = ?
        ''', (opcion,))
        
        conn.commit()
        conn.close()
    
    def registrar_opcion_bienestar(self, tipo_bienestar, opcion=None):
        """Registra selección en bienestar (deportes, cultural, comida)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO bienestar_stats (tipo, opcion, contador)
            VALUES (?, ?, 1)
            ON CONFLICT(tipo, opcion) 
            DO UPDATE SET contador = contador + 1, ultima_actualizacion = CURRENT_TIMESTAMP
        ''', (tipo_bienestar, opcion or 'menu'))
        
        conn.commit()
        conn.close()
    
    def registrar_programa_consultado(self, programa):
        """Registra consulta de programa (pensum, requisitos)"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO programas_stats (programa, contador)
            VALUES (?, 1)
            ON CONFLICT(programa) 
            DO UPDATE SET contador = contador + 1, ultima_actualizacion = CURRENT_TIMESTAMP
        ''', (programa,))
        
        conn.commit()
        conn.close()

    def registrar_pregunta_no_entendida(self, phone_number, estado, mensaje_usuario):
        """Registra una pregunta que el bot no pudo responder"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO preguntas_no_entendidas (phone_number, estado, mensaje_usuario)
            VALUES (?, ?, ?)
        ''', (phone_number, estado, mensaje_usuario))

        conn.commit()
        conn.close()
    
    def obtener_estadisticas_menu_principal(self):
        """Obtiene estadísticas del menú principal"""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query('''
            SELECT opcion, nombre_opcion, contador 
            FROM menu_principal_stats 
            ORDER BY contador DESC
        ''', conn)
        conn.close()
        return df
    
    def obtener_estadisticas_bienestar(self):
        """Obtiene estadísticas de bienestar"""
        conn = sqlite3.connect(self.db_path)
        try:
            df = pd.read_sql_query('''
                SELECT tipo, opcion, contador 
                FROM bienestar_stats 
                ORDER BY contador DESC
            ''', conn)
        except:
            df = pd.DataFrame(columns=['tipo', 'opcion', 'contador'])
        conn.close()
        return df
    
    def obtener_estadisticas_programas(self):
        """Obtiene estadísticas de programas consultados"""
        conn = sqlite3.connect(self.db_path)
        try:
            df = pd.read_sql_query('''
                SELECT programa, contador 
                FROM programas_stats 
                ORDER BY contador DESC
            ''', conn)
        except:
            df = pd.DataFrame(columns=['programa', 'contador'])
        conn.close()
        return df
    
    def obtener_interacciones_por_fecha(self, dias=30):
        """Obtiene interacciones de los últimos N días"""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query('''
            SELECT DATE(timestamp) as fecha, COUNT(*) as total
            FROM interacciones
            WHERE timestamp >= datetime('now', '-{} days')
            GROUP BY DATE(timestamp)
            ORDER BY fecha
        '''.format(dias), conn)
        conn.close()
        return df
    
    def obtener_usuarios_activos(self, dias=7):
        """Obtiene número de usuarios únicos activos"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT COUNT(DISTINCT phone_number) as usuarios_activos
            FROM interacciones
            WHERE timestamp >= datetime('now', '-{} days')
        '''.format(dias))
        
        resultado = cursor.fetchone()[0] or 0
        conn.close()
        return resultado
    
    def obtener_resumen_general(self):
        """Obtiene un resumen general de estadísticas"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Total de interacciones
        cursor.execute('SELECT COUNT(*) FROM interacciones')
        total_interacciones = cursor.fetchone()[0] or 0
        
        # Usuarios únicos
        cursor.execute('SELECT COUNT(DISTINCT phone_number) FROM interacciones')
        usuarios_unicos = cursor.fetchone()[0] or 0
        
        # Opción más popular
        cursor.execute('''
            SELECT nombre_opcion, contador 
            FROM menu_principal_stats 
            WHERE contador > 0
            ORDER BY contador DESC 
            LIMIT 1
        ''')
        opcion_popular = cursor.fetchone()
        
        conn.close()
        
        return {
            'total_interacciones': total_interacciones,
            'usuarios_unicos': usuarios_unicos,
            'opcion_mas_popular': opcion_popular[0] if opcion_popular else 'N/A',
            'veces_usada': opcion_popular[1] if opcion_popular else 0
        }
    
    def exportar_a_csv(self, tabla, filename):
        """Exporta una tabla a CSV para Power BI"""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(f'SELECT * FROM {tabla}', conn)
        conn.close()
        
        df.to_csv(filename, index=False, encoding='utf-8')
        return filename
    
    def exportar_a_excel(self, tabla, filename):
        """Exporta una tabla a Excel (.xlsx)"""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(f'SELECT * FROM {tabla}', conn)
        conn.close()
    
        df.to_excel(filename, index=False)
        return filename
    
    def exportar_todo_para_powerbi(self, carpeta='exports'):
        """Exporta todas las tablas para Power BI (Excel)"""
        os.makedirs(carpeta, exist_ok=True)
    
        # Limpiar exportaciones anteriores
        for nombre in os.listdir(carpeta):
            if nombre.lower().endswith(('.csv', '.xlsx')):
                try:
                    os.remove(os.path.join(carpeta, nombre))
                except Exception as e:
                    print(f"❌ Error eliminando {nombre}: {e}")
        
        tablas = [
            'interacciones',
            'menu_principal_stats',
            'bienestar_stats',
            'programas_stats',
            'preguntas_no_entendidas'
        ]
        
        archivos_exportados = []
        for tabla in tablas:
            try:
                filename = f'{carpeta}/{tabla}.xlsx'
                self.exportar_a_excel(tabla, filename)
                archivos_exportados.append(filename)
                print(f"✅ Exportado: {filename}")
            except Exception as e:
                print(f"❌ Error exportando {tabla}: {e}")
        
        return archivos_exportados


# Probar el servicio
if __name__ == '__main__':
    print("🧪 Ejecutando AnalyticsService...")

    analytics = AnalyticsService()

    if os.getenv('ANALYTICS_TEST_DATA') == '1':
        print("\n📝 Registrando interacciones de prueba...")
        analytics.registrar_interaccion('+573001234567', 'menu_principal', 'bienestar', 'bienestar')
        analytics.registrar_opcion_menu_principal(5)
        analytics.registrar_opcion_bienestar('deportes', 'Fútbol')

        analytics.registrar_interaccion('+573007654321', 'menu_principal', 'pensum', 'pensum')
        analytics.registrar_opcion_menu_principal(1)
        analytics.registrar_programa_consultado('Ingeniería de Sistemas')

    print("\n📊 Resumen general:")
    resumen = analytics.obtener_resumen_general()
    for key, value in resumen.items():
        print(f"   {key}: {value}")

    print("\n💾 Exportando datos...")
    archivos = analytics.exportar_todo_para_powerbi()

    print("\n✅ Exportacion completada exitosamente!")
