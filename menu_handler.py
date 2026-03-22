import re
import unicodedata

from config import IMAGE_URLS
from requisitos_data import (
    REQUISITOS_SISTEMAS,
    REQUISITOS_INDUSTRIAL,
    REQUISITOS_CIVIL,
    REQUISITOS_ELECTRICA,
    REQUISITOS_ELECTROMECANICA
)
from matricula_data import INFORMACION_MATRICULA
from posgrados_data import POSGRADOS_INFO
from bienestar_data import BIENESTAR_INFO 
from programas.sistema import funcion_sistema
from programas.industrial import funcion_industrial
from programas.civil import funcion_civil
from programas.electrica import funcion_electrica
from programas.electromecanica import funcion_electromecanica
from posgrados import funcion_posgrados
from matricula import funcion_matriculas
from services.analytics_service import AnalyticsService  


class MenuHandler:
    """Maneja la lógica de menús y respuestas del bot"""
    
    def __init__(self, session_manager):
        self.session_manager = session_manager
        self.requisitos_sistemas = REQUISITOS_SISTEMAS
        self.info_matricula = INFORMACION_MATRICULA
        self.info_posgrados = POSGRADOS_INFO
        self.info_bienestar = BIENESTAR_INFO  # Agregar bienestar

        self.requisitos_programas = {
            'sistemas': REQUISITOS_SISTEMAS,
            'industrial': REQUISITOS_INDUSTRIAL,
            'civil': REQUISITOS_CIVIL,
            'electrica': REQUISITOS_ELECTRICA,
            'electromecanica': REQUISITOS_ELECTROMECANICA
        }

        self._programas_labels = {
            'sistemas': 'Ingeniería de Sistemas',
            'industrial': 'Ingeniería Industrial',
            'civil': 'Ingeniería Civil',
            'electrica': 'Ingeniería Eléctrica',
            'electromecanica': 'Ingeniería Electromecánica'
        }

        self.analytics = AnalyticsService()
    
    def _normalize_text(self, text):
        """Limpia y normaliza el texto (minúsculas, sin tildes)"""
        text = text.strip().lower()
        # Eliminar tildes
        text = unicodedata.normalize('NFD', text)
        return ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')

    def _extract_first_int(self, text):
        """Extrae el primer número entero de un texto"""
        match = re.search(r'\d+', text)
        return int(match.group()) if match else None

    def process_message(self, phone_number, message):
        """Determina la respuesta según el estado del usuario y su mensaje"""
        session = self.session_manager.get_session(phone_number)
        estado = session['estado']
        text = self._normalize_text(message)
        
        # Guardar interaccion en analytics
        self.analytics.registrar_interaccion(phone_number, estado, None, mensaje_usuario=message)

        # COMANDO GLOBAL: MENU
        if text == 'menu' or text == 'inicio' or text == 'hola':
            self.session_manager.reset_session(phone_number)
            return self.get_main_menu()

        # MANEJO POR ESTADOS
        if estado == 'inicio':
            return self.handle_inicio(phone_number, text)
            
        elif estado == 'menu_principal':
            return self.handle_menu_principal(phone_number, text)
            
        elif estado == 'seleccionar_programa':
            return self.handle_seleccionar_programa(phone_number, text)
            
        elif estado == 'verificar_requisito':
            return self.handle_verificar_requisito(phone_number, text)

        elif estado == 'seleccionar_bienestar':
            return self.handle_seleccionar_bienestar(phone_number, text)
        
        elif estado == 'bienestar_deportes':
             return self.handle_bienestar_deportes(phone_number, text)
             
        elif estado == 'bienestar_cultural':
             return self.handle_bienestar_cultural(phone_number, text)

        elif estado == 'seleccionar_posgrado':
             return self.handle_seleccionar_posgrado(phone_number, text)

        # Si no reconoce el estado o mensaje
        return "No estoy seguro de cómo ayudarte con eso. Escribe *menu* para volver al inicio.", None

    def get_main_menu(self):
        """Devuelve el texto del menú principal"""
        menu = """*🎓 CHATBOT UNIVERSITARIO - UNISINU*

¡Hola! Soy tu asistente virtual. ¿En qué puedo ayudarte hoy?

Selecciona una opción escribiendo el número:

1. 📋 *Pensum del programa*
2. 📝 *Matrícula* (Inscripción y adición)
3. 🎓 *Posgrado* (Especialización, Maestría, Doctorado)
4. 🌎 *Cursos Inglés/Español*
5. 🏃 *Bienestar* (Deportes, Cultura, Comida)
6. 👨‍🏫 *Tutorías*
7. 🔍 *Semilleros de Investigación*
8. ⚖️ *Requisitos de Materias*
9. 📊 *Reportes y Estadísticas*

_Escribe *menu* en cualquier momento para volver aquí._"""
        return menu, IMAGE_URLS['LOGOU']

    def handle_inicio(self, phone_number, text):
        """Maneja el saludo inicial"""
        self.session_manager.update_session(phone_number, estado='menu_principal')
        return self.get_main_menu()

    def handle_menu_principal(self, phone_number, text):
        """Procesa la selección del menú principal"""
        opcion = self._extract_first_int(text)
        
        if not opcion:
            # Búsqueda por palabras clave si no hay número
            if 'pensum' in text or 'malla' in text: opcion = 1
            elif 'matricula' in text or 'inscri' in text: opcion = 2
            elif 'posgrado' in text or 'maestria' in text: opcion = 3
            elif 'ingles' in text or 'espanol' in text: opcion = 4
            elif 'bienestar' in text or 'deporte' in text: opcion = 5
            elif 'tutoria' in text: opcion = 6
            elif 'investigacion' in text or 'semillero' in text: opcion = 7
            elif 'requisito' in text: opcion = 8
            elif 'reporte' in text or 'estadistica' in text: opcion = 9

        if opcion == 1 or opcion == 8:
            # Analytics
            self.analytics.registrar_opcion_menu_principal(opcion)
            
            tipo = "requisitos" if opcion == 8 else "pensum"
            self.session_manager.update_session(phone_number, 
                                             estado='seleccionar_programa',
                                             datos_temporales={'tipo_consulta': tipo})
            
            msg = """*🎓 SELECCIONA TU PROGRAMA*

¿De qué programa deseas consultar?

1. Ingeniería de Sistemas
2. Ingeniería Industrial
3. Ingeniería Civil
4. Ingeniería Eléctrica
5. Ingeniería Electromecánica

_Escribe el número o el nombre del programa._"""
            return msg, None

        elif opcion == 2:
            self.analytics.registrar_opcion_menu_principal(2)
            # Matrícula - Mostrar pasos generales o pedir detalle
            msg = """*📝 INFORMACIÓN DE MATRÍCULA*

¿Qué deseas consultar sobre el proceso de matrícula?

1. Pasos para inscribir materias
2. Pasos para adicionar materias
3. Requisitos generales

_Escribe una opción o dinos tu duda._"""
            # Por ahora enviamos info general estructurada
            info = self.info_matricula['pasos_inscripcion']
            return f"*Pasos para Inscripción:*\n\n{info}", IMAGE_URLS['MATRICULA']

        elif opcion == 3:
            self.analytics.registrar_opcion_menu_principal(3)
            self.session_manager.update_session(phone_number, estado='seleccionar_posgrado')
            msg = """*🎓 POSGRADOS*

¿Qué nivel de posgrado te interesa?

1. Especializaciones
2. Maestrías
3. Doctorados

_Escribe el número de la opción._"""
            return msg, None

        elif opcion == 5:
             self.analytics.registrar_opcion_menu_principal(5)
             self.session_manager.update_session(phone_number, estado='seleccionar_bienestar')
             msg = """*🏃 BIENESTAR UNIVERSITARIO*

¿Qué área te gustaría consultar?

1. ⚽ *Deportes* (Fútbol, Taekwondo, Pesas...)
2. 🎭 *Área Cultural* (Danza, Música, Coro...)
3. 🍽️ *Comida* (Servicio de alimentación)

_Escribe el número de tu elección._"""
             return msg, None

        elif opcion == 9:
            # Analytics y Reportes (Simulado por ahora)
            msg = """*📊 ESTADÍSTICAS DEL BOT*

Has seleccionado ver el reporte de uso.
Esta funcionalidad permite visualizar qué áreas son las más consultadas por los estudiantes.

_Próximamente estaremos integrando gráficas en tiempo real aquí._"""
            return msg, None

        return "Opción no válida. Por favor selecciona un número del 1 al 9.", None

    def handle_seleccionar_programa(self, phone_number, text):
        """Procesa la selección del programa académico"""
        session = self.session_manager.get_session(phone_number)
        tipo_consulta = session['datos_temporales'].get('tipo_consulta', 'pensum')
        
        opcion = self._extract_first_int(text)
        programa_key = None
        
        # Mapeo de opciones
        programas_map = {
            1: 'sistemas',
            2: 'industrial',
            3: 'civil',
            4: 'electrica',
            5: 'electromecanica'
        }
        
        if opcion in programas_map:
            programa_key = programas_map[opcion]
        else:
            # Búsqueda por texto
            if 'sistema' in text: programa_key = 'sistemas'
            elif 'industrial' in text: programa_key = 'industrial'
            elif 'civil' in text: programa_key = 'civil'
            elif 'electrica' in text: programa_key = 'electrica'
            elif 'electromecanica' in text: programa_key = 'electromecanica'

        if programa_key:
            # Registrar programa en analytics
            self.analytics.registrar_programa_consultado(self._programas_labels[programa_key])
            
            if tipo_consulta == 'pensum':
                nombre = self._programas_labels[programa_key]
                img_key = f'PENSUM_{programa_key.upper()}'
                msg = f"Aquí tienes el pensum de *{nombre}*. \n\n¿Deseas consultar los requisitos de alguna materia de este programa? \n\n1. Sí, verificar requisitos\n2. No, volver al menú"
                
                self.session_manager.update_session(phone_number, 
                                                 estado='verificar_requisito',
                                                 datos_temporales={'programa': programa_key})
                return msg, IMAGE_URLS.get(img_key)
            else:
                # Flujo de requisitos directamente
                self.session_manager.update_session(phone_number, 
                                                 estado='verificar_requisito',
                                                 datos_temporales={'programa': programa_key})
                return f"Has seleccionado *{self._programas_labels[programa_key]}*. \n\n¿De qué semestre es la materia que buscas? (Escribe el número del semestre del 1 al 9)", None
        
        return "Programa no identificado. Por favor elige del 1 al 5.", None

    def handle_verificar_requisito(self, phone_number, text):
        """Maneja la consulta de requisitos específicos"""
        session = self.session_manager.get_session(phone_number)
        programa_key = session['datos_temporales'].get('programa')
        
        # Si el usuario dice 'no' o 'volver'
        if text in ['2', 'no', 'volver', 'regresar']:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self.get_main_menu()
            
        # Si el usuario elige 'si' (opción 1)
        if text == '1' or 'si' in text:
            return "¿De qué semestre es la materia? (Escribe el número del 1 al 9)", None

        # Si el usuario escribe un número de semestre
        semestre = self._extract_first_int(text)
        if semestre and 1 <= semestre <= 9:
            data_programa = self.requisitos_programas.get(programa_key, {})
            materias_semestre = data_programa.get(semestre, [])
            
            if not materias_semestre:
                return f"No tengo información detallada del semestre {semestre} para este programa en este momento.", None
                
            msg = f"*Materias de Semestre {semestre}:*\n\n"
            for i, materia in enumerate(materias_semestre, 1):
                msg += f"{i}. {materia['nombre']}\n"
            
            msg += "\nEscribe el nombre de la materia para ver sus requisitos o escribe *menu* para salir."
            
            # Guardar el semestre en datos temporales para facilitar la búsqueda
            datos = session['datos_temporales']
            datos['semestre_actual'] = semestre
            self.session_manager.update_session(phone_number, datos_temporales=datos)
            
            return msg, None

        # Búsqueda de materia por nombre
        semestre_actual = session['datos_temporales'].get('semestre_actual')
        if programa_key:
            requisitos_dict = self.requisitos_programas.get(programa_key, {})
            
            # Buscar en todos los semestres si no hay uno seleccionado, o priorizar el seleccionado
            materia_encontrada = None
            
            # Función auxiliar para comparar nombres normalizados
            def match_materia(nom_buscado, nom_real):
                return nom_buscado in self._normalize_text(nom_real)

            # Si hay un semestre seleccionado, buscar ahí primero
            if semestre_actual:
                for mat in requisitos_dict.get(semestre_actual, []):
                    if match_materia(text, mat['nombre']):
                        materia_encontrada = mat
                        break
            
            # Si no se encontró, buscar en todo el programa
            if not materia_encontrada:
                for sem, lista_mat in requisitos_dict.items():
                    for mat in lista_mat:
                        if match_materia(text, mat['nombre']):
                            materia_encontrada = mat
                            break
                    if materia_encontrada: break

            if maretia_encontrada:
                resp = f"📘 *Materia:* {materia_encontrada['nombre']}\n"
                resp += f"✅ *Requisito:* {materia_encontrada['requisito']}\n\n"
                resp += "¿Deseas ver otra materia? Escribe el nombre o el número de otro semestre."
                return resp, None

        return "No encontré la materia. Asegúrate de escribir bien el nombre o selecciona un semestre (1-9).", None

    def handle_seleccionar_bienestar(self, phone_number, text):
         """Maneja la selección de áreas de bienestar"""
         opcion = self._extract_first_int(text)
         
         if opcion == 1:
             self.analytics.registrar_opcion_bienestar('deportes')
             self.session_manager.update_session(phone_number, estado='bienestar_deportes')
             msg = self.info_bienestar['deportes']['info']
             return msg, None
         
         elif opcion == 2:
             self.analytics.registrar_opcion_bienestar('area_cultural')
             self.session_manager.update_session(phone_number, estado='bienestar_cultural')
             msg = self.info_bienestar['area_cultural']['info']
             return msg, None
             
         elif opcion == 3:
             self.analytics.registrar_opcion_bienestar('comida')
             return self.info_bienestar['comida']['info'], None
             
         return "Opción no válida. Elige 1 (Deportes), 2 (Cultura) o 3 (Comida).", None

    def handle_bienestar_deportes(self, phone_number, text):
        """Muestra detalles de un deporte específico"""
        detalles = self.info_bienestar['deportes']['detalles']
        opcion = str(self._extract_first_int(text))
        
        # Búsqueda por palabras clave si no hay número
        if opcion == 'None':
            if 'futbol' in text: opcion = '1'
            elif 'futsal' in text: opcion = '2'
            elif 'taekwondo' in text: opcion = '3'
            elif 'rugby' in text: opcion = '4'
            elif 'pesa' in text: opcion = '5'
            elif 'voley' in text: opcion = '6'
            elif 'balon' in text: opcion = '7'
            elif 'soft' in text: opcion = '8'
            elif 'tenis' in text: opcion = '9'
            elif 'gimnasio' in text: opcion = '10'

        if opcion in detalles:
            # Registrar en analytics
            self.analytics.registrar_opcion_bienestar('deportes', detalles[opcion] if isinstance(detalles[opcion], str) else f"deporte_{opcion}")
            
            info = detalles[opcion]
            if isinstance(info, dict):
                 # Si tiene masculino/femenino
                 return f"{info['masculino']}\n\n{info['femenino']}", None
            return info, None
            
        return "No reconozco ese deporte. Escribe el número correspondiente (1-10) o el nombre.", None

    def handle_bienestar_cultural(self, phone_number, text):
        """Muestra detalles de una actividad cultural"""
        detalles = self.info_bienestar['area_cultural']['detalles']
        opcion = str(self._extract_first_int(text))
        
        if opcion == 'None':
             if 'gaita' in text or 'tambor' in text: opcion = '1'
             elif 'rock' in text: opcion = '2'
             elif 'orquesta' in text: opcion = '3'
             elif 'vallenato' in text: opcion = '4'
             elif 'coro' in text: opcion = '5'
             elif 'modern' in text: opcion = '6'  # Danza moderna
             elif 'folclor' in text: opcion = '7' # Danza folclórica

        if opcion in detalles:
            # Analytics
            self.analytics.registrar_opcion_bienestar('area_cultural', f"cultural_{opcion}")
            return detalles[opcion], None
            
        return "No reconozco esa actividad cultural. Escribe el número correspondiente (1-7).", None

    def handle_seleccionar_posgrado(self, phone_number, text):
        """Maneja la selección de niveles de posgrado"""
        opcion = self._extract_first_int(text)
        
        niveles = {1: 'especializaciones', 2: 'maestrias', 3: 'doctorados'}
        
        if opcion in niveles:
            nivel_key = niveles[opcion]
            programas = self.info_posgrados[nivel_key]
            
            resp = f"*🎓 {nivel_key.upper()} DISPONIBLES*\n\n"
            for prog in programas:
                resp += f"• *{prog['nombre']}*\n  ⏳ Duración: {prog['duracion']}\n  💰 Inversión aprox: {prog['costo']}\n\n"
            
            resp += "_Para más información o proceso de posgrado, escribe *menu*._"
            return resp, None
            
        return "Por favor selecciona una opción válida (1-3).", None
