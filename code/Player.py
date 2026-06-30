#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WINDOW_WIDTH, PLAYER_MOVE_UP, PLAYER_MOVE_DOWN, PLAYER_MOVE_LEFT, \
    PLAYER_MOVE_RIGHT, WINDOW_HEIGHT
from code.Entity import Entity

class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.speed += 1
        if self.rect.bottom < WINDOW_HEIGHT:
            self.rect.centery += self.speed

    def jump(self):
        self.speed = -ENTITY_SPEED[self.name]
