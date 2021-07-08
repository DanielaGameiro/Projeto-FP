import pygame
from Board import Board
from Constantes import Sheep, Wolf

class Game_functions:
    def __init__(self, win):
        self.selected = None
        self.board = Board(Sheep, Wolf)
        self.turn = Sheep
        self.valid_moves = {}
        self.win = win

    def Update(self):
        self.board.Draw(self.win)
        pygame.display.update()