import pygame
from pygame.locals import*
from Constantes import Cumprimento, Largura, White, Square_Size
from Board import Board
from Game_function import Game_functions
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

    Sheep = pygame.image.load('Mini_Sheep.png')
    Wolf = pygame.image.load('Mini_Wolf.png')
    
    b3 = pygame.mixer.Sound('bye.mp3')

    while True:

        screen.fill((214, 162, 94))

        return_rect = pygame.draw.rect(screen, (223, 0, 100), (1050, 550, 200, 60), 0)
        return_rect_interior = pygame.draw.rect(screen, (255, 138, 190), (1062, 555, 175, 50), 0)

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
                b3.play()
                if (mb[0]):
                    return

        for r in range(0, 480, 60):
            for c in range(0, 520,70):
                rect = pygame.draw.rect(screen, (255, 255, 255), (r, c, 60, 60), 0)
                rect1 = pygame.draw.rect(screen, (0, 0, 0), (r, c, 60, 60), 9)

        for i in range (60, 500, 120):
            screen.blit(Wolf, (i, 0))
        

        screen.blit(leave_surface, (1100, 560))
        screen.blit(Sheep, (180, 480))
        clock.tick(60)
        pygame.display.flip()