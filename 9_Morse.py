# Reto #9
# CÓDIGO MORSE
# Fecha publicación enunciado: 02/03/22
# Fecha publicación resolución: 07/03/22
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

import pandas as pd
import numpy as np


def is_morse(txt):
    if type(txt) != str:
        print("No se ha introducido una cadena de texto \nFIN DEL PROGRAMA")
        return False
    elif set(txt).issubset({'.', '-', ' '}):
        return True
    else:
        return False


def morse_trad(txt):
    trad_list = []
    if is_morse(txt):
        for word in txt.split('  '):
            trad_word = ''
            for character in word.split():
                trad_word += list(morse.keys())[list(morse.values()).index(character)]
            trad_list.append(trad_word)
    else:
        for word in txt.split(' '):
            trad_word = ''
            for character in list(word):
                trad_word += morse[character] + ' '
            trad_list.append(trad_word)
    return " ".join(trad_list)


# Importamos desde la wikipedia la tabla de código morse y la formateamos
wiki_morse = pd.read_html('https://es.wikipedia.org/wiki/C%C3%B3digo_morse')
wiki_morse[2] = wiki_morse[2].set_axis(list(range(0, wiki_morse[2].shape[1])), axis=1, copy=False)

# Creamos un diccionario con todos los carácteres morse
morse = dict()
for i in range(0, wiki_morse[2].shape[1], 3):
    morse.update(dict(wiki_morse[2].loc[:, i:i + 1].values.tolist()))
morse.pop(np.nan)
# Los carácteres de Wikipedia no coinciden con los caracteres ASCII de . y -
for key_morse in morse.keys():
    morse[key_morse] = morse[key_morse].replace(' ', '')
    morse[key_morse] = morse[key_morse].replace('·', '.')
    morse[key_morse] = morse[key_morse].replace('—', '-')

input_text = input('Introduzca el texto a traducir:\n')

print("La cadena introducida {cod}. Su traducción es la siguinte:"
      "\n{trad}".format(cod='es morse' if is_morse(input_text) else 'no es morse',
                        trad=morse_trad(input_text)))
