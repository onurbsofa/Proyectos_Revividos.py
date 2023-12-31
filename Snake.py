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
time, time_steps = 0, 110 #time es el tiempo actual y time_steps es el tiempo que tarda en moverse la serpiente
food = snake.copy()
food.center = get_random_position() 
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
    pg.draw.rect(screen, 'red', food)
    if snake.colliderect(food):# si la serpiente choca con la comida
        length += 1
        food.center = get_random_position()
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW:# si la serpiente choca con los bordes
        snake.center = get_random_position()
        length = 1
        snake_body_segments = [snake.copy()]
        food.center = get_random_position()
    if any(segment.center == snake.center for segment in snake_body_segments[:-1]):# si la serpiente choca con su cuerpo
        snake.center = get_random_position()
        length = 1
        snake_body_segments = [snake.copy()]
        food.center = get_random_position()
    [pg.draw.rect(screen, 'green', segment) for segment in snake_body_segments]
    time_now = pg.time.get_ticks()
    if time_now - time > time_steps:# si el tiempo actual menos el tiempo anterior es mayor al tiempo que tarda en moverse la serpiente
        time = time_now # el tiempo actual se vuelve el tiempo anterior
        snake.move_ip(snake_direction)
        snake_body_segments.append(snake.copy())# se agrega una copia de la cabeza de la serpiente a la lista de segmentos
        snake_body_segments = snake_body_segments[-length:]# se actualiza la lista de segmentos
    pg.display.flip()
    clock.tick(60)