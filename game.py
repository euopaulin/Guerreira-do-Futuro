import pygame
import sys

def inicializa_game():
    pygame.init()
    name = "Guerreira do futuro"
    display = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption(name) #tamanho do display
    background = pygame.image.load("assets/image/back (3).png").convert()
    return display, background

display, background_image = inicializa_game()

#Carrega a imagem de fundo
display.blit(background_image, (0, 0))
player1 = pygame.Rect(0, 0, 50, 50) #Boneco do player_1
player1_speed_y = 0 #Velocidade do player_1
player1_speed_x = 0
player2 = pygame.Rect(200, 100, 50, 50) #Boneco do player_2
player2_speed_y = 0
player2_speed_x = 0
ball = pygame.Rect(600, 123, 323, 223)
ball_speed_x = 0
ball_speed_y = 0
ball_dir_x = 1
ball_dir_y = 1

clock = pygame.time.Clock()
FPS = 200

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            
        #Controle do player1 e player2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player1_speed_x = -2
            elif event.key == pygame.K_LEFT:
                player2_speed_x = -2

            if event.key == pygame.K_d:
                player1_speed_x = 2
            elif event.key == pygame.K_RIGHT:
                player2_speed_x = 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed_y = -2
            elif event.key == pygame.K_s:
                player1_speed_y = 2

            if event.key == pygame.K_UP:
                player2_speed_y = -2
            elif event.key == pygame.K_DOWN:
                player2_speed_y = 2

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_a, pygame.K_d):
                player1_speed_x = 0

            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player2_speed_x = 0

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                player1_speed_y = 0

            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player2_speed_y = 0
                
    player1.y += player1_speed_y 
    player1.x += player1_speed_x
    player2.y += player2_speed_y 
    player2.x += player2_speed_x
    
        #Controle do player1 e player2
    if player1.y <= 0:
            player1.y = 0
    elif player1.y >= 670:
            player1.y = 670
    if player1.x <= 0:
            player1.x = 0
    elif player1.x >= 1230:
            player1.x = 1230
            
    if player2.y <= 0:
            player2.y = 0
    elif player2.y >= 670:
            player2.y = 670
    if player2.x <= 0:    
            player2.x = 0
    elif player2.x >= 1230:
            player2.x = 1230

    #Controle da bola
    if ball.y <= 0:
        ball.y = 600   
    elif ball.x <= 1280:
        ball.x = 600

    if ball.y <= 0:
        ball_dir_y *= -1
    elif ball.y >= 720 - 15:
        ball_dir_y *= -1

    ball.x = ball_dir_x
    ball.y = ball_dir_y
        
    # Aqui toda vez que eu clicar com o A ou D irá acrescentar a velocidade do player

    display.fill((0, 0, 0))
    display.blit(background_image, (0, 0))

    pygame.draw.rect(display, "white", player1)
    pygame.draw.rect(display, "blue", player2)
    pygame.draw.circle(display, "red", ball.center, 8)

    pygame.display.flip()

    clock.tick(FPS)

    # Teste
pygame.quit()
sys.exit()



            