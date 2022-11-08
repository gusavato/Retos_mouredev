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


def es_morse(txt):
    if type(txt) != str:
        print("No se ha introducido una cadena de texto")
    elif


# Importamos desde la wikipedia la tabla de código morse y la formateamos

wiki_morse = pd.read_html('https://es.wikipedia.org/wiki/C%C3%B3digo_morse')
wiki_morse[2] = wiki_morse[2].set_axis(list(range(0, wiki_morse[2].shape[1])), axis=1, copy=False)

# Creamos un diccionario con todos los morse

morse = dict()
for i in range(0, wiki_morse[2].shape[1], 3):
    morse.update(dict(wiki_morse[2].loc[:, i:i + 1].values.tolist()))
morse.pop(np.nan)
