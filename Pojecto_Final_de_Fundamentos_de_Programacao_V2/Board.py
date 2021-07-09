import pygame
from Constantes import Black, Rows, Sheep, Square_Size, Cols, Wolf
from Piece import Pieces

class Board:
    def __init__(self, sleep, wolf):
        self.board = []
        self.wolves_left = wolf = 4 #Só há 4 lobos
        self.sheep_left = sheep = 1 #Só há 1 ovelha
        self.Create_Board()

    #Desenhar o tabuleiro
    def Draw_Squares(self, screen):
        for row in range(Rows):
            for col in range(row % 2, Cols, 2):
                pygame.draw.rect(screen, Black, (row*Square_Size, col*Square_Size, Square_Size, Square_Size))

    #Mover as peças (colocar a peça noutro lugar e apagar o que se encontrava no lugar anterior)
    def Move(self, piece, row, col): 
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.Move(row, col)

    def Get_Piece(self, row, col):
        return self.board[row][col]

    #Criar tabuleiro
    def Create_Board(self):
        for row in range(Rows):
            self.board.append([])
            for col in range(Cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3 and self.wolves_left != 0:
                        self.board[row].append(Pieces(row , col, self.wolves_left))
                        self.wolves_left = self.wolves_left - 1
                    elif row > 4 and self.sheep_left != 0:
                        self.board[row].append(Pieces(row + 0.5, col + 0.5, self.wolves_left))
                        self.sheep_left = 0
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    #Desenhar as peças no respectivo lugar
    def Draw(self, win):
        self.Draw_Squares(win)
        for row in range(Rows):
            for col in range(Cols):
                piece = self.board[row][col]
                if piece != 0 and row < 3:
                    piece.Draw_Wolf(win)
                elif piece != 0 and row > 4:
                    piece.Draw_Sheep(win)

    def Remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0

    def Get_Valid_Moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == Sheep:
            moves.update(self._Traverse_Left(row - 1, max(row - 3, -1), -1, piece.color, left))
            moves.update(self._Traverse_Right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == Wolf:
            moves.update(self._Traverse_Left(row + 1, min(row + 3, Rows), 1, piece.color, left))
            moves.update(self._Traverse_Right(row - 1, min(row + 3, Rows), 1, piece.color, right))

        return moves

    def _Traverse_Left(self, start, stop, step, color, left, skipped = []):
        moves = []
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                else:
                    moves[(r, left)] = last
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1

        return moves

    def _Traverse_Right(self, start, stop, step, color, right, skipped = []):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= Cols:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                else:
                    moves[(r, right)] = last
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        
        return moves
