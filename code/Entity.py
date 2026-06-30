#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE, ENTINTY_SCORE, ENTITY_SPEED


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = ENTITY_SPEED[self.name]
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.record = ENTINTY_SCORE[self.name]

    @abstractmethod
    def move(self, ):
        pass
