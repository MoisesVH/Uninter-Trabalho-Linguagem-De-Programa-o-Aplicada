#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WINDOW_HEIGHT, ENTITY_SPEED, WINDOW_WIDTH, PLAYER_MOVE_UP, PLAYER_MOVE_DOWN, PLAYER_MOVE_LEFT, \
    PLAYER_MOVE_RIGHT
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[PLAYER_MOVE_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_MOVE_DOWN[self.name]] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_MOVE_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_keys[PLAYER_MOVE_RIGHT[self.name]] and self.rect.right < WINDOW_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        pass
