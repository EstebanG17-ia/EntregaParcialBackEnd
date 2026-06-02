from classes.clases import *


class Builder:

    def __init__(self):

        self._esElipse = False

    def configBorde(
        self,
        borde_grosor,
        borde_color
    ):

        self._borde_grosor = borde_grosor
        self._borde_color = borde_color

        return self

    def configColor(self, color):

        self._color_relleno = color

        return self

    def configPosicion(self, x, y):

        self._coord_x = x
        self._coord_y = y

        return self

    def configDimension(
        self,
        width,
        height
    ):

        self._width = width
        self._height = height

        return self

    def esElipse(self):

        self._esElipse = True

        return self

    def build(self):

        datos = {
            "width": self._width,
            "height": self._height,
            "borde_grosor": self._borde_grosor,
            "borde_color": self._borde_color,
            "x": self._coord_x,
            "y": self._coord_y,
            "relleno": self._color_relleno
        }

        if self._esElipse:
            return Elipse(**datos)

        return Cuadrado(**datos)