from p5 import *

class Borde:
    def __init__(self, grosor, color):
        self.grosor = grosor
        self.color = color


class Dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Posicion:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y


class Figura:
    def __init__(
        self,
        borde_grosor,
        borde_color,
        width,
        height,
        x,
        y,
        relleno
    ):

        self.borde = Borde(borde_grosor, borde_color)
        self.dimension = Dimension(width, height)
        self.posicion = Posicion(x, y)

        self.color_relleno = relleno

    def dibujar(self):

        stroke_weight(self.borde.grosor)
        stroke(self.borde.color)

        fill(self.color_relleno)

        rect(
            self.posicion.coord_x,
            self.posicion.coord_y,
            self.dimension.width,
            self.dimension.height
        )