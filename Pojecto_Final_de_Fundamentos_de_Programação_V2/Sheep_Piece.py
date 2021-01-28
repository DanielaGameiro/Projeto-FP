import pygame

class Sheep:

    pygame.init()

    def __init__ (self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.Sheep = pygame.image.load('Mini_Sheep.png')

    def draw_sheep (self):
        self.screen.blit(self.Sheep, (self.x, self.y))