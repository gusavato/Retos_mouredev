#
# Reto #5
# ASPECT RATIO DE UNA IMAGEN
# Fecha publicación enunciado: 01/02/22
# Fecha publicación resolución: 07/02/22
# Dificultad: DIFÍCIL
#
# Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
# - Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
# - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
# - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920#1080px.

from PIL import Image
from requests import get
from io import BytesIO

url = input('Dirección web de la imagen: ')
imagen_web = get(url)

with Image.open(BytesIO(imagen_web.content)) as imagen:
    ancho, altura = imagen.size

ratio = ancho / altura

print('El aspect ratio de la imagen es: {:,.2f}'.format(ratio))
