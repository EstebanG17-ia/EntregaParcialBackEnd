from p5 import *
from random import randint

from classes.clases import *
from patron.Builders import Builder


MAX_WIDTH = 800
MAX_HEIGHT = 700

TOTAL_FIGURAS = 10

figuras = []


def setup():

    size(MAX_WIDTH, MAX_HEIGHT)

    for _ in range(TOTAL_FIGURAS):

        tipo = randint(0, 1)

        x = randint(
            50,
            MAX_WIDTH - 50
        )

        y = randint(
            50,
            MAX_HEIGHT - 50
        )

        figuras.append(
            crearFigura(
                tipo,
                x,
                y
            )
        )


def draw():

    background(220)

    for figura in figuras:

        figura.dibujar()

        figura.desplazar_rebotar(
            MAX_WIDTH,
            MAX_HEIGHT
        )


def crearFigura(tipo, x, y):

    colores = [
        "#463932",
        "#12B85D",
        "#2196F3",
        "#FF9800",
        "#E91E63",
        "#9C27B0",
        "#F44336"
    ]

    color = colores[randint(0, len(colores)-1)]

    tamano = randint(40, 70)

    if tipo == 0:

        return (
            Builder()
            .configBorde(
                randint(1, 4),
                "#000000"
            )
            .configColor(color)
            .configDimension(
                tamano,
                tamano
            )
            .configPosicion(
                x,
                y
            )
            .build()
        )

    return (
        Builder()
        .configBorde(
            randint(1, 4),
            "#000000"
        )
        .configColor(color)
        .configDimension(
            tamano,
            tamano
        )
        .configPosicion(
            x,
            y
        )
        .esElipse()
        .build()
    )


run()