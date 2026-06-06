import pygame

print('Iniciando...')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))

while True:
    # Checando todos os eventos
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            pygame.quit() # fechando a janela
            print('Fim do programa')
            quit() # encerrando o pygame