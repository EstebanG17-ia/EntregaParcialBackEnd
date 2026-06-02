from p5 import *
from classes.clases import *

cuadrado = None

MAX_WIDTH = 800
MAX_HEIGHT = 700

def setup():
    global cuadrado

    size(MAX_WIDTH, MAX_HEIGHT)

    cuadrado = Figura(
        2,
        "#000000",
        50,
        50,
        50,
        50,
        "#463932"
    )

def draw():
    background(220)

    cuadrado.dibujar()
    cuadrado.desplazar_rebotar(MAX_WIDTH, MAX_HEIGHT)

run()