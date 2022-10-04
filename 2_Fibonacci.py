#
# Escribe un programa que imprima los 50 primeros números de la sucesión
# de Fibonacci empezando en 0.
# - La serie Fibonacci se compone por una sucesión de números en
#   la que el siguiente siempre es la suma de los dos anteriores.
#   0, 1, 1, 2, 3, 5, 8, 13...
# /
fib = []
for i in range(51):
    if i <= 1:
        fib.append(i)
        print(i)
        continue
    fib.append(fib[-1] + fib[-2])
    print(fib[-1])
