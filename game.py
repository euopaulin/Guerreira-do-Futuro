import pygame
import sys

pygame.init()

screen= pygame.display.set_mode((800,600))

pygame.display.set_caption("A guerreira do Futuro")

background_color=(131,111,255)

player_color = (255, 0, 0)

player_x = 100
player_y = 100
player_width = 50
player_height = 50

player_speed = 5

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill(background_color)           

        pygame.player_x = player_speed

        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
            
        pygame.display.update()


            

pygame.quit()
sys.exit()
        