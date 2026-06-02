from p5 import *
from classes.clases import *

cuadrado = None

def setup():
    global cuadrado

    size(800, 700)

    cuadrado = Figura(
        borde_grosor=2,
        borde_color="#000000",
        width=50,
        height=50,
        x=50,
        y=50,
        relleno="#463932"
    )

def draw():
    background(220)

    cuadrado.dibujar()

run()