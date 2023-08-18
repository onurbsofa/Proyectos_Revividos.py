import pygame as pg
from random import randrange

# Variables Globales
WINDOW = 500
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()# frame rate

# loop principal
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    screen.fill('black')
    pg.display.flip()
    clock.tick(60)