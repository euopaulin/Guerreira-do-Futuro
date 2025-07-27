import pygame
import sys

display=pygame.display.set_mode((1280, 720))

player1 = pygame.Rect(0, 0, 50, 50)
player2 = pygame.Rect(200, 100, 50, 50)
ball= pygame.Rect(600,123, 323, 223)


loop = True
while loop:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player1.x += 50
            elif event.key == pygame.K_a:
                player2.y -= 50
            elif event.key == pygame.K_d:
                ball.x += 50


    pygame.display.flip()

    pygame.draw.rect(display, "white", player1)

    pygame.draw.rect(display, "blue", player2)

    pygame.draw.circle(display, "red", ball.center, 8)

    pygame.display.flip()  # Clear the screen with black

            