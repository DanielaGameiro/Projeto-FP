import pygame
from pygame.locals import*
from Constantes import Cumprimento, Largura, White
from Board import Board
from Wolf_Piece import Wolf
from Sheep_Piece import Sheep
import pygame.freetype

def Game():

    #É aqui que o jogo acontce

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((Cumprimento, Largura))

    pygame.display.set_caption("Wolf & Sheep")
    icon = pygame.image.load('Wolf_&_Sheep_V2.png')
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()

    Board_Game = Board()

    Wolf_0 = Wolf(351, 100, screen)
    Wolf_1 = Wolf(475, 100, screen)
    Wolf_2 = Wolf(599, 100, screen)
    Wolf_3 = Wolf(723, 100, screen)

    Sheep_1 = Sheep(535, 535, screen)

    running = True

    while (running):

        screen.fill((214, 162, 94))

        return_rect = pygame.draw.rect(screen, (223, 0, 100), (1050, 550, 200, 60), 0)
        return_rect_interior = pygame.draw.rect(screen, (255, 138, 190), (1062, 555, 175, 50), 0)

        white = pygame.draw.rect(screen, White, (350, 100, 496, 496), 0)

        leave = pygame.font.SysFont("NotoSans-Regular.ttff", 70)
        leave_surface = leave.render("Exit", True, White)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False

        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()

        if (mx > 1050) and (mx < 1250) and (my > 550) and (my < 610):
            return_rect = pygame.draw.rect(screen, (0, 0, 100), (1050, 550, 200, 60), 0)
            return_rect_interior = pygame.draw.rect(screen, (0, 138, 190), (1062, 555, 175, 50), 0)
            if (mb[0]):
                return

        k = pygame.key.get_pressed()

        if (k[pygame.K_LEFT]):
            Sheep_1.going_up_left()
        elif(k[pygame.K_RIGHT]):
            Sheep_1.going_up_right()
        elif(k[pygame.K_DOWN]):
            Sheep_1.going_down()

        screen.blit(leave_surface, (1100, 560))
        clock.tick(60)
        Board_Game.Draw(screen)
        Wolf_0.draw_wolf()
        Wolf_1.draw_wolf()
        Wolf_2.draw_wolf()
        Wolf_3.draw_wolf()
        Sheep_1.draw_sheep()
        pygame.display.flip()