# C
import pygame

COLOR_FONT1 = (175, 50, 175)
COLOR_FONT2 = (255, 255, 255)

# E
ENTITY_HEALTH = {
    'background_level1_1': 999,
    'background_level1_2': 999,
    'background_level1_3': 999,
    'background_level1_4': 999,

    'background_level2_1': 999,
    'background_level2_2': 999,
    'background_level2_3': 999,
    'background_level2_4': 999,

    'player1': 200,
    'player2': 200,

    'enemy1': 60,
    'enemy2': 80,
    'enemy3': 140,

    'player1_shot': 1,
    'player2_shot': 1,

    'enemy1_shot': 1,
    'enemy2_shot': 1,
    'enemy3_shot': 1,
}

ENTITY_SPEED = {
    'background_level1_1': 0,
    'background_level1_2': 2,
    'background_level1_3': 1,
    'background_level1_4': 3,

    'player1': 3,
    'player2': 3,

    'enemy1': 2,
    'enemy2': 1,
    'enemy3': 0.5,

    'player1_shot': 4,
    'player2_shot': 4,

    'enemy1_shot': 4,
    'enemy2_shot': 2,
    'enemy3_shot': 2,
}

ENTITY_SHOT_DELAY = {
    'player1': 20,
    'player2': 20,
    'enemy1': 100,
    'enemy2': 150,
    'enemy3': 200,
}

EVENT_ENEMY1 = pygame.USEREVENT + 0
EVENT_ENEMY2 = pygame.USEREVENT + 1

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

PLAYER_SHOT = {
    'player1': pygame.K_t,
    'player2': pygame.K_KP_ENTER,
}

# s
SPAWN_TIME1 = 5000
SPAWN_TIME2 = 7000

# w
WINDOW_HEIGHT = 324
WINDOW_WIDTH = 576
