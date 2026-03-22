# Proyecto Chatbot Unisinu

Este es un chatbot de WhatsApp diseñado para asistir a los estudiantes de la Universidad del Sinú (Unisinu) con información académica, procesos de matrícula, bienestar universitario y más.

## 🚀 Características

- **Gestión de Sesiones:** Mantiene el contexto de la conversación para cada usuario.
- **Menús Interactivos:** Navegación sencilla a través de opciones numéricas y palabras clave.
- **Información Académica:** Consulta de pensum y requisitos de materias para programas de ingeniería.
- **Bienestar Universitario:** Información sobre deportes, actividades culturales y servicios de alimentación.
- **Analítica Integrada:** Registro de interacciones para mejora continua y estadísticas de uso.

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Flask:** Micro-framework web para manejar el webhook.
- **Twilio API:** Integración con WhatsApp.
- **SQLite:** Almacenamiento de estadísticas y analítica.
- **Pandas:** Procesamiento de datos para reportes.

## 📦 Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/santiagomartinez0523-lab/proyecto-chatbot-unisinu.git
    cd proyecto-chatbot-unisinu
    ```

2.  **Crear un entorno virtual:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar variables de entorno:**
    Crea un archivo `.env` en la raíz del proyecto con tus credenciales de Twilio:
    ```env
    TWILIO_ACCOUNT_SID=tu_sid
    TWILIO_AUTH_TOKEN=tu_token
    TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
    ```

## 🚀 Ejecución

Para iniciar el servidor del chatbot:

```bash
python whatsapp_bot.py
```

## 📁 Estructura del Proyecto

- `whatsapp_bot.py`: Punto de entrada principal y manejo de rutas Flask.
- `menu_handler.py`: Lógica central de procesamiento de mensajes y menús.
- `session_manager.py`: Gestión de estados de sesión persistentes.
- `requisitos_data.py`: Base de datos de materias y prerrequisitos.
- `services/`: Servicios adicionales como analítica y analytics_service.
- `programas/`: Módulos específicos para cada programa académico.
- `bienestar/`: Módulos relacionados con bienestar universitario.

## 👥 Contribuidores

- Santiago Martinez
