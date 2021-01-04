import pygame
from pygame.locals import*
import pygame.freetype

def Game():

    pygame.init()
    pygame.font.init()

    cumprimento = 1300
    largura = 650
    screen = pygame.display.set_mode((cumprimento, largura))

    pygame.display.set_caption("Wolf & Sheep")
    icon = pygame.image.load('Wolf_&_Sheep_v2.png')
    pygame.display.set_icon(icon)

    clock = pygame.time.Clock()
    running = True

    while (running):

        screen.fill((214, 162, 94))

        tab = pygame.draw.rect(screen, (255, 255, 255), (200, 50, 800, 500), 0)

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


        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()

Game()