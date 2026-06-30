#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Background import Background
from code.Player import Player
from code.Obstacle import Obstacle



class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        randomize = random.randint(160, WINDOW_HEIGHT - 80)

        match entity_name:
            case 'background':
                return Background(f'background', position=(0, 0))

            case 'player':
                return Player('player', (120, WINDOW_HEIGHT / 2))

            case 'pipe_':
                obstacle_list = [
                    Obstacle('pipe_top', (WINDOW_WIDTH, randomize)),
                    Obstacle('pipe_bottom', (WINDOW_WIDTH, randomize - 368))
                ]
                return obstacle_list


        return None
