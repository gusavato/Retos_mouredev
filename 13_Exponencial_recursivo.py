# Reto #13
# FACTORIAL RECURSIVO
# Fecha publicación enunciado: 28/03/22
# Fecha publicación resolución: 04/04/22
# Dificultad: FÁCIL
#
# Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

def exponencial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * exponencial(n - 1)


print(exponencial(10))
