import pygame
from Board import Board
from Constantes import Sheep, Wolf

class Game_functions:
    def __init__(self, win):
        self._Init()
        self.win = win

    def Update(self):
        self.board.Draw(self.win)
        pygame.display.update()

    def _Init(self):
        self.selected = None
        self.board = Board(Sheep, Wolf)
        self.turn = Sheep
        self.valid_moves = {}

    def Reset(self):
        self._Init()

    def Select(self, row, col):
        if self.selected:
            result = self._Move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.valid_move(self.selected, row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece

    def _Move(self, row, col):
        piece = self.board.Get_Piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.Valid_moves:
            self.board.Move(self.selected, row, col)
    
    def 