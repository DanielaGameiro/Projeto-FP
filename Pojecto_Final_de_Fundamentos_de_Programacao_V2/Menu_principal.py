#Importar bibliotecas e modulos necessários
import pygame
import os
from pygame.locals import*
from Constantes import Cumprimento, Largura, White
from Game import Game
from Rules import Rules
import pygame.freetype

#Iniciar o jogo

def Menu_principal():

    #Iniciar o pygame e as fonts para o texto
    pygame.init()
    pygame.font.init()

    #Definir o ecran
    screen = pygame.display.set_mode((Cumprimento, Largura))

    #Dar um nome à janela e mudar o icon
    pygame.display.set_caption("Wolf & Sheep")
    icon = pygame.image.load('Wolf_&_Sheep_V2.png')
    pygame.display.set_icon(icon)

    #Carregar as imagens
    Sheep = pygame.image.load('Sheep.png').convert_alpha()
    Sheep_x = 1000
    Sheep_y = 0

    Wolf = pygame.image.load('Wolf.png').convert_alpha()
    Wolf_x = 20
    Wolf_y = 0

    #Texto que vai aparecer nos botões
    title = pygame.font.SysFont("NotoSans-Regular.ttff", 100)
    title_surface = title.render("Wolf & Sheep", True, White)

    start = pygame.font.SysFont("NotoSans-Regular.ttff", 70)
    start_surface = start.render("Start", True, White)

    rules = pygame.font.SysFont("NotoSans-Regular.ttff", 70)
    rules_surface = rules.render("Rules", True, White)

    leave = pygame.font.SysFont("NotoSans-Regular.ttff", 70)
    leave_surface = rules.render("Exit", True, White)

    b1 = pygame.mixer.Sound('Lets play.mp3')
    b2 = pygame.mixer.Sound('rules.mp3')
    b3 = pygame.mixer.Sound('bye.mp3')
    Wolf_sound = pygame.mixer.Sound('wolf.mp3')

    clock = pygame.time.Clock()

    running = True

    #Iniciar o loop do jogo
    while (running):

        #Dar cor ao ecran
        screen.fill((214, 162, 94))

        #Botões
        rect1_exterior = pygame.draw.rect(screen, (223, 0, 100), (550, 250, 200, 60), 0)
        rect1_interior = pygame.draw.rect(screen, (255, 138, 190), (562, 255, 175, 50), 0)
        rect2_exterior = pygame.draw.rect(screen, (223, 0, 100), (550, 350, 200, 60), 0)
        rect2_interior = pygame.draw.rect(screen, (255, 138, 190), (562, 355, 175, 50), 0)
        rect3_exterior = pygame.draw.rect(screen, (223, 0, 100), (550, 450, 200, 60), 0)
        rect3_interior = pygame.draw.rect(screen, (255, 138, 190), (562, 455, 175, 50), 0)

        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running = False

        #Variáveis para detectar a posição do rato e os botões pressionados
        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()

        if (mx > 550) and (mx < 750) and (my > 250) and (my < 310):
            rect1_exterior = pygame.draw.rect(screen, (0, 0, 100), (550, 250, 200, 60), 0)
            rect1_interior = pygame.draw.rect(screen, (0, 138, 190), (562, 255, 175, 50), 0)
            b1.play()
            if (mb[0]):
                Game()
        
        elif (mx > 550) and (mx < 750) and (my > 350) and (my < 410):
            rect2_exterior = pygame.draw.rect(screen, (0, 0, 100), (550, 350, 200, 60), 0)
            rect2_interior = pygame.draw.rect(screen, (0, 138, 190), (562, 355, 175, 50), 0)
            b2.play()
            if (mb[0]):
                Rules()

        elif (mx > 550) and (mx < 750) and (my > 450) and (my < 510):
            rect3_exterior = pygame.draw.rect(screen, (0, 0, 100), (550, 450, 200, 60), 0)
            rect3_interior = pygame.draw.rect(screen, (0, 138, 190), (562, 455, 175, 50), 0)
            b3.play()
            if (mb[0]):
                running = False
       
        #Colocar tudo no ecran
        screen.blit(Sheep, (Sheep_x, Sheep_y))
        screen.blit(Wolf, (Wolf_x, Wolf_y))
        screen.blit(title_surface, (430, 100))
        screen.blit(start_surface, (590, 260))
        screen.blit(rules_surface, (580, 360))
        screen.blit(leave_surface, (595, 460))

        #Updates do ecran
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()

Menu_principal()