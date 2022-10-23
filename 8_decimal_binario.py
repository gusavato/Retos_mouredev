# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def a_binario(dec):
    binary = ''
    while binary != 1:
        binary += str(dec % 2)
        dec = dec // 2
    return int(binary)


print(a_binario(10))
