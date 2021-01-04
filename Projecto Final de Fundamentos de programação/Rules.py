import pygame
import os
from pygame.locals import*
import pygame.freetype

def Menu():

    pygame.init()
    pygame.font.init()

    cumprimento = 1300
    largura = 650
    screen = pygame.display.set_mode((cumprimento, largura))

    pygame.display.set_caption("Wolf & Sheep")
    icon = pygame.image.load('Wolf_&_Sheep_v2.png')
    pygame.display.set_icon(icon)

    rules = pygame.font.SysFont("NotoSans-Regular.ttff", 90)
    rules_surface = rules.render("Regras", True, (255, 255, 255))

    r1 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r1_surface = r1.render("1 - O jogo 'Wolf & Sheep' é um jogo para dois jogadores. O computador não irá jogar com ninguém.", True, (255, 255, 255))

    r2 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r2_surface = r2.render("2 - A ovelha (o jogador que esclheu a ovelha) joga sempre primeiro.", True, (255, 255, 255))

    r3 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r3_surface = r3.render("3 - O jogador que escolheu os lobos, só pode mover um lobo por turno.", True, (255, 255, 255))

    r4 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r4_surface = r4.render("4 - Os movimentos das peças são feitos na diagonal, sendo que cada peça só pode mover-se uma casa por turno.", True, (255, 255, 255))

    r5 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r5_surface = r5.render("5 - A ovelha pode andar para a frente ou para trás enquanto, os lobos só podem andar para a frente.", True, (255, 255, 255))

    r6 = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r6_surface = r6.render("6 - O jogo tem duas formas de acabar. Ou a ovelha chega ao topo do tabuleiro (ganha a ovelha).", True, (255, 255, 255))

    r6_cont = pygame.font.SysFont("NotoSans-Regular.ttff", 30)
    r6_cont_surface = r6_cont.render("Ou os lobos encurralam a ovelha (ganham os lobos porque a oveha não tem mais movimentos válidos).", True, (255, 255, 255))

    boa_sorte = pygame.font.SysFont("NotoSans-Regular.ttff", 90)
    boa_sorte_surface = boa_sorte.render("Boa Sorte aos jogadores!!!", True, (255, 255, 255))

    clock = pygame.time.Clock()
    running = True

    while (running):

        screen.fill((214, 162, 94))

        rect1_exterior = pygame.draw.rect(screen, (223, 0, 100), (1050, 550, 200, 60), 0)
        rect1_interior = pygame.draw.rect(screen, (255, 138, 190), (1062, 555, 175, 50), 0)

        leave = pygame.font.SysFont("NotoSans-Regular.ttff", 70)
        leave_surface = leave.render("Exit", True, (255, 255, 255))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False

        if (event.type == pygame.MOUSEBUTTONDOWN):
            mx, my = pygame.mouse.get_pos()
            if (mx > 1050) and (mx < 1250) and (my > 550) and (my < 610):
                return
        
        screen.blit(rules_surface,(500, 20))
        screen.blit(r1_surface,(10, 110))
        screen.blit(r2_surface,(10, 160))
        screen.blit(r3_surface,(10, 210))
        screen.blit(r4_surface,(10, 260))
        screen.blit(r5_surface,(10, 310))
        screen.blit(r6_surface,(10, 360))
        screen.blit(r6_cont_surface,(40, 380))
        screen.blit(boa_sorte_surface,(250, 490))
        screen.blit(leave_surface,(1092, 560))
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()

Menu()