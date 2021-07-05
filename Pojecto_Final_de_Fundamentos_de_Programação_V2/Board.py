import pygame
from Constantes import Black, Rows, Square_Size, Cols
from Piece import Pieces

class Board:
    def __init__(self, sleep, wolf):
        self.board = []
        self.selected_piece = None
        self.wolves_left = wolf = 4 #Só há 4 lobos
        self.sheep_left = sheep = 1 #Só há 1 ovelha
        self.Create_Board()

    #Desenhar o tabuleiro
    def Draw_Squares(self, screen):
        for row in range(Rows):
            for col in range(row % 2, Cols, 2):
                pygame.draw.rect(screen, Black, (row*Square_Size + 92, col*Square_Size + 40, Square_Size, Square_Size))

    def Create_Board(self):
        for row in range(Rows):
            self.board.append([])
            for col in range(Cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3 and self.wolves_left != 0:
                        self.board[row].append(Pieces(row, col, self.wolves_left))
                        self.wolves_left = self.wolves_left - 1
                    elif row > 4 and self.sheep_left != 0:
                        self.board[row].append(Pieces(row + 1, col + 1, self.wolves_left))
                        self.sheep_left = 0
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def Draw(self, win):
        self.Draw_Squares(win)
        for row in range(Rows):
            for col in range(Cols):
                piece = self.board[row][col]
                if piece != 0 and row < 3:
                    piece.Draw_Wolf(win)
                elif piece != 0 and row > 4:
                    piece.Draw_Sheep(win)
