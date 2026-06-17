#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'background_level1_':
                list_background = []
                for i in range(4):
                    list_background.append(Background(f'background_level1_{i + 1}', position=(0, 0)))
                    list_background.append(Background(f'background_level1_{i + 1}', position=(WINDOW_WIDTH, 0)))

                return list_background

            case 'player1':
                return Player('player1', (10, WINDOW_HEIGHT / 2 - 30))

            case 'player2':
                return Player('player2', (10, WINDOW_HEIGHT / 2 + 30))

            case 'enemy1':
                return Enemy('enemy1', (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT - 40)))

            case 'enemy2':
                return Enemy('enemy2', (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT - 40)))

            case 'enemy3':
                return Enemy('enemy3', (WINDOW_WIDTH, random.randint(0, WINDOW_HEIGHT - 40)))

        return None
