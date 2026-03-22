# Proyecto ChatBot UniSinú (Ingenierías)

Este es un asistente virtual desarrollado en Python para la Facultad de Ingeniería de la Universidad del Sinú. El bot permite a los estudiantes consultar pensum, requisitos de materias, información de bienestar universitario, posgrados y procesos de matrícula a través de WhatsApp.

## 🚀 Características

- **Consulta de Pensum:** Visualización de la malla curricular por programa.
- **Requisitos de Materias:** Información detallada sobre prerrequisitos para Ingeniería de Sistemas y otros programas.
- **Bienestar Universitario:** Horarios e información de deportes (fútbol, pesas, taekwondo, etc.) y actividades culturales (danza, música, coro).
- **Proceso de Matrícula:** Guía paso a paso asistida por imágenes para la inscripción de materias.
- **Posgrados:** Información sobre doctorados, maestrías y especializaciones.
- **Análisis de Uso:** Sistema integrado para rastrear consultas populares y actividad de usuarios.

## 🛠️ Tecnologías

- **Lenguaje:** Python 3.x
- **Framework Web:** Flask (para el Webhook)
- **Comunicación:** Twilio API for WhatsApp
- **Base de Datos:** SQLite (para analíticas)
- **Librerías principales:** Twilio, Flask, Python-dotenv, Pillow (PIL), Pandas.

## 📂 Estructura del Proyecto

- `whatsapp_bot.py`: Punto de entrada principal para el servidor Flask/Twilio.
- `menu_handler.py`: Cerebro del bot que gestiona estados y flujos de conversación.
- `session_manager.py`: Gestión de persistencia de sesiones de usuario.
- `programas/`: Lógica específica para cada carrera de ingeniería.
- `bienestar/`: Información sobre deportes y cultura.
- `services/`: Servicio de analíticas y base de datos.
- `*_data.py`: Archivos de datos estructurados para el bot.

## 🔧 Instalación y Configuración

1. Clonar el repositorio.
2. Crear un entorno virtual: `python -m venv venv`.
3. Activar el entorno virtual.
4. Instalar dependencias: `pip install -r requirements.txt`.
5. Configurar el archivo `.env` con las credenciales de Twilio (SID, Token, etc.).
6. Ejecutar localmente con: `python whatsapp_bot.py`.
7. (Opcional) Usar `ngrok` para exponer el servidor local a internet.

## 📊 Analíticas

Para ver las estadísticas de uso del bot, ejecuta:
```bash
python ver_estadisticas.py
```

## ✒️ Autor

**Santiago Martínez**
Repositorio original: [proyecto-chatbot-unisinu](https://github.com/santiagomartinez0523-lab/proyecto-chatbot-unisinu)
