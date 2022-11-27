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

def check_delimiter(expresion):
    delimiter = {'[': ']', '{': '}', '(': ')'}
    for pos, char in enumerate(expresion):
        if char in delimiter.keys():
            if delimiter.get(char) in expresion[pos:]:
                delimiter_end = expresion.index(delimiter.get(char))
                if set(expresion[pos + 1:delimiter_end]) & (set(delimiter.keys() | set(delimiter.values()))):
                    check_delimiter(expresion[pos + 1:delimiter_end])
                else:
                    break
            else:
                print('Expresión NO EQUILIBRADA no se ha encontrado el caracter {} de cierre\n{}'.
                      format(delimiter[char], expresion))
                return False
        elif char in delimiter.values():
            print('Expresión NO EQUILIBRADA no se ha encontrado el caracter {} de apertura\n{}'.
                  format(list(delimiter.keys())[list(delimiter.values()).index(char)], expresion))
            return False
    print('Expresión EQUILIBRADA')
    return True


expr = input('Introducir expresión:\n')
check_delimiter(expr)
