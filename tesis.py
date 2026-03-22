import re
import unicodedata
from PIL import Image
from programas.sistema import funcion_sistema 
from programas.industrial import funcion_industrial
from programas.civil import funcion_civil
from programas.electrica import funcion_electrica
from programas.electromecanica import funcion_electromecanica
from bienestar.deportes import funcion_deportes
from bienestar.area_cultural import funcion_area_cultural
from bienestar.comida import funcion_comida
from posgrados import funcion_posgrados
from matricula import funcion_matriculas


def _normalize_text(text):
    text = text.strip().lower()
    text = unicodedata.normalize('NFD', text)
    return ''.join(ch for ch in text if unicodedata.category(ch) != 'Mn')


def _extract_first_int(text):
    match = re.search(r'\d+', text)
    return int(match.group()) if match else None


def _infer_main_intent(message):
    text = _normalize_text(message)
    number = _extract_first_int(text)
    if number in range(1, 9):
        return number

    if any(k in text for k in ['pensum', 'plan de estudios', 'malla curricular']):
        return 1
    if any(k in text for k in ['matricula', 'inscripcion', 'inscribir', 'baja', 'ingresar materia']):
        return 2
    if any(k in text for k in ['posgrado', 'maestria', 'doctorado', 'especializacion']):
        return 3
    if any(k in text for k in ['curso de ingles', 'curso de espanol', 'ingles', 'espanol']):
        return 4
    if any(k in text for k in ['bienestar', 'deporte', 'cultural', 'comida', 'alimentacion']):
        return 5
    if any(k in text for k in ['tutoria', 'tutorias']):
        return 6
    if any(k in text for k in ['semillero', 'investigacion']):
        return 7
    if any(k in text for k in ['requisito', 'prerrequisito', 'correlativo', 'materia requisito']):
        return 8

    return None


def _infer_programa(message):
    text = _normalize_text(message)
    if 'sistema' in text or 'sistemas' in text:
        return 1
    if 'industrial' in text:
        return 2
    if 'civil' in text:
        return 3
    if 'electrica' in text or 'electrico' in text:
        return 4
    if 'electromecanica' in text or 'electromecanico' in text:
        return 5
    return None


def _infer_bienestar(message):
    text = _normalize_text(message)
    if 'deporte' in text or 'deportes' in text:
        return 1
    if 'cultural' in text or 'cultura' in text:
        return 2
    if 'comida' in text or 'alimentacion' in text or 'cafeteria' in text:
        return 3
    return None


def _parse_yes_no(message):
    text = _normalize_text(message)
    if text in ['si', 'sí', 's', 'claro', 'ok', 'vale', 'yes']:
        return True
    if text in ['no', 'n', 'nop', 'nope']:
        return False
    return None



