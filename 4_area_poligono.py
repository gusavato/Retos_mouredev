# /*
#  * Reto #4
#  * ÁREA DE UN POLÍGONO
#  * Fecha publicación enunciado: 24/01/22
#  * Fecha publicación resolución: 31/01/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  *

def area():
    poligono = input('Poligono:\n'
                     'Triángulo --> T\n'
                     'Rectángulo --> R\n'
                     'Cuadrado --> C\n').lower()
    if poligono == 't':
        altura = float(input('altura del triángulo:\n'))
        base = float(input('base del triángulo:\n'))
        return altura * base / 2
    elif poligono == 'c':
        lado = float(input('lado del cuadrado:\n'))
        return lado ** 2
    elif poligono == 'r':
        altura = float(input('altura del rectángulo:\n'))
        base = float(input('base del rectángulo:\n'))
        return altura * base
    else:
        print('poligono no aceptado')


print(area())
