#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.Record import Record


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):

        while True:
            record = Record(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
                player_record = [0] # [player1]
                level = Level(self.window, 'level', menu_return, player_record)
                level_return = level.run(player_record)
                player_record[0] = level_return
                record.save(menu_return, player_record)

            elif menu_return == MENU_OPTION[1]:
                record.show()

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()  # fechando a janela
                quit()  # encerrando o pygame
