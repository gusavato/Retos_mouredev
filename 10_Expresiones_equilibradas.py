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


def extract_delimiters(exp: object, delim: object) -> list:
    exp_delim = []
    for char in exp:
        if char in delim.values() | delim.keys():
            exp_delim.append(char)
    return exp_delim


def get_delimiters_count(delimiter_list,delimiters):
    count = dict()
    for k, v in delimiters.items():
        delimiter_count[k] = delimiter_list.count(k)
        delimiter_count.update({v: delimiter_list.count(v)})
    return count

def open_equal_close(delimiter_list,delimiters):
    delimiters_count = get_delimiters_count(delimiter_list, delimiters)
    for k, v in delimiters.items():
        if delimiters_count.get(k) == delimiters_count.get(v):
            continue
        else:
            return False
    return True


def check_delimiter():
    expresion = input('Introducir expresión:\n')
    delimiters = {'[': ']', '{': '}', '(': ')'}
    exp_delim = extract_delimiters(expresion, delimiters)
    if open_equal_close(exp_delim,delimiters):




check_delimiter()
