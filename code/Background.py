#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WINDOW_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        if self.name == 'background_level1_3':
            self.rect.centerx += ENTITY_SPEED[self.name]

            if self.rect.left >= WINDOW_WIDTH:
                self.rect.right = 0
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

            if self.rect.right <= 0:
                self.rect.left = WINDOW_WIDTH
