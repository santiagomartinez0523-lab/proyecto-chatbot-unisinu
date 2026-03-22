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

        self._programas_keywords = {
            'sistemas': ['sistema', 'sistemas', 'ing sistemas', 'ingenieria de sistemas'],
            'industrial': ['industrial', 'ing industrial', 'ingenieria industrial'],
            'civil': ['civil', 'ing civil', 'ingenieria civil'],
            'electrica': ['electrica', 'eléctrica', 'ing electrica', 'ingenieria electrica'],
            'electromecanica': ['electromecanica', 'electromecánica', 'ing electromecanica', 'ingenieria electromecanica']
        }

        self._keywords_menu_principal = {
            1: ['pensum', 'plan de estudios', 'malla curricular'],
            2: ['matricula', 'inscripcion', 'inscribir', 'baja', 'ingresar materia'],
            3: ['posgrado', 'maestria', 'maestría', 'doctorado', 'especializacion', 'especialización'],
            4: ['curso de ingles', 'curso de espanol', 'curso de español', 'ingles', 'espanol', 'español'],
            5: [
                'bienestar', 'deporte', 'deportes', 'actividad deportiva', 'actividades deportivas',
                'actividad fisica', 'actividades fisicas', 'gimnasio', 'entrenamiento',
                'cultural', 'cultura', 'area cultural', 'área cultural', 'arte', 'musica', 'música',
                'danza', 'teatro', 'comida', 'alimentacion', 'alimentación', 'cafeteria', 'cafetería',
                'menu', 'menú', 'servicio de alimentacion', 'servicio de alimentación'
            ],
            6: ['tutoria', 'tutorias', 'tutoría', 'tutorías'],
            7: ['semillero', 'semilleros', 'investigacion', 'investigación'],
            8: ['requisito', 'requisitos', 'prerrequisito', 'pre requisito', 'correlativo', 'materia requisito']
        }

        self._keywords_bienestar = {
            'deportes': [
                'deporte', 'deportes', 'actividad deportiva', 'actividades deportivas',
                'actividad fisica', 'actividades fisicas', 'entrenamiento', 'gimnasio',
                'futbol', 'fútbol', 'futsal', 'futsala', 'baloncesto', 'voley', 'voleibol',
                'tenis de mesa', 'rugby', 'taekwondo', 'pesas', 'levantamiento de pesas'
            ],
            'area_cultural': [
                'cultural', 'cultura', 'area cultural', 'área cultural', 'arte',
                'actividades culturales', 'musica', 'música', 'danza', 'teatro', 'coro',
                'orquesta', 'gaitas', 'tambores', 'grupo de rock', 'rock'
            ],
            'comida': [
                'comida', 'alimentacion', 'alimentación', 'cafeteria', 'cafetería',
                'menu', 'menú', 'almuerzo', 'restaurante', 'servicio de alimentacion',
                'servicio de alimentación', 'cantina'
            ]
        }

        self._keywords_requisitos = [
            'requisito', 'requisitos', 'prerrequisito', 'pre requisito',
            'correlativo', 'materia requisito', 'requisitos de', 'requisito de'
        ]

        self._keywords_semestre_materias = [
            'materias del semestre', 'materias de semestre', 'materias semestre',
            'materias del sem', 'materias del 7', 'materias del 8',
            'materias del 6', 'materias del 5', 'materias del 4',
            'materias del 3', 'materias del 2', 'materias del 1',
            'materias del 9', 'materias del 10', 'materias sem'
        ]
        
        # NUEVO: Inicializar servicio de analytics
        self.analytics = AnalyticsService()

        self._programas_map = {
            'sistema': 1,
            'industrial': 2,
            'civil': 3,
            'electrica': 4,
            'electromecanica': 5
        }

        self._deportes_map = {
            'futbol': '1',
            'futbol masculino': '1',
            'futbol femenino': '1',
            'futsala': '2',
            'futsal': '2',
            'taekwondo': '3',
            'rugby': '4',
            'levantamiento de pesas': '5',
            'pesas': '5',
            'voleybol': '6',
            'voleibol': '6',
            'baloncesto': '7',
            'softbol': '8',
            'tenis de mesa': '9',
            'gimnasio': '10',
            'gimnasio multifuerza': '10'
        }

        self._cultural_map = {
            'gaitas': '1',
            'tambores': '1',
            'gaitas y tambores': '1',
            'rock': '2',
            'grupo de rock': '2',
            'orquesta': '3',
            'vallenato': '4',
            'coro': '5',
            'danza moderna': '6',
            'danza folclorica': '7',
            'danza folclórica': '7'
        }

        self._romanos = {
            'i': 1,
            'ii': 2,
            'iii': 3,
            'iv': 4,
            'v': 5,
            'vi': 6,
            'vii': 7,
            'viii': 8,
            'ix': 9,
            'x': 10
        }

        self._materia_index = self._build_materia_index()

    def _normalize_text(self, text):
        text = text.strip().lower()
        text = unicodedata.normalize('NFD', text)
        return ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')

    def _extract_first_int(self, text):
        match = re.search(r'\d+', text)
        return int(match.group()) if match else None

    def _infer_menu_principal_option(self, message):
        text = self._normalize_text(message)
        number = self._extract_first_int(text)
        if number in range(1, 9):
            return number

        for opcion, keywords in self._keywords_menu_principal.items():
            if any(k in text for k in keywords):
                return opcion

        return None

    def _infer_programa_key(self, message):
        text = self._normalize_text(message)
        for programa, keywords in self._programas_keywords.items():
            if any(k in text for k in keywords):
                return programa if programa != 'sistemas' else 'sistema'
        return None

    def _infer_posgrado_tipo(self, message):
        text = self._normalize_text(message)
        if 'doctorado' in text:
            return 1
        if 'maestria' in text or 'maestría' in text:
            return 2
        if 'especializacion' in text or 'especialización' in text:
            return 3
        return None

    def _infer_bienestar_categoria(self, message):
        text = self._normalize_text(message)
        for categoria, keywords in self._keywords_bienestar.items():
            if any(k in text for k in keywords):
                return categoria
        return None

    def _parse_yes_no(self, message):
        text = self._normalize_text(message)
        if text in ['si', 'sí', 's', 'claro', 'ok', 'vale', 'yes']:
            return True
        if text in ['no', 'n', 'nop', 'nope']:
            return False
        return None

    def _registrar_no_entendida(self, phone_number, estado, message):
        self.analytics.registrar_pregunta_no_entendida(
            phone_number=phone_number,
            estado=estado,
            mensaje_usuario=message
        )

    def _set_pregunta_pendiente(self, phone_number, message):
        self.session_manager.update_session(
            phone_number,
            datos_temporales={'pregunta_pendiente': message}
        )
        self.session_manager.update_session(
            phone_number,
            datos_temporales={'pregunta_pendiente': message}
        )

    def _build_mensaje_usuario(self, phone_number, message):
        session = self.session_manager.get_session(phone_number)
        pendiente = session.get('datos_temporales', {}).get('pregunta_pendiente')
        if pendiente and pendiente != message:
            combinado = f"{pendiente} | detalle: {message}"
        else:
            combinado = message

        self.session_manager.update_session(
            phone_number,
            datos_temporales={'pregunta_pendiente': None}
        )
        return combinado

    def _infer_genero(self, message):
        text = self._normalize_text(message)
        tokens = set(re.findall(r'\b\w+\b', text))
        if any(k in tokens for k in ['hombre', 'masculino', 'varon', 'm']):
            return 'masculino'
        if any(k in tokens for k in ['mujer', 'femenino', 'f', 'dama', 'chica']):
            return 'femenino'
        return None

    def _is_list_request(self, message):
        text = self._normalize_text(message)
        return any(k in text for k in [
            'cuales son', 'cual es', 'que deportes', 'que actividades',
            'lista', 'listado', 'disponibles', 'existen', 'hay',
            'ver deportes', 'ver actividades', 'ver opciones'
        ])

    def _has_requisito_intent(self, message):
        text = self._normalize_text(message)
        return any(k in text for k in self._keywords_requisitos)

    def _has_semestre_materias_intent(self, message):
        text = self._normalize_text(message)
        return any(k in text for k in self._keywords_semestre_materias) and self._extract_semestre_from_text(text) is not None

    def _extract_semestre_from_text(self, message):
        text = self._normalize_text(message)
        number = self._extract_first_int(text)
        if number:
            return number
        return self._romanos.get(text)

    def _replace_roman_with_numbers(self, text):
        def repl(match):
            romano = match.group(0)
            return str(self._romanos.get(romano, romano))
        return re.sub(r'\b(i|ii|iii|iv|v|vi|vii|viii|ix|x)\b', repl, text)

    def _build_materia_index(self):
        index = {}
        for programa, data in self.requisitos_programas.items():
            for semestre, info in data.items():
                materias = info.get('materias')
                if not materias:
                    continue
                for _, (nombre, requisito) in materias.items():
                    key = self._normalize_text(nombre)
                    key_alt = self._replace_roman_with_numbers(key)
                    entry = {
                        'programa': programa,
                        'programa_nombre': self._programas_labels[programa],
                        'semestre': semestre,
                        'materia': nombre,
                        'requisito': requisito
                    }
                    index.setdefault(key, []).append(entry)
                    index.setdefault(key_alt, []).append(entry)
        return index

    def _find_materia_matches(self, message):
        text = self._normalize_text(message)
        matches = []
        for key, entries in self._materia_index.items():
            if key and key in text:
                matches.append((key, entries))
        if not matches:
            return []
        max_len = max(len(key) for key, _ in matches)
        filtered = []
        for key, entries in matches:
            if len(key) == max_len:
                filtered.extend(entries)
        return filtered

    def _build_materias_semestre_text(self, programa_key, semestre):
        requisitos = self.requisitos_programas.get(programa_key, {})
        semestre_info = requisitos.get(semestre)
        nombre_programa = self._programas_labels.get(programa_key, 'Programa')

        if not semestre_info:
            return f"❌ No tengo información del semestre {semestre} para {nombre_programa}."

        if 'materias' not in semestre_info:
            mensaje = semestre_info.get('mensaje', 'Información no disponible para este semestre.')
            return f"📚 *{nombre_programa}*\n\n{mensaje}"

        materias = semestre_info['materias']
        nombre_semestre = semestre_info.get('nombre', f'Semestre {semestre}')
        texto = f"📚 *{nombre_programa}*\n\n*{nombre_semestre}*\n\nMaterias disponibles:\n\n"
        for num, (nombre, _) in materias.items():
            texto += f"• {nombre}\n"
        return texto
    
    def process_message(self, phone_number, message):
        """
        Procesa el mensaje del usuario y retorna la respuesta
        Returns: (texto_respuesta, url_imagen_o_None)
        """
        session = self.session_manager.get_session(phone_number)
        estado = session['estado']
        
        # Comandos especiales y saludos
        mensaje_lower = message.lower().strip()
        
        
        if mensaje_lower in ['menu', 'inicio', 'volver', 'reset']:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None
        
        
        saludos = ['hola', 'hi', 'hello', 'buenas', 'buenos dias', 'buenas tardes', 
                   'buenas noches', 'hey', 'ey', 'saludos', 'que tal']
        if mensaje_lower in saludos:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None

        if self._has_requisito_intent(message):
            matches = self._find_materia_matches(message)
            if matches:
                return self._handle_requisitos_por_materia(phone_number, matches)
            self.session_manager.update_session(phone_number, estado='requisitos_buscar_materia')
            return "📋 ¿De qué materia deseas conocer el requisito? Escribe el nombre de la materia.", None

        if self._has_semestre_materias_intent(message):
            semestre = self._extract_semestre_from_text(message)
            programa_key = self._infer_programa_key(message)
            if programa_key == 'sistema':
                programa_key = 'sistemas'
            if programa_key in self.requisitos_programas:
                texto = self._build_materias_semestre_text(programa_key, semestre)
                return f"{texto}\n\n_Escribe *menu* para volver al inicio_", None

            self.session_manager.update_session(
                phone_number,
                estado='requisitos_elegir_programa_semestre',
                datos_temporales={'semestre_consulta': semestre}
            )
            return self._menu_requisitos(), None
        
        # Enrutamiento según estado
        if estado == 'inicio':
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None
        
        elif estado == 'menu_principal':
            return self._handle_menu_principal(phone_number, message)
        
        elif estado == 'seleccionar_pensum':
            return self._handle_seleccionar_pensum(phone_number, message)
        
        elif estado == 'verificar_requisito':
            return self._handle_verificar_requisito(phone_number, message)
        
        elif estado == 'seleccionar_bienestar':
            return self._handle_seleccionar_bienestar(phone_number, message)
        
        elif estado == 'bienestar_deportes':
            return self._handle_bienestar_deportes(phone_number, message)

        elif estado == 'bienestar_deportes_genero':
            return self._handle_bienestar_deportes_genero(phone_number, message)
        
        elif estado == 'bienestar_area_cultural':
            return self._handle_bienestar_area_cultural(phone_number, message)
        
        elif estado == 'bienestar_comida':
            return self._handle_bienestar_comida(phone_number, message)
        
        elif estado == 'confirmar_otro_bienestar':
            return self._handle_confirmar_otro_bienestar(phone_number, message)
        
        elif estado == 'seleccionar_requisitos':
            return self._handle_seleccionar_requisitos(phone_number, message)

        elif estado == 'requisitos_buscar_materia':
            return self._handle_requisitos_buscar_materia(phone_number, message)
        
        elif estado == 'requisitos_semestre':
            return self._handle_requisitos_semestre(phone_number, message)
        
        elif estado == 'requisitos_materia':
            return self._handle_requisitos_materia(phone_number, message)

        elif estado == 'requisitos_elegir_programa':
            return self._handle_requisitos_elegir_programa(phone_number, message)

        elif estado == 'requisitos_elegir_programa_semestre':
            return self._handle_requisitos_elegir_programa_semestre(phone_number, message)
        
        elif estado == 'confirmar_otra_asignatura':
            return self._handle_confirmar_otra_asignatura(phone_number, message)
        
        elif estado == 'matricula_paso':
            return self._handle_matricula_paso(phone_number, message)
        
        elif estado == 'confirmar_otra_matricula':
            return self._handle_confirmar_otra_matricula(phone_number, message)
        
        elif estado == 'menu_posgrados':
            return self._handle_menu_posgrados(phone_number, message)
        
        elif estado == 'seleccionar_tipo_posgrado':
            return self._handle_seleccionar_tipo_posgrado(phone_number, message)
        
        elif estado == 'confirmar_otro_posgrado':
            return self._handle_confirmar_otro_posgrado(phone_number, message)
        
        else:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None
    
    def _menu_principal(self):
        """Retorna el menú principal"""
        return """🎓 *Bienvenido al ChatBot Universitario*

¿Cuál es el motivo de su solicitud?

1. 📋 *Pensum del programa*
2. 📝 *Matrícula* (Inscripción y adición)
3. 🎓 *Posgrado* (Especialización, Maestría, Doctorado)
4. 🌎 *Cursos Inglés/Español*
5. 🏃 *Bienestar* (Deportes, Cultura, Comida)
6. 👨‍🏫 *Tutorías*
7. 🔍 *Semilleros de Investigación*
8. ⚖️ *Requisitos de Materias*

_Escribe el número de la opción o el nombre del tema._"""
    
    def _handle_menu_principal(self, phone_number, message):
        """Maneja la selección del menú principal"""
        opcion = self._infer_menu_principal_option(message)
        if opcion is None:
            self._registrar_no_entendida(phone_number, 'menu_principal', message)
            return (
                "No entiendo la pregunta. Solo puedo responder preguntas relacionadas con: "
                "pensum, matrícula, posgrados, cursos de inglés/español, bienestar, tutorías, semilleros y requisitos."
            ), None
        
        # NUEVO: Registrar la opción elegida en analytics
        if 1 <= opcion <= 9:
            opcion_labels = {
                1: 'pensum',
                2: 'matricula',
                3: 'posgrados',
                4: 'cursos_ingles_espanol',
                5: 'bienestar',
                6: 'tutorias',
                7: 'semilleros',
                8: 'requisitos',
                9: 'reportes'
            }
            self.analytics.registrar_opcion_menu_principal(opcion)
            self.analytics.registrar_interaccion(
                phone_number=phone_number,
                estado='menu_principal',
                opcion_elegida=opcion_labels.get(opcion, str(opcion)),
                mensaje_usuario=self._build_mensaje_usuario(phone_number, message)
            )
        
        if opcion == 1:
            self.session_manager.update_session(phone_number, estado='seleccionar_pensum')
            return self._menu_pensum(), None
        
        elif opcion == 2:
            info = self.info_matricula[1]
            
            self.session_manager.update_session(
                phone_number,
                estado='matricula_paso',
                datos_temporales={'paso_actual': 2}
            )
            
            texto_paso1 = f"📋 *Cómo Ingresar una Materia*\n\n*Paso 1 de 3*\n\n{info['pasos'][0]['texto']}\n\n_Escribe *siguiente* para ver el paso 2_"
            
            return texto_paso1, info['pasos'][0]['imagen']
        
        elif opcion == 3:
            self.session_manager.update_session(phone_number, estado='menu_posgrados')
            return self._menu_posgrados(), None
        
        elif opcion == 4:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return "📚 *Cursos de Inglés/Español*\n\nEn proceso...\n\n_Escribe *menu* para volver al inicio_", None
        
        elif opcion == 5:
            categoria = self._infer_bienestar_categoria(message)
            if categoria == 'deportes':
                self.session_manager.update_session(
                    phone_number,
                    estado='bienestar_deportes',
                    datos_temporales={'categoria_bienestar': 'deportes'}
                )
                return self.info_bienestar['deportes']['info'], None
            if categoria == 'area_cultural':
                self.session_manager.update_session(
                    phone_number,
                    estado='bienestar_area_cultural',
                    datos_temporales={'categoria_bienestar': 'area_cultural'}
                )
                return self.info_bienestar['area_cultural']['info'], None
            if categoria == 'comida':
                self.session_manager.update_session(
                    phone_number,
                    estado='bienestar_comida',
                    datos_temporales={'categoria_bienestar': 'comida'}
                )
                info_comida = self.info_bienestar.get('comida', {})
                texto = info_comida.get('info', '🍽️ *Comida*\n\nInformación no disponible.')
                self.session_manager.update_session(
                    phone_number,
                    estado='confirmar_otro_bienestar'
                )
                return f"{texto}\n\n¿Deseas consultar otra opción de bienestar? Responde sí o no.", None

            self.session_manager.update_session(phone_number, estado='seleccionar_bienestar')
            return self._menu_bienestar(), None
        
        elif opcion == 6:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return "👨‍🏫 *Tutorías*\n\nEn proceso...\n\n_Escribe *menu* para volver al inicio_", None
        
        elif opcion == 7:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return "🔬 *Semilleros de Investigación*\n\nEn proceso...\n\n_Escribe *menu* para volver al inicio_", None
        
        elif opcion == 8:
            self.session_manager.update_session(phone_number, estado='seleccionar_requisitos')
            return self._menu_requisitos(), None
        
        else:
            return "No entendí tu solicitud. ¿Qué deseas consultar? (pensum, matrícula, posgrados, bienestar, requisitos, tutorías, semilleros).", None
    
    def _menu_pensum(self):
        """Retorna el menú de selección de pensum"""
        return """📚 *¿Qué pensum de programa deseas saber?*

Opciones: Ingeniería de Sistemas, Ingeniería Industrial, Ingeniería Civil, Ingeniería Eléctrica, Ingeniería Electromecánica.

Escribe el nombre del programa."""
    
    def _handle_seleccionar_pensum(self, phone_number, message):
        """Maneja la selección de pensum"""
        opcion = self._extract_first_int(message)
        if opcion is None:
            programa_key = self._infer_programa_key(message)
            if programa_key:
                opcion = self._programas_map.get(programa_key)
        if opcion is None:
            self._set_pregunta_pendiente(phone_number, message)
            return "No entendí el programa. ¿De qué carrera quieres saber el pensum? (Sistemas, Industrial, Civil, Eléctrica o Electromecánica).", None
        
        programas = {
            1: ('Ingeniería de Sistemas', 'sistema', IMAGE_URLS['ing_sistema']),
            2: ('Ingeniería Industrial', 'industrial', IMAGE_URLS['ing_industrial']),
            3: ('Ingeniería Civil', 'civil', IMAGE_URLS['ing_civil']),
            4: ('Ingeniería Eléctrica', 'electrica', IMAGE_URLS['ing_electrica']),
            5: ('Ingeniería Electromecánica', 'electromecanica', IMAGE_URLS['ing_electromecanica'])
        }
        
        if opcion not in programas:
            self._set_pregunta_pendiente(phone_number, message)
            return "No entendí el programa. ¿De qué carrera quieres saber el pensum? (Sistemas, Industrial, Civil, Eléctrica o Electromecánica).", None
        
        nombre, clave, url = programas[opcion]
        
        # NUEVO: Registrar programa consultado
        self.analytics.registrar_programa_consultado(nombre)
        self.analytics.registrar_interaccion(
            phone_number=phone_number,
            estado='seleccionar_pensum',
            opcion_elegida=nombre,
            categoria='pensum',
            subcategoria=nombre,
            mensaje_usuario=self._build_mensaje_usuario(phone_number, message)
        )
        
        self.session_manager.update_session(
            phone_number,
            estado='verificar_requisito',
            datos_temporales={'programa': clave, 'nombre_programa': nombre}
        )
        
        texto = f"""📊 *Pensum de {nombre}*

¿Deseas verificar algún requisito de una materia?

    Responde *sí* para continuar o *no* para volver al menú principal."""
        
        return texto, url
    
    def _handle_verificar_requisito(self, phone_number, message):
        """Maneja la verificación de requisitos desde el pensum"""
        opcion = self._extract_first_int(message)
        if opcion is None:
            respuesta = self._parse_yes_no(message)
            if respuesta is True:
                opcion = 1
            elif respuesta is False:
                opcion = 2
        if opcion is None:
            self._set_pregunta_pendiente(phone_number, message)
            return "❌ Por favor responde con *sí* o *no*.", None
        
        session = self.session_manager.get_session(phone_number)
        programa = session['datos_temporales'].get('programa')
        
        if opcion == 1:
            if programa == 'sistema':
                self.session_manager.update_session(
                    phone_number,
                    estado='requisitos_semestre',
                    datos_temporales={'programa_req': 'sistemas'}
                )
                return self._menu_semestres_programa('sistemas'), None
            else:
                funciones = {
                    'industrial': funcion_industrial,
                    'civil': funcion_civil,
                    'electrica': funcion_electrica,
                    'electromecanica': funcion_electromecanica
                }
                
                if programa in funciones:
                    # SIMULACIÓN: En un bot real llamaríamos a la función del módulo
                    # Aquí retornamos un mensaje orientativo
                    self.session_manager.update_session(
                        phone_number,
                        estado='requisitos_semestre',
                        datos_temporales={'programa_req': programa}
                    )
                    return self._menu_semestres_programa(programa), None
                else:
                    self.session_manager.update_session(phone_number, estado='menu_principal')
                    return "❌ Error: Programa no encontrado.\n\n_Escribe *menu* para volver al inicio_", None
        
        elif opcion == 2:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None
        
        else:
            return "❌ Opción no válida. Por favor elige (1 o 2) o Para volver al menú, escribe: *menu*.", None
    
    # ========== FUNCIONES PARA BIENESTAR ==========
    
    def _menu_bienestar(self):
        """Retorna el menú de bienestar"""
        return """🏃 *Bienestar Universitario*

¿Qué área te gustaría consultar?

1. ⚽ *Deportes* (Fútbol, Taekwondo, Pesas...)
2. 🎭 *Área Cultural* (Danza, Música, Coro...)
3. 🍽️ *Comida* (Servicio de alimentación)

_Escribe el número o el nombre del área._"""
    
    def _handle_seleccionar_bienestar(self, phone_number, message):
        """Maneja la selección de bienestar"""
        opcion = self._extract_first_int(message)
        if opcion is None:
            categoria = self._infer_bienestar_categoria(message)
            if categoria == 'deportes':
                opcion = 1
            elif categoria == 'area_cultural':
                opcion = 2
            elif categoria == 'comida':
                opcion = 3
        if opcion is None:
            self._set_pregunta_pendiente(phone_number, message)
            return "❌ Por favor escribe el tema que deseas consultar (deportes, área cultural o comida).", None
        
        if opcion == 1:
            # Deportes
            self.analytics.registrar_opcion_bienestar('deportes', 'menu')
            self.session_manager.update_session(
                phone_number,
                estado='bienestar_deportes',
                datos_temporales={'categoria_bienestar': 'deportes'}
            )
            return self.info_bienestar['deportes']['info'], None
        
        elif opcion == 2:
            # Área Cultural
            self.analytics.registrar_opcion_bienestar('area_cultural', 'menu')
            self.session_manager.update_session(
                phone_number,
                estado='bienestar_area_cultural',
                datos_temporales={'categoria_bienestar': 'area_cultural'}
            )
            return self.info_bienestar['area_cultural']['info'], None
        
        elif opcion == 3:
            # Comida
            self.analytics.registrar_opcion_bienestar('comida', 'menu')
            self.session_manager.update_session(
                phone_number,
                estado='bienestar_comida',
                datos_temporales={'categoria_bienestar': 'comida'}
            )
            info_comida = self.info_bienestar.get('comida', {})
            texto = info_comida.get('info', '🍽️ *Comida*\n\nInformación no disponible.')
            self.session_manager.update_session(
                phone_number,
                estado='confirmar_otro_bienestar'
            )
            return f"{texto}\n\n¿Deseas consultar otra opción de bienestar? Responde sí o no.", None
        
        else:
            self._set_pregunta_pendiente(phone_number, message)
            return "No entendí el tema de bienestar. ¿Deseas deportes, área cultural o comida?", None
    
    def _handle_bienestar_deportes(self, phone_number, message):
        """Maneja la selección de un deporte específico"""
        detalles = self.info_bienestar['deportes']['detalles']

        if self._is_list_request(message):
            return self.info_bienestar['deportes']['info'], None

        text = self._normalize_text(message)
        opcion = message if message in detalles else self._deportes_map.get(text)
        if opcion in detalles:
            genero = self._infer_genero(message)
            session = self.session_manager.get_session(phone_number)
            genero_guardado = session.get('datos_temporales', {}).get('genero')
            genero = genero or genero_guardado

            info_deporte = detalles[opcion]

            if isinstance(info_deporte, dict):
                if genero is None:
                    self.session_manager.update_session(
                        phone_number,
                        estado='bienestar_deportes_genero',
                        datos_temporales={'categoria_bienestar': 'deportes', 'deporte_pendiente': opcion}
                    )
                    return "Antes de continuar, ¿eres hombre o mujer? (masculino/femenino)", None

                info_deporte = info_deporte.get(genero)
                if not info_deporte:
                     return "❌ Lo siento, no tengo información específica de ese género para este deporte.", None

            # Analytics
            self.analytics.registrar_opcion_bienestar('deportes', opcion)
            
            self.session_manager.update_session(
                phone_number,
                estado='confirmar_otro_bienestar'
            )
            return f"{info_deporte}\n\n¿Deseas consultar otro deporte o área de bienestar? Responde sí o no.", None
        
        self._set_pregunta_pendiente(phone_number, message)
        return "❌ Deporte no encontrado. Por favor selecciona el número (1-10) o escribe el nombre del deporte.", None

    def _handle_bienestar_deportes_genero(self, phone_number, message):
        """Maneja la selección de género para deportes"""
        genero = self._infer_genero(message)
        if not genero:
            return "❌ Por favor responde *masculino* o *femenino*.", None
        
        session = self.session_manager.get_session(phone_number)
        opcion = session['datos_temporales'].get('deporte_pendiente')
        
        # Guardar genero para futuro
        datos = session['datos_temporales']
        datos['genero'] = genero
        
        self.session_manager.update_session(
            phone_number, 
            datos_temporales=datos,
            estado='bienestar_deportes'
        )
        
        return self._handle_bienestar_deportes(phone_number, opcion)

    def _handle_bienestar_area_cultural(self, phone_number, message):
        """Maneja la selección de actividad cultural"""
        detalles = self.info_bienestar['area_cultural']['detalles']
        
        if self._is_list_request(message):
            return self.info_bienestar['area_cultural']['info'], None

        text = self._normalize_text(message)
        opcion = message if message in detalles else self._cultural_map.get(text)
        
        if opcion in detalles:
            # Analytics
            self.analytics.registrar_opcion_bienestar('area_cultural', opcion)
            
            self.session_manager.update_session(
                phone_number,
                estado='confirmar_otro_bienestar'
            )
            return f"{detalles[opcion]}\n\n¿Deseas consultar otra actividad cultural o área de bienestar? Responde sí o no.", None
        
        self._set_pregunta_pendiente(phone_number, message)
        return "❌ Actividad no encontrada. Por favor selecciona el número (1-7) o escribe el nombre de la actividad.", None

    def _handle_confirmar_otro_bienestar(self, phone_number, message):
        """Pregunta si desea consultar más bienestar"""
        respuesta = self._parse_yes_no(message)
        if respuesta is True:
            self.session_manager.update_session(phone_number, estado='seleccionar_bienestar')
            return self._menu_bienestar(), None
        elif respuesta is False:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None
        else:
            return "❌ Por favor responde *sí* o *no*.", None

    # ========== FUNCIONES PARA REQUISITOS ==========

    def _menu_requisitos(self):
        """Retorna el menú de requisitos"""
        return """⚖️ *Requisitos de Materias*

¿Qué deseas consultar?

1. Buscar requisito por *Nombre de Materia*
2. Ver materias por *Semestre*

_Escribe el número de la opción o lo que buscas._"""

    def _handle_seleccionar_requisitos(self, phone_number, message):
        """Maneja la selección inicial de requisitos"""
        opcion = self._extract_first_int(message)
        if opcion == 1:
            self.session_manager.update_session(phone_number, estado='requisitos_buscar_materia')
            return "📋 Escribe el nombre de la materia que deseas consultar:", None
        elif opcion == 2:
            self.session_manager.update_session(phone_number, estado='requisitos_elegir_programa')
            return self._menu_pensum(), None
        else:
            # Intentar buscar directamente
            matches = self._find_materia_matches(message)
            if matches:
                return self._handle_requisitos_por_materia(phone_number, matches)
            
            return "❌ Opción no válida. Elige 1 (Nombre) o 2 (Semestre).", None

    def _handle_requisitos_buscar_materia(self, phone_number, message):
        """Busca requisitos por nombre de materia"""
        matches = self._find_materia_matches(message)
        if not matches:
            self._registrar_no_entendida(phone_number, 'requisitos_buscar_materia', message)
            return "❌ No encontré ninguna materia con ese nombre. Intenta con otro nombre o escribe *menu* para salir.", None
        
        return self._handle_requisitos_por_materia(phone_number, matches)

    def _handle_requisitos_por_materia(self, phone_number, matches):
        """Procesa y muestra los resultados de búsqueda de materias"""
        if len(matches) == 1:
            m = matches[0]
            # Analytics
            self.analytics.registrar_interaccion(
                phone_number=phone_number,
                estado='requisitos_materia',
                opcion_elegida=m['materia'],
                categoria='requisitos',
                subcategoria=m['programa_nombre'],
                mensaje_usuario=m['materia']
            )
            
            self.session_manager.update_session(phone_number, estado='confirmar_otra_asignatura')
            res = f"📘 *Carrera:* {m['programa_nombre']}\n"
            res += f"🗓️ *Semestre:* {m['semestre']}\n"
            res += f"📌 *Materia:* {m['materia']}\n"
            res += f"✅ *Requisito:* {m['requisito']}\n\n"
            res += "¿Deseas consultar otra materia? Responde con sí o no."
            return res, None
        
        # Múltiples resultados
        resp = "🔍 Encontré varias materias similares en diferentes programas:\n\n"
        for i, m in enumerate(matches[:5], 1):
            resp += f"{i}. *{m['materia']}* ({m['programa_nombre']} - Sem {m['semestre']})\n"
        
        resp += "\nEscribe el número de la opción que buscas o escribe de nuevo el nombre con más detalle."
        self.session_manager.update_session(
            phone_number, 
            estado='requisitos_elegir_opcion_multiple',
            datos_temporales={'opciones_materias': matches[:5]}
        )
        return resp, None

    def _menu_semestres_programa(self, programa_key):
        """Retorna menú de semestres"""
        nombre = self._programas_labels.get(programa_key, 'Programa')
        return f"📚 *{nombre}*\n\n¿De qué semestre deseas ver las materias? (Escribe el número del 1 al 9)"

    def _handle_requisitos_elegir_programa(self, phone_number, message):
        """Primer paso para ver materias por semestre: elegir programa"""
        programa_key = self._infer_programa_key(message)
        if programa_key == 'sistema':
            programa_key = 'sistemas'
            
        if programa_key in self.requisitos_programas:
            self.session_manager.update_session(
                phone_number,
                estado='requisitos_semestre',
                datos_temporales={'programa_req': programa_key}
            )
            return self._menu_semestres_programa(programa_key), None
        
        return "❌ Programa no reconocido. Por favor elige de la lista (Sistemas, Industrial, Civil, Eléctrica, Electromecánica).", None

    def _handle_requisitos_elegir_programa_semestre(self, phone_number, message):
        """Maneja el caso donde el usuario ya dio el semestre pero falta el programa"""
        programa_key = self._infer_programa_key(message)
        if programa_key == 'sistema':
            programa_key = 'sistemas'
            
        if programa_key in self.requisitos_programas:
            session = self.session_manager.get_session(phone_number)
            semestre = session['datos_temporales'].get('semestre_consulta')
            texto = self._build_materias_semestre_text(programa_key, semestre)
            self.session_manager.update_session(phone_number, estado='confirmar_otra_asignatura')
            return f"{texto}\n\n¿Deseas consultar otro semestre o materia? Responde sí o no.", None
        
        return "❌ Por favor elige el programa (Sistemas, Industrial, Civil, etc.) para mostrarte las materias.", None

    def _handle_requisitos_semestre(self, phone_number, message):
        """Muestra materias del semestre seleccionado"""
        semestre = self._extract_first_int(message)
        if semestre is None or semestre < 1 or semestre > 10:
            return "❌ Por favor escribe un número de semestre válido (1-9).", None
        
        session = self.session_manager.get_session(phone_number)
        programa_key = session['datos_temporales'].get('programa_req')
        
        texto = self._build_materias_semestre_text(programa_key, semestre)
        
        self.session_manager.update_session(
            phone_number,
            estado='requisitos_materia',
            datos_temporales={'semestre_req': semestre}
        )
        
        return f"{texto}\n\nEscribe el *nombre de la materia* para ver sus requisitos o escribe *volver* para elegir otro semestre.", None

    def _handle_requisitos_materia(self, phone_number, message):
        """Muestra el requisito de una materia específica del semestre"""
        if message.lower() in ['volver', 'regresar']:
            session = self.session_manager.get_session(phone_number)
            prog = session['datos_temporales'].get('programa_req')
            self.session_manager.update_session(phone_number, estado='requisitos_semestre')
            return self._menu_semestres_programa(prog), None
            
        matches = self._find_materia_matches(message)
        if not matches:
             return "❌ No encontré esa materia. Intenta escribir el nombre completo tal como aparece arriba.", None
        
        # Filtrar por el programa y semestre actual para ser precisos
        session = self.session_manager.get_session(phone_number)
        prog_act = session['datos_temporales'].get('programa_req')
        sem_act = session['datos_temporales'].get('semestre_req')
        
        # Priorizar coincidencia exacta en este contexto
        exact_match = None
        for m in matches:
            if m['programa'] == prog_act and m['semestre'] == sem_act:
                exact_match = m
                break
        
        m = exact_match or matches[0]
        
        # Analytics
        self.analytics.registrar_interaccion(
            phone_number=phone_number,
            estado='requisitos_materia',
            opcion_elegida=m['materia'],
            categoria='requisitos',
            subcategoria=m['programa_nombre'],
            mensaje_usuario=m['materia']
        )
        
        self.session_manager.update_session(phone_number, estado='confirmar_otra_asignatura')
        res = f"📘 *Carrera:* {m['programa_nombre']}\n"
        res += f"🗓️ *Semestre:* {m['semestre']}\n"
        res += f"📌 *Materia:* {m['materia']}\n"
        res += f"✅ *Requisito:* {m['requisito']}\n\n"
        res += "¿Deseas consultar otra materia? Responde con sí o no."
        return res, None

    def _handle_confirmar_otra_asignatura(self, phone_number, message):
        """Pregunta si desea consultar más requisitos"""
        respuesta = self._parse_yes_no(message)
        if respuesta is True:
            self.session_manager.update_session(phone_number, estado='seleccionar_requisitos')
            return self._menu_requisitos(), None
        elif respuesta is False:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None
        else:
            return "❌ Por favor responde *sí* o *no*.", None

    # ========== FUNCIONES PARA MATRÍCULA ==========

    def _handle_matricula_paso(self, phone_number, message):
        """Maneja el flujo de pasos de matrícula"""
        text = self._normalize_text(message)
        if 'siguiente' not in text and 'continuar' not in text:
            return "❌ Escribe *siguiente* para ver el siguiente paso o *menu* para salir.", None
            
        session = self.session_manager.get_session(phone_number)
        paso_actual = session['datos_temporales'].get('paso_actual', 1)
        
        info = self.info_matricula[1] # Por ahora solo tenemos la opción 1
        pasos = info['pasos']
        
        if paso_actual > len(pasos):
             self.session_manager.update_session(phone_number, estado='confirmar_otra_matricula')
             return "Has visto todos los pasos. ¿Deseas consultar algo más de matrícula? sí/no", None
             
        idx = paso_actual - 1
        self.session_manager.update_session(
            phone_number,
            datos_temporales={'paso_actual': paso_actual + 1}
        )
        
        msg = f"*Paso {paso_actual} de {len(pasos)}*\n\n{pasos[idx]['texto']}"
        if paso_actual < len(pasos):
            msg += "\n\n_Escribe *siguiente* para continuar_"
        else:
            msg += "\n\n_Fin del proceso. Escribe *menu* para volver._"
            self.session_manager.update_session(phone_number, estado='confirmar_otra_matricula')

        return msg, pasos[idx]['imagen']

    def _handle_confirmar_otra_matricula(self, phone_number, message):
        """Pregunta si desea más info de matrícula"""
        respuesta = self._parse_yes_no(message)
        if respuesta is True:
            self.session_manager.update_session(phone_number, estado='menu_principal') # Por ahora vuelve al menu
            return "Dime, ¿qué otra duda tienes sobre el proceso de ingreso o adición de materias?", None
        elif respuesta is False:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None
        else:
            return "❌ Por favor responde *sí* o *no*.", None

    # ========== FUNCIONES PARA POSGRADOS ==========

    def _menu_posgrados(self):
        """Retorna el menú de posgrados"""
        return """🎓 *Posgrados UNISINU*

¿Qué nivel de estudio le interesa?

1. Doctorados
2. Maestrías
3. Especializaciones

_Escribe el número de la opción o el nombre._"""

    def _handle_menu_posgrados(self, phone_number, message):
        """Maneja la selección inicial de posgrados"""
        opcion = self._extract_first_int(message)
        if opcion is None:
            opcion = self._infer_posgrado_tipo(message)
        
        niveles = {1: 'doctorados', 2: 'maestrias', 3: 'especializaciones'}
        
        if opcion in niveles:
            nivel = niveles[opcion]
            self.session_manager.update_session(
                phone_number,
                estado='seleccionar_tipo_posgrado',
                datos_temporales={'tipo_posgrado': nivel}
            )
            
            resp = f"🎓 *{nivel.upper()}*\n\n"
            for i, p in enumerate(self.info_posgrados[nivel], 1):
                resp += f"{i}. {p['nombre']}\n"
            
            resp += "\nEscribe el número para ver detalles o *volver* para cambiar de nivel."
            return resp, None
            
        return "❌ Opción no válida. Elige 1 (Doctorados), 2 (Maestrías) o 3 (Especializaciones).", None

    def _handle_seleccionar_tipo_posgrado(self, phone_number, message):
        """Muestra detalles del posgrado elegido"""
        if message.lower() in ['volver', 'regresar']:
            self.session_manager.update_session(phone_number, estado='menu_posgrados')
            return self._menu_posgrados(), None
            
        opcion = self._extract_first_int(message)
        session = self.session_manager.get_session(phone_number)
        nivel = session['datos_temporales'].get('tipo_posgrado')
        
        programas = self.info_posgrados.get(nivel, [])
        if opcion and 1 <= opcion <= len(programas):
            p = programas[opcion-1]
            
            # Analytics
            self.analytics.registrar_interaccion(
                phone_number=phone_number,
                estado='posgrados_detalle',
                opcion_elegida=p['nombre'],
                categoria='posgrados',
                subcategoria=nivel,
                mensaje_usuario=p['nombre']
            )
            
            resp = f"🎓 *{p['nombre']}*\n\n"
            resp += f"⏳ *Duración:* {p['duracion']}\n"
            resp += f"💰 *Costo:* {p['costo']}\n\n"
            resp += "¿Deseas consultar otro posgrado? sí/no"
            
            self.session_manager.update_session(phone_number, estado='confirmar_otro_posgrado')
            return resp, None
            
        return f"❌ Por favor selecciona un número del 1 al {len(programas)}.", None

    def _handle_confirmar_otro_posgrado(self, phone_number, message):
        """Pregunta si desea ver más posgrados"""
        respuesta = self._parse_yes_no(message)
        if respuesta is True:
            self.session_manager.update_session(phone_number, estado='menu_posgrados')
            return self._menu_posgrados(), None
        elif respuesta is False:
            self.session_manager.update_session(phone_number, estado='menu_principal')
            return self._menu_principal(), None
        else:
            return "❌ Por favor responde *sí* o *no*.", None

    def _ejecutar_funcion_con_captura(self, func):
        """
        Ejecuta una función de los módulos antiguos que usan print() 
        y captura su salida para enviarla por WhatsApp
        """
        import io
        from contextlib import redirect_stdout
        
        f = io.StringIO()
        with redirect_stdout(f):
            try:
                # Estas funciones suelen pedir input, aquí fallarían
                # Deberían ser refactorizadas para no ser interactivas
                # Por ahora solo llamamos si sabemos que no pide input inmediato
                func() 
            except Exception as e:
                return f"Error al obtener información: {str(e)}"
        
        return f.getvalue()
