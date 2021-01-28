import pygame
from Constantes import Black, Rows, Square_Size

class Board:
    def __init__(self):
        self.board = []

    def Draw (self, screen):
        for row in range(Rows):
            for col in range(row % 2, Rows, 2):
                pygame.draw.rect(screen, Black, (row*Square_Size + 350, col*Square_Size + 100, Square_Size, Square_Size))