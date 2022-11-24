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
                check_delimiter(expresion[pos+1:delimiter_end])
            else:
                print('Expresión NO EQUILIBRADA no se ha encontrado el caracter {} de cierre\n'
                      '{}'
                      .format(delimiter.get(char), expresion))
                return False
    print('Expresión EQUILIBRADA')
    return True


check_delimiter('{a * [(b - c)}')


