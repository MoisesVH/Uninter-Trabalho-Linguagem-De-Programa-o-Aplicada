#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from locale import setlocale

import pygame
from pygame import Surface, Rect
from pygame.font import Font, init

from code.Const import COLOR_FONT2, WINDOW_HEIGHT, EVENT_OBSTACLE, SPAWN_TIME, \
    EVENT_TIMEOUT, TIMEOUT_STEP, TIMER_LEVEL, WINDOW_WIDTH
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_record: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.timer = TIMER_LEVEL
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity(f'background'))
        player = EntityFactory.get_entity('player')
        player_record = player_record[0]
        self.entity_list.append(player)

        pygame.time.set_timer(EVENT_OBSTACLE, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        self.start()

        pygame.mixer_music.load(f'./assets/{self.name}.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for ent in self.entity_list:
                            if ent.name == 'player':
                                ent.jump()

                if event.type == EVENT_OBSTACLE:
                    self.entity_list.extend(EntityFactory.get_entity('pipe_'))

                if event.type == EVENT_TIMEOUT:
                    self.timer += TIMEOUT_STEP

            found_player = False

            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            if not found_player:
                return self.timer

            self.level_text(16, f'Timer: {self.timer / 1000:.2f}s', COLOR_FONT2, (40, 10))

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def start(self):


        start = 0
        while start < 1:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

            self.level_text(20, 'Press the SPACE key to start the game', COLOR_FONT2,
                            (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        for ent in self.entity_list:
                            if ent.name == 'player':
                                ent.jump()

                        start += 1

            pygame.display.flip()
