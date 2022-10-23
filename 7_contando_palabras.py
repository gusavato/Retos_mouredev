# Crea un programa que cuente cuantas veces se repite cada palabra
# y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que
#   lo resuelvan automáticamente.

import string

# Creamos la lista puntuación con los carácteres de puntuación
puntuacion = list(string.punctuation)

# Solicitamos cadena de texto al usuario
cadena = input('introduzaca cadena de texto: ')

# Cadena de texto para pruebas
# cadena = 'Esto. es una cadena de  .; texto \n' \
#          'con varias, 1234 \n' \
#          'hola Hola hola HOla'

# Creamos la lista lineas con las líneas de la cadena de texto
lineas = cadena.splitlines()

# Creamos la lista palabras con todas las palabras de la cadena, y las pasamos a minúscula
palabras = []

for i in lineas:
    for j in i.split():
        palabra_sin = j.lower()

        # Bucle que revisa si hay signos de puntuación en la palabra
        for punt in puntuacion:
            if punt in palabra_sin:
                palabra_sin = palabra_sin.replace(punt, '')
        palabras.append(palabra_sin)

# Eliminamos los posibles elementos de la lista palabras que sean solo números:
for palabra in palabras:
    if palabra.isdigit():
        palabras.remove(palabra)

# Es posible que el bucle anterior cree un elemento en la lista palabras que sea un string vacío
# (Caracteres de puntuación aislados entre espacios). Por ello aplicamos el remcve en la lista palabras
if '' in palabras:
    palabras.remove('')

# Creamos el diccionario que nos sirva de contador, y le asignamos las repeticiones:
contador = dict()

for palabra in palabras:
    if palabra in contador.keys():
        contador[palabra] += 1
    else:
        contador[palabra] = 1

# Mostramos el resultado por pantalla:
for clave in contador:
    if contador[clave] != 1:
        print('La palabra "{}" se repite {} veces'.format(clave, contador[clave]))
    else:
        print('La palabra "{}" se repite {} vez'.format(clave, contador[clave]))
