import pygame

class Wolf:

    pygame.init()

    def __init__ (self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.Wolf = pygame.image.load("Mini_Wolf.png")

    def draw_wolf (self):
        self.screen.blit(self.Wolf, (self.x, self.y))