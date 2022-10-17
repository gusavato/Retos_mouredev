# Crea un programa que invierta el orden de una cadena de texto
# sin usar funciones propias del lenguaje que lo hagan de forma automática.
# - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

cadena = input('Introduzca cadena de texto a invertir: ')

cadena_inv = list(cadena)
cadena_inv = "".join(cadena_inv[::-1])

print(cadena_inv)
