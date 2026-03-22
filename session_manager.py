# session_manager.py
# Gestor de sesiones de usuario en memoria y disco

import json
import os

class SessionManager:
    """Clase para manejar las sesiones de los usuarios (estado y datos temporales)"""
    
    def __init__(self, filename='sessions.json'):
        self.filename = filename
        self.sessions = self._load_sessions()

    def _load_sessions(self):
        """Carga las sesiones desde un archivo JSON si existe"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️ Error cargando sesiones: {e}")
                return {}
        return {}

    def _save_sessions(self):
        """Guarda las sesiones actuales en el archivo JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.sessions, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Error guardando sesiones: {e}")

    def get_session(self, phone_number):
        """Retorna la sesión de un usuario o crea una nueva si no existe"""
        if phone_number not in self.sessions:
            self.sessions[phone_number] = {
                'estado': 'inicio',
                'datos_temporales': {}
            }
            # No guardamos aquí para no llenar el disco con sesiones vacías
        return self.sessions[phone_number]

    def update_session(self, phone_number, estado=None, datos_temporales=None):
        """Actualiza el estado y/o datos temporales de una sesión"""
        if phone_number not in self.sessions:
            self.get_session(phone_number)
            
        if estado:
            self.sessions[phone_number]['estado'] = estado
        
        if datos_temporales is not None:
            # Si se pasan nuevos datos, los fusionamos con los existentes
            self.sessions[phone_number]['datos_temporales'].update(datos_temporales)
            
        self._save_sessions()

    def reset_session(self, phone_number):
        """Reinicia la sesión del usuario al estado inicial"""
        self.sessions[phone_number] = {
            'estado': 'inicio',
            'datos_temporales': {}
        }
        self._save_sessions()

    def clear_temporal_data(self, phone_number):
        """Limpia solo los datos temporales sin cambiar el estado"""
        if phone_number in self.sessions:
            self.sessions[phone_number]['datos_temporales'] = {}
            self._save_sessions()

    def delete_session(self, phone_number):
        """Elimina por completo la sesión de un usuario"""
        if phone_number in self.sessions:
            del self.sessions[phone_number]
            self._save_sessions()

    def get_all_sessions(self):
        """Retorna todas las sesiones activas"""
        return self.sessions
