import pygame
import sys

pygame.init()

display = pygame.display.set_mode((1280, 720)) #tamanho do display

player1 = pygame.Rect(0, 0, 50, 50) #Boneco do player
player1_speed = 0 #Velocidade do player
player2 = pygame.Rect(200, 100, 50, 50)
player2_speed = 0
ball = pygame.Rect(600, 123, 323, 223)


loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        #Controle do player1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1_speed = -2

            elif event.key == pygame.K_d:
                player1_speed = 2

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                player1_speed = 0
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player2_speed = -2

            elif event.key == pygame.K_RIGHT:
                player2_speed = 2

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player2_speed = 0

        #Controle do player1

        if player1.y <= 0:
            player1.y = 0
        elif player1.y >= 670:
            player1.y = 670
        
        #Controle do player2
        if player2.x <= 0:
            player2.y = 0
        elif player2.y >= 670:
            player2.y = 670

    player1.y += player1_speed  #Aqui toda vez que eu clicar com o A ou D irá acrescentar a velocidade do player

    display.fill((0, 0, 0)) 

    pygame.draw.rect(display, "white", player1)
    pygame.draw.rect(display, "blue", player2)
    pygame.draw.circle(display, "red", ball.center, 8)

    pygame.display.flip()


    # Teste
pygame.quit()
sys.exit()


            