import json
import os
from datetime import datetime, timedelta


class SessionManager:
    """Gestiona las sesiones de usuarios en un archivo JSON"""
    
    def __init__(self, filename='sessions.json'):
        self.filename = filename
        self.sessions = self._load_sessions()
    
    def _load_sessions(self):
        """Carga sesiones desde el archivo JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error cargando sesiones: {e}")
                return {}
        return {}
    
    def _save_sessions(self):
        """Guarda sesiones en el archivo JSON"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.sessions, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error guardando sesiones: {e}")
    
    def get_session(self, phone_number):
        """Obtiene la sesión de un usuario"""
        if phone_number not in self.sessions:
            # Crear nueva sesión
            self.sessions[phone_number] = {
                'estado': 'inicio',
                'ultimo_menu': None,
                'datos_temporales': {},
                'created_at': datetime.now().isoformat(),
                'updated_at': datetime.now().isoformat()
            }
            self._save_sessions()
        
        return self.sessions[phone_number]
    
    def update_session(self, phone_number, estado=None, ultimo_menu=None, datos_temporales=None):
        """Actualiza la sesión de un usuario"""
        session = self.get_session(phone_number)
        
        if estado is not None:
            session['estado'] = estado
        
        if ultimo_menu is not None:
            session['ultimo_menu'] = ultimo_menu
        
        if datos_temporales is not None:
            session['datos_temporales'].update(datos_temporales)
        
        session['updated_at'] = datetime.now().isoformat()
        self._save_sessions()
    
    def reset_session(self, phone_number):
        """Reinicia la sesión de un usuario al estado inicial"""
        if phone_number in self.sessions:
            self.sessions[phone_number] = {
                'estado': 'inicio',
                'ultimo_menu': None,
                'datos_temporales': {},
                'created_at': self.sessions[phone_number].get('created_at', datetime.now().isoformat()),
                'updated_at': datetime.now().isoformat()
            }
            self._save_sessions()
    
    def delete_session(self, phone_number):
        """Elimina la sesión de un usuario"""
        if phone_number in self.sessions:
            del self.sessions[phone_number]
            self._save_sessions()
    
    def get_all_sessions(self):
        """Retorna todas las sesiones (útil para debugging)"""
        return self.sessions
    
    def clean_old_sessions(self, days=7):
        """Elimina sesiones inactivas de más de X días"""
        cutoff_date = datetime.now() - timedelta(days=days)
        to_delete = []
        
        for phone, session in self.sessions.items():
            updated_at = datetime.fromisoformat(session['updated_at'])
            if updated_at < cutoff_date:
                to_delete.append(phone)
        
        for phone in to_delete:
            del self.sessions[phone]
        
        if to_delete:
            self._save_sessions()
            print(f"🧹 Eliminadas {len(to_delete)} sesiones antiguas")
        
        return len(to_delete)
