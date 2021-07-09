import pygame
from Board import Board
from Constantes import Sheep, Wolf, Blue, Square_Size

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
            self.valid_moves = self.board.Get_Valid_Moves(piece)
            return True

        return False

    def _Move(self, row, col):
        piece = self.board.Get_Piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.Move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.Remove(skipped)
            self.Change_Turn()
        else:
            return False
        return True
    
    def Draw_Valid_Moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, Blue, (col * Square_Size + Square_Size // 2, row * Square_Size + Square_Size // 2), 15)

    def Change_Turn(self):
        self.valid_moves = {}
        if self.turn == Wolf:
            self.turn = Sheep
        else:
            self.turn = Wolf