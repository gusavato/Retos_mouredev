# Reto #15
# ¿CUÁNTOS DÍAS?
# Fecha publicación enunciado: 11/04/22
# Fecha publicación resolución: 18/04/22
# Dificultad: DIFÍCIL
#
# Enunciado: Crea una función que calcule y retorne cuántos días
# hay entre dos cadenas de texto que representen fechas.
# - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# - La función recibirá dos String y retornará un Int.
# - La diferencia en días será absoluta (no importa el orden de las fechas).
# - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

from datetime import date


def str_to_date(str1: str) -> date:
    try:
        d, m, y = map(int, str1.split('/'))
        date_transform = date(day=d, month=m, year=y)
    except SyntaxError:
        "Formato de fecha no válido. Formato correcto 'dd/MM/yyyy'"
    return date_transform


def date_substract(date1: str, date2: str) -> int:
    date_1 = str_to_date(date1)
    date_2 = str_to_date(date2)
    substract = abs(date_1 - date_2)
    return substract.days


date_1 = input('Introduzca fecha 1: \n')
date_2 = input('Introduzca fecha 2: \n')

print(f'La difernecia de días entre {date_1} y {date_2} es: {date_substract(date_1, date_2)} días')
