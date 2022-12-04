# Reto #11
# ELIMINANDO CARACTERES
# Fecha publicación enunciado: 14/03/22
# Fecha publicación resolución: 21/03/22
# Dificultad: FÁCIL

# Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2)
# e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.

def replace(strn, set_out) -> str:
    out = str()
    for char in strn:
        if char in set_out:
            continue
        else:
            out += char
    return out


def discard_char(str1: str, str2: str) -> tuple:
    set_out1 = set(str1) - set(str2)
    set_out2 = set(str2) - set(str1)
    out1 = replace(str1, set_out1)
    out2 = replace(str2, set_out2)
    return out1, out2


# TEST

print(discard_char('Hola amigo', 'Hola'))
