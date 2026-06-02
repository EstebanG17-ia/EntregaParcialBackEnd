from p5 import *
from random import randint


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

        self.borde = Borde(
            borde_grosor,
            borde_color
        )

        self.dimension = Dimension(
            width,
            height
        )

        self.posicion = Posicion(
            x,
            y
        )

        self.color_relleno = relleno

        self.vel_x = randint(-5, 5)
        self.vel_y = randint(-5, 5)

        if self.vel_x == 0:
            self.vel_x = 1

        if self.vel_y == 0:
            self.vel_y = 1

    def desplazar_rebotar(self, max_x, max_y):

        self.posicion.coord_x += self.vel_x
        self.posicion.coord_y += self.vel_y

        if (
            self.posicion.coord_x <= 0
            or
            self.posicion.coord_x + self.dimension.width >= max_x
        ):
            self.vel_x *= -1

        if (
            self.posicion.coord_y <= 0
            or
            self.posicion.coord_y + self.dimension.height >= max_y
        ):
            self.vel_y *= -1

    def dibujar(self):

        stroke_weight(
            self.borde.grosor
        )

        stroke(
            self.borde.color
        )

        fill(
            self.color_relleno
        )

        rect(
            self.posicion.coord_x,
            self.posicion.coord_y,
            self.dimension.width,
            self.dimension.height
        )


class Cuadrado(Figura):
    pass


class Elipse(Figura):

    def dibujar(self):

        stroke_weight(
            self.borde.grosor
        )

        stroke(
            self.borde.color
        )

        fill(
            self.color_relleno
        )

        ellipse(
            self.posicion.coord_x,
            self.posicion.coord_y,
            self.dimension.width,
            self.dimension.height
        )