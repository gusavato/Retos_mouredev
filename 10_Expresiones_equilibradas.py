# Reto #10
# EXPRESIONES EQUILIBRADAS
# Fecha publicación enunciado: 07/03/22
# Fecha publicación resolución: 14/03/22
# Dificultad: MEDIA

# Enunciado: Crea un programa que comprueba si los paréntesis,
# llaves y corchetes de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# - Expresión balanceada: { [ a #( c + d ) ] - 5 }
# - Expresión no balanceada: { a #( c + d ) ] - 5 }


def check_delimiter():
    expresion = input('Introducir expresión:\n')
    delimiters = {'[': ']', '{': '}', '(': ')'}
    list_delimiters = []
    for char in expresion:
        if char in delimiters.keys():
            list_delimiters.append(char)
        elif char in delimiters.values():
            if list(delimiters.keys())[list(delimiters.values()).index(char)] == list_delimiters[-1]:
                list_delimiters.pop()
            else:
                return False
    if not list_delimiters:
        return True
    else:
        return False


print(check_delimiter())
