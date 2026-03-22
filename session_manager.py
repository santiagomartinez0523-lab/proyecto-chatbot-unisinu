import json
import os

class SessionManager:
    """Maneja las sesiones de los usuarios en un archivo JSON"""
    
    def __init__(self, filename='sessions.json'):
        self.filename = filename
        self.sessions = self._load_sessions()
        
    def _load_sessions(self):
        """Carga las sesiones desde el archivo JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
        
    def _save_sessions(self):
        """Guarda las sesiones en el archivo JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.sessions, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando sesiones: {e}")
            
    def get_session(self, phone_number):
        """Retorna la sesión de un usuario, si no existe la crea"""
        if phone_number not in self.sessions:
            self.sessions[phone_number] = {
                'estado': 'inicio',
                'datos_temporales': {},
                'ultima_interaccion': '' # Podrías agregar timestamps
            }
            self._save_sessions()
        return self.sessions[phone_number]
        
    def update_session(self, phone_number, estado=None, datos_temporales=None):
        """Actualiza el estado o los datos de una sesión"""
        if phone_number not in self.sessions:
            self.get_session(phone_number)
            
        if estado:
            self.sessions[phone_number]['estado'] = estado
        if datos_temporales is not None:
            # merge o reemplazo? probemos merge
            self.sessions[phone_number]['datos_temporales'].update(datos_temporales)
            
        self._save_sessions()
        
    def reset_session(self, phone_number):
        """Vuelve la sesión al estado inicial"""
        self.sessions[phone_number] = {
            'estado': 'inicio',
            'datos_temporales': {}
        }
        self._save_sessions()

    def get_all_sessions(self):
        """Devuelve todas las sesiones (para debug)"""
        return self.sessions

    def delete_session(self, phone_number):
        """Elimina una sesión de un usuario"""
        if phone_number in self.sessions:
            del self.sessions[phone_number]
            self._save_sessions()
            return True
        return False
