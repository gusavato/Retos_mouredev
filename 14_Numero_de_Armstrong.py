# Reto #14
# ¿ES UN NÚMERO DE ARMSTRONG?
# Fecha publicación enunciado: 04/04/22
# Fecha publicación resolución: 11/04/22
# Dificultad: FÁCIL
#
# Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
# Si no conoces qué es un número de Armstrong, debes buscar información al respecto.

def is_armstrong(n: int) -> bool:
    base = len(str(n))
    digits = [int(i) ** base for i in str(n)]
    if sum(digits) == n:
        return True
    else:
        return False


print(is_armstrong(153))
print(is_armstrong(370))
print(is_armstrong(371))
print(is_armstrong(407))
print(is_armstrong(1000))

