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

from datetime import datetime, timedelta


def date_transform(str_date: str) -> datetime:
    d, m, y = map(int, str_date.split('/'))
    return datetime.date(day=d, month=m, year=y)


def days_delta(str1: str, str2: str) -> int:
    try:
        day_1 = date_transform(str1)
        day_2 = date_transform(str2)
    except:
        print('Fechas introduciadas incorrectas. Formato admitido "dd/MM/yyyy"')
    return


days_delta('12/10/2022', '10/10/2022')
