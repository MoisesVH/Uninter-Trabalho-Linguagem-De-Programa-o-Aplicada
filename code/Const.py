# C
import random

import pygame

COLOR_FONT1 = (255, 255, 255)
COLOR_FONT2 = (101, 67, 33)

# E
ENTINTY_SCORE = {
    'background': 0,

    'player': 0,

    'pipe_bottom': 5,
    'pipe_top': 5,
}

ENTITY_DAMAGE = {
    'background': 0,

    'player': 0,

    'pipe_bottom': 1,
    'pipe_top': 1,
}

ENTITY_HEALTH = {
    'background': 999,

    'player': 1,

    'pipe_bottom': 999,
    'pipe_top': 999,
}

ENTITY_SPEED = {
    'background': 0,

    'player': 8,

    'pipe_bottom': 5,
    'pipe_top': 5,
}

EVENT_OBSTACLE = pygame.USEREVENT + 0
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = [
    'NEW GAME',
    'SCORE',
    'EXIT'
]

# P
PLAYER_MOVE_UP = {
    'player': pygame.K_w,
}

PLAYER_MOVE_DOWN = {
    'player': pygame.K_s,
}

PLAYER_MOVE_LEFT = {
    'player': pygame.K_a,
}

PLAYER_MOVE_RIGHT = {
    'player': pygame.K_d,
}

# s
SPAWN_TIME = 2000  # 2 segundos

# T
TIMEOUT_STEP = 100  # 1 milisegundo
TIMER_LEVEL = 0  # 0 segundos

# w
WINDOW_HEIGHT = 384
WINDOW_WIDTH = 576
