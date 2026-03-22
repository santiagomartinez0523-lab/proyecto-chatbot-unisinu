import re
import unicodedata
from PIL import Image

# Versión simplificada para legibilidad en un solo archivo
# En el proyecto final, esto se divide en módulos

# --- UTILS ---
def normalize_text(text):
    text = text.strip().lower()
    text = unicodedata.normalize('NFD', text)
    return ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')

def extract_number(text):
    match = re.search(r'\d+', text)
    return int(match.group()) if match else None

# --- PROGRAM LOGICS (PROXIES) ---
def funcion_sistema():
    print("Consultando Requisitos de Sistemas...")
    # Lógica de sistema.py
    pass

def funcion_industrial():
    print("Consultando Requisitos de Industrial...")
    # Lógica de industrial.py
    pass

# --- MAIN FLOW ---
def main():
    print("\nBienvenido al Chatbot Académico (Local Console Mode)")
    
    while True:
        print("\n¿En qué puedo ayudarte?")
        print("1. Pensum\n2. Matrícula\n3. Posgrados\n4. Bienestar\n5. Salir")
        
        opcion = extract_number(input("Elige una opción: "))
        
        if opcion == 1:
            print("Selecciona programa: 1.Sistemas 2.Industrial 3.Civil 4.Eléctrica 5.Electromecánica")
            prog = extract_number(input("Programa: "))
            if prog == 1:
                img = Image.open("image/Ing_sistema.png")
                img.show()
                # ...
        elif opcion == 5:
            break

if __name__ == "__main__":
    main()
