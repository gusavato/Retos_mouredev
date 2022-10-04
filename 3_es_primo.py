# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def es_primo(p):
    for n in range(2, p - 1):
        if p % n == 0:
            return False
    return True


for i in range(1, 101):
    if es_primo(i):
        print(i)
