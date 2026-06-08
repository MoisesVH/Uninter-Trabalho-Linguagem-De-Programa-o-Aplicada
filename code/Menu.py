#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_FONT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/backgounds/backgound_menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./assets/menu.wav')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Sky Shot', COLOR_FONT, ((WINDOW_WIDTH / 2), 75))
            self.menu_text(24, 'NOVO JOGO 1P', COLOR_FONT, ((WINDOW_WIDTH / 2), 175))
            self.menu_text(24, 'NOVO JOGO 2P - COOPERATIVO', COLOR_FONT, ((WINDOW_WIDTH / 2), 195))
            self.menu_text(24, 'NOVO JOGO 2P - COMPETITIVO', COLOR_FONT, ((WINDOW_WIDTH / 2), 215))
            self.menu_text(24, 'PONTUAÇÃO', COLOR_FONT, ((WINDOW_WIDTH / 2), 235))
            self.menu_text(24, 'SAIR DO JOGO', COLOR_FONT, ((WINDOW_WIDTH / 2), 255))

            pygame.display.flip()

            # Checando todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechando a janela
                    print('Fim do programa')
                    quit()  # encerrando o pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)