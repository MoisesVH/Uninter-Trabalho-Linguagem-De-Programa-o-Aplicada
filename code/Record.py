from datetime import datetime

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.DBProxy import DBProxy
from code.Const import WINDOW_WIDTH, COLOR_FONT2
from code.Menu import Menu


class Record:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/background.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, menu_return: str, player_record: list[int]):
        pygame.mixer.music.load('./assets/menu.wav')
        pygame.mixer.music.play(-1)
        db_proxy = DBProxy('DBRecords')
        name = ''
        record = player_record[0]

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.record_text(48, 'GAME OVER', COLOR_FONT2, (WINDOW_WIDTH / 2, 50))
            self.record_text(20, 'Enter you name (3 characters):', COLOR_FONT2, (WINDOW_WIDTH / 2, 80))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if event.type == pygame.QUIT:
                        pygame.quit()  # fechando a janela
                        quit()  # encerrando o pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 3:
                        db_proxy.save({'name': name, 'record': record, 'date': get_formatted_date()})
                        self.show()
                        return

                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 3:
                            name += event.unicode

            self.record_text(20, name, COLOR_FONT2, (WINDOW_WIDTH / 2, 120))

            pygame.display.flip()

    def show(self):
        menu = Menu(self.window)
        pygame.mixer.music.load('./assets/menu.wav')
        pygame.mixer.music.play(-1)

        self.window.blit(source=self.surf, dest=self.rect)

        self.record_text(48, 'TOP 10 RECORDS', COLOR_FONT2, (WINDOW_WIDTH / 2, 50))

        db_proxy = DBProxy('DBRecords')
        list_record = db_proxy.retrieve_top10()
        db_proxy.close()
        i = 1
        for record in list_record:
            i += 1
            id, name, record, date = record
            self.record_text(20, f'{name}        {record / 1000:.2f}        {date}', COLOR_FONT2,
                             (WINDOW_WIDTH / 2, 60 + 20 * i))

        self.record_text(20, 'Press the ESC key to return to the menu', COLOR_FONT2, (WINDOW_WIDTH / 2, 310))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # fechando a janela
                    quit()  # encerrando o pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

            pygame.display.flip()

    def record_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_date = current_datetime.strftime('%d/ %m/ %y')
    return f'{current_time} - {current_date}'
