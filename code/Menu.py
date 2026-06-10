#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_FONT1, COLOR_FONT2, MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/background_menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        option_select = 0
        pygame.mixer.music.load('./assets/menu.wav')
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Sky Shot', (0, 0, 0), ((WINDOW_WIDTH / 2) - 2, 77))
            self.menu_text(50, 'Sky Shot', COLOR_FONT1, ((WINDOW_WIDTH / 2), 75))

            for i in range(len(MENU_OPTION)):
                if i == option_select:
                    self.menu_text(27, MENU_OPTION[i], COLOR_FONT1, ((WINDOW_WIDTH / 2), 175 + 23 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], COLOR_FONT2, ((WINDOW_WIDTH / 2), 175 + 23 * i))

            # Checando todos os eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechando a janela
                    quit()  # encerrando o pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # tecla para baixa
                        option_select += 1
                        if option_select > len(MENU_OPTION)-1:
                            option_select = 0

                    if event.key == pygame.K_UP: # tecla para cima
                        option_select -= 1
                        if option_select < 0:
                            option_select = len(MENU_OPTION)-1

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[option_select]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
