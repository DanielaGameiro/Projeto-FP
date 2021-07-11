import pygame
from Constantes import Wolf, Sheep, Square_Size

class Pieces:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.Calc_pos()

    #Calculo das coordenads das peças
    def Calc_pos(self):
        self.x = Square_Size * self.col
        self.y = Square_Size * self.row

    #Mover as peças
    def Move(self, row, col):
        self.row = row
        self.col = col
        self.Calc_pos()

    #Desenha as peças
    def Draw_Wolf (self, win):
        Wolf = pygame.image.load('Mini_Wolf.png')
        win.blit(Wolf, (self.x, self.y))

    def Draw_Sheep(self, win):
        Sheep = pygame.image.load('Mini_Sheep.png')
        win.blit(Sheep, (self.x, self.y))