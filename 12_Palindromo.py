# Reto #12
# ¿ES UN PALÍNDROMO?
# Fecha publicación enunciado: 21/03/22
# Fecha publicación resolución: 28/03/22
# Dificultad: MEDIA

# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean)
# según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a
# derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.
def accent_mark(string_accent):
    accents, no_accents = 'áéíóúäëïöüàèìòù', 'aeiouaeiouaeiou'
    trans = str.maketrans(accents, no_accents)
    return string_accent.translate(trans)


def is_palindrome(str1: str) -> bool:
    str_pa = str1[::-1].lower()
    str_pa = accent_mark(str_pa)
    if str_pa.replace(' ', '') == accent_mark(str1).lower().replace(' ', ''):
        return True
    else:
        return False


print(is_palindrome('Ana lleva al oso la avellana'))
