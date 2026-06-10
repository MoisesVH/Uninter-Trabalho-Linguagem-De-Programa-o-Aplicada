#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WINDOW_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'background_level1_':
                list_background = []
                for i in range(4):
                        list_background.append(Background(f'background_level1_{i + 1}', position=(0, 0)))
                        list_background.append(Background(f'background_level1_{i + 1}', position=(WINDOW_WIDTH, 0)))

                return list_background
        return None
