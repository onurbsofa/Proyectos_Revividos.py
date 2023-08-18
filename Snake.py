import pygame as pg
from random import randrange

# Variables Globales
WINDOW = 500
TILE_SIZE = 25
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]# funcion para obtener una posicion aleatoria
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])# INSTANCIA DE LA CLASE RECT sera la cabeza de la serpiente
snake.center = get_random_position()
length = 1
snake_body_segments = [snake.copy()]
snake_direction = (0, 0)
time, time_steps = 0, 110
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()# frame rate

# loop principal
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake_direction = (0, -TILE_SIZE)
            if event.key == pg.K_DOWN:
                snake_direction = (0, TILE_SIZE)
            if event.key == pg.K_LEFT:
                snake_direction = (-TILE_SIZE, 0)
            if event.key == pg.K_RIGHT:
                snake_direction = (TILE_SIZE, 0)
    screen.fill('black')
    [pg.draw.rect(screen, 'green', segment) for segment in snake_body_segments]
    time_now = pg.time.get_ticks()
    if time_now - time > time_steps:
        time = time_now
        snake.move_ip(snake_direction)
        snake_body_segments.append(snake.copy())
        snake_body_segments = snake_body_segments[-length:]
    pg.display.flip()
    clock.tick(60)