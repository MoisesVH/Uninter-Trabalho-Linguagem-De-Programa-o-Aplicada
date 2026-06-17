# C
import pygame

COLOR_FONT1 = (175, 50, 175)
COLOR_FONT2 = (255, 255, 255)

# E
ENTITY_SPEED = {
    'background_level1_1': 0,
    'background_level1_2': 2,
    'background_level1_3': 1,
    'background_level1_4': 3,

    'player1': 3,
    'player2': 3,

    'enemy1': 3,
    'enemy2': 2,
    'enemy3': 1,
}

EVENT_ENEMY1 = pygame.USEREVENT + 0
EVENT_ENEMY2 = pygame.USEREVENT + 1
EVENT_ENEMY3 = pygame.USEREVENT + 3

# M
MENU_OPTION = [
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'NEW GAME 2P - COMPETITIVE',
    'SCORE',
    'EXIT'
]

# P
PLAYER_MOVE_UP = {
    'player1': pygame.K_w,
    'player2': pygame.K_UP,
}
PLAYER_MOVE_DOWN = {
    'player1': pygame.K_s,
    'player2': pygame.K_DOWN,
}
PLAYER_MOVE_LEFT = {
    'player1': pygame.K_a,
    'player2': pygame.K_LEFT,
}
PLAYER_MOVE_RIGHT = {
    'player1': pygame.K_d,
    'player2': pygame.K_RIGHT,
}

# s
SPAWN_TIME1 = 5000
SPAWN_TIME2 = 10000
SPAWN_TIME3 = 40000

# w
WINDOW_HEIGHT = 324
WINDOW_WIDTH = 576
