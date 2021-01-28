#Importar variáveis e bibliotecas
import pygame
import os
from pygame.locals import*
from Constantes import Cumprimento, Largura, White
import pygame.freetype

def Rules():

    #Dentro desta função, vão estar as regras do jogo e o botão para regressar ao menu principal
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((Cumprimento, Largura))

    pygame.display.set_caption("Wolf & Sheep")
    icon = pygame.image.load('Wolf_&_Sheep_V2.png')
    pygame.display.set_icon(icon)

    #Titulo
    rules = pygame.font.SysFont("NotoSans-Regular.ttff", 90)
    rules_surface = rules.render("Regras", True, White)

    #Regras do jogo
    r1 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r1_surface = r1.render("1 - O jogo 'Wolf & Sheep' é jogo para dois jogadores. O computador não irá jogar com ninguém.", True, White)

    r2 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r2_surface = r2.render("2 - O jogador que escolher a ovelha joga sempre primeiro", True, White)

    r3 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r3_surface = r3.render("3 - Há quatro lobos e uma ovelha. Só se pode mover um lobo por turno.", True, White)

    r4 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r4_surface = r4.render("4 - As peças movem-se na diagonal, sendo que por turno, cada peça só se move uma casa.", True, White)

    r5 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r5_surface = r5.render("5 - A ovelha pode andar para a frente ou para trás, enquanto os lobos só andam para frente.", True, White) 

    r6 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r6_surface = r6.render("6 - Há duas formas de ganhar este jogo. Ou a ovelha chega ao topo do tabuleiro (vitória para a ovelha)", True, White)

    r6_cont = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r6_cont_surface = r6_cont.render("Ou os lobos encurralam a ovelha (ganham os lobos porque a ovelha não tem mais movimentos válidos).", True, White)

    boa_sorte = pygame.font.SysFont("NotoSans-Regular.ttff", 90)
    boa_sorte_surface = boa_sorte.render("Boa Sorte aos jogadores!!!", True, White)

    clock = pygame.time.Clock()
    running = True

    while (running):

        screen.fill((214, 162, 94))

        rect1_exterior = pygame.draw.rect(screen, (223, 0, 100), (1050, 550, 200, 60), 0)
        rect1_interior = pygame.draw.rect(screen, (255, 138, 190), (1062, 555, 175, 50), 0)

        leave = pygame.font.SysFont("NotoSans-Regular.ttff", 70)
        leave_surface = leave.render("Exit", True, White)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False

        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()

        if (mx > 1050) and (mx < 1250) and (my > 550) and (my < 610):
            rect1_exterior = pygame.draw.rect(screen, (0, 0, 100), (1050, 550, 200, 60), 0)
            rect1_interior = pygame.draw.rect(screen, (0, 138, 190), (1062, 555, 175, 50), 0)
            if (mb[0]):
                return
        
        screen.blit(rules_surface, (500, 20))
        screen.blit(r1_surface, (10, 110))
        screen.blit(r2_surface, (10, 160))
        screen.blit(r3_surface, (10, 210))
        screen.blit(r4_surface, (10, 260))
        screen.blit(r5_surface, (10, 310))
        screen.blit(r6_surface, (10, 360))
        screen.blit(r6_cont_surface, (40, 380))
        screen.blit(boa_sorte_surface, (250, 490))
        screen.blit(leave_surface, (1092, 560))
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()