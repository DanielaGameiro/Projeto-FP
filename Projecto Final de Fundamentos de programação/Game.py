import pygame
from pygame.locals import*
from Constantes import Cumprimento, Largura
from Board import Board
import pygame.freetype

def Game():

    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode((Cumprimento, Largura))

    pygame.display.set_caption("Wolf & Sheep")
    icon = pygame.image.load('Wolf_&_Sheep_v2.png')
    pygame.display.set_icon(icon)

    leave = pygame.font.SysFont("NotoSans-Regular.ttff", 70)
    leave_surface = leave.render("Exit", True, (255, 255, 255))

    clock = pygame.time.Clock()

    Board_Game = Board()

    running = True

    while (running):

        screen.fill((214, 162, 94))

        rect1_exterior = pygame.draw.rect(screen, (223, 0, 100), (1050, 550, 200, 60), 0)
        rect1_interior = pygame.draw.rect(screen, (255, 138, 190), (1062, 555, 175, 50), 0)

        white = pygame.draw.rect(screen, (255, 255, 255), (350, 100, 496, 496), 0)

        leave = pygame.font.SysFont("NotoSans-Regular.ttff", 70)
        leave_surface = leave.render("Exit", True, (255, 255, 255))

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                running = False
        
        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()

        if (mx > 1050) and (mx < 1250) and (my > 550) and (my < 610):
            rect1_exterior = pygame.draw.rect(screen, (0, 0, 100), (1050, 550, 200, 60), 0)
            rect1_interior = pygame.draw.rect(screen, (0, 138, 190), (1062, 555, 175, 50), 0)
            if(mb[0]):
                return

        screen.blit(leave_surface,(1100, 560))
    
        clock.tick(60)
        Board_Game.Draw(screen)
        pygame.display.flip()