def main():
    while True:
        print("\nCual es el motivo de su solicitud?\n")
        print("Escribe tu consulta (ej: pensum, matrícula, posgrados, bienestar, requisitos).")
        mensaje = input("Consulta: ").strip()

        if not mensaje:
            print("Entrada vacía. Intenta de nuevo.")
            continue

        opcion = _infer_main_intent(mensaje)
        if opcion is None:
            print("No entendí tu solicitud. Escribe algo como 'pensum', 'matrícula' o 'bienestar'.")
            continue

        match opcion:
            case 1:
                print('¿Qué pensum de programa deseas saber? (Sistemas, Industrial, Civil, Eléctrica o Electromecánica)')
                msg_programa = input("Programa: ").strip()
                opcion_1 = _extract_first_int(msg_programa)
                if opcion_1 is None:
                    opcion_1 = _infer_programa(msg_programa)
                if opcion_1 not in [1, 2, 3, 4, 5]:
                    print("Programa no válido.")
                    continue

                match opcion_1:
                    case 1:
                        print("Mostrando pensum de Ingeniería de Sistemas...")
                        img = Image.open("image/Ing_sistema.png")
                        img.show()
                        print('Deseas verificar algun requisito de una materia?.')
                        print('1. Deseo verificar el requisito de una materia')
                        print('2. No deseo verificar ningun requisito')

                        resp = input("¿Deseas verificar requisitos? (sí/no): ").strip()
                        opcion2 = 1 if _parse_yes_no(resp) is True else 2 if _parse_yes_no(resp) is False else None
                        if opcion2 is None:
                            print("Respuesta no válida.")
                            continue

                        match opcion2:
                            case 1:
                                funcion_sistema()
                            case 2:
                                print("Ok, regresando al menú principal...")
                                continue  # Vuelve al menú principal

                    case 2:
                        print("Mostrando pensum de Ingeniería Industrial...")
                        img = Image.open("image/ing_industrial.png")
                        img.show()
                        print('Deseas verificar algun requisito de una materia?.')
                        print('1. Deseo verificar el requisito de una materia')
                        print('2. No deseo verificar ningun requisito')

                        resp = input("¿Deseas verificar requisitos? (sí/no): ").strip()
                        opcion2 = 1 if _parse_yes_no(resp) is True else 2 if _parse_yes_no(resp) is False else None
                        if opcion2 is None:
                            print("Respuesta no válida.")
                            continue

                        match opcion2:
                            case 1:
                                funcion_industrial()
                            case 2:
                                print("Ok, regresando al menú principal...")
                                continue

                    case 3:
                        print("Mostrando pensum de Ingeniería Civil...")
                        img = Image.open("image/ing_civil.png")
                        img.show()
                        print('Deseas verificar algun requisito de una materia?.')
                        print('1. Deseo verificar el requisito de una materia')
                        print('2. No deseo verificar ningun requisito')

                        resp = input("¿Deseas verificar requisitos? (sí/no): ").strip()
                        opcion2 = 1 if _parse_yes_no(resp) is True else 2 if _parse_yes_no(resp) is False else None
                        if opcion2 is None:
                            print("Respuesta no válida.")
                            continue

                        match opcion2:
                            case 1:
                                funcion_civil()
                            case 2:
                                print("Ok, regresando al menú principal...")
                                continue

                    case 4:
                        print("Mostrando pensum de Ingeniería Eléctrica...")
                        img = Image.open("image/ing_electrica.png")
                        img.show()
                        print('Deseas verificar algun requisito de una materia?.')
                        print('1. Deseo verificar el requisito de una materia')
                        print('2. No deseo verificar ningun requisito')

                        resp = input("¿Deseas verificar requisitos? (sí/no): ").strip()
                        opcion2 = 1 if _parse_yes_no(resp) is True else 2 if _parse_yes_no(resp) is False else None
                        if opcion2 is None:
                            print("Respuesta no válida.")
                            continue

                        match opcion2:
                            case 1:
                                funcion_electrica()
                            case 2:
                                print("Ok, regresando al menú principal...")
                                continue

                    case 5:
                        print("Mostrando pensum de Ingeniería Electromecánica...")
                        img = Image.open("image/ing_electromecanica.png")
                        img.show()
                        print('Deseas verificar algun requisito de una materia?.')
                        print('1. Deseo verificar el requisito de una materia')
                        print('2. No deseo verificar ningun requisito')

                        resp = input("¿Deseas verificar requisitos? (sí/no): ").strip()
                        opcion2 = 1 if _parse_yes_no(resp) is True else 2 if _parse_yes_no(resp) is False else None
                        if opcion2 is None:
                            print("Respuesta no válida.")
                            continue

                        match opcion2:
                            case 1:
                                funcion_electromecanica()
                            case 2:
                                print("Ok, regresando al menú principal...")
                                continue

                    case _:
                        print("Opción de pensum no válida")
                        continue
            case 2:
                funcion_matriculas()
            case 3:
                funcion_posgrados()
            case 5:
                print("¿Qué deseas saber del Bienestar? (Deportes, Área Cultural o Comida)")
                msg_bienestar = input("Bienestar: ").strip()
                opcion_bienestar = _extract_first_int(msg_bienestar)
                if opcion_bienestar is None:
                    opcion_bienestar = _infer_bienestar(msg_bienestar)
                if opcion_bienestar not in [1, 2, 3]:
                    print("Opción no válida")
                    continue

                match opcion_bienestar:
                    case 1:
                        funcion_deportes()
                    case 2:
                        funcion_area_cultural()
                    case 3:
                        funcion_comida()
                    case _:
                        print("Opción no válida")

            case _:
                print("Opción no válida")
                continue


if __name__ == "__main__":
    main()
