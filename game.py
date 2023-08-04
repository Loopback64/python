import pygame
import sys

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego de Naves")

white = (255, 255, 255)

player_width = 50
player_height = 50
player_x = (width - player_width) // 2
player_y = height - player_height - 10
player_speed = 5

def game_loop():
    global player_x  # Declarar player_x como global para que sea accesible y modificable

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed

        player_x = max(0, min(player_x, width - player_width))

        screen.fill(white)
        pygame.draw.rect(screen, (0, 0, 255), (player_x, player_y, player_width, player_height))
        pygame.display.update()

    pygame.quit()
    sys.exit()

game_loop()

