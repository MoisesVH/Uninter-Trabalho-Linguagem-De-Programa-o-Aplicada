#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_FONT2, WINDOW_HEIGHT, MENU_OPTION, EVENT_ENEMY1, EVENT_ENEMY2, SPAWN_TIME1, \
    SPAWN_TIME2
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('background_level1_'))
        self.entity_list.append(EntityFactory.get_entity('player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('player2'))

        pygame.time.set_timer(EVENT_ENEMY1, SPAWN_TIME1)
        pygame.time.set_timer(EVENT_ENEMY2, SPAWN_TIME2)

        self.timeout = 20000  # 20 segundds

    def run(self, ):
        pygame.mixer_music.load(f'./assets/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shot = ent.shot()
                    if shot is not None:
                        self.entity_list.append(shot)

                if ent.name == 'player1':
                    self.level_text(16, f'Player 1 - Health: {ent.health} | SCORE: {ent.score}', COLOR_FONT2, (10, 30))
                if ent.name == 'player2':
                    self.level_text(16, f'Player 2 - Health: {ent.health} | SCORE: {ent.score}', COLOR_FONT2, (10, 60))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY1:
                    self.entity_list.append(EntityFactory.get_entity('enemy1'))

                if event.type == EVENT_ENEMY2:
                    self.entity_list.append(EntityFactory.get_entity('enemy2'))

            self.level_text(16, f'{self.name} - Timeout: {self.timeout / 1000:.2f}s', COLOR_FONT2, (10, 5))
            self.level_text(16, f'fps: {clock.get_fps() :.0f}', COLOR_FONT2, (10, WINDOW_HEIGHT - 35))
            self.level_text(16, f'entidades: {len(self.entity_list)}', COLOR_FONT2, (10, WINDOW_HEIGHT - 20))

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
