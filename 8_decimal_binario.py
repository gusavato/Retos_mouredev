# Crea un programa se encargue de transformar un número
# decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

def a_binario(dec):
    binario = ''
    while True:
        binario += str(dec % 2)
        dec = dec // 2
        if dec == 1:
            binario += '1'
            break
    return int(binario[::-1])


numero = int(input('Introduzca número para pasar a binanrio: \n'))
print('La expresión en base binaria del número {} es: \n {}'.format(numero, a_binario(numero)))
