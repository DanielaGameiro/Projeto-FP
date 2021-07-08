import pygame

#Tamanho do ecran
Cumprimento = 1300
Largura = 800

#Tamanho do tabuleiro
Width = 800
Height = 800

#Linhas e colunas
Rows, Cols = 8, 8

#Tamanho dos quadrados
Square_Size = Width // (Cols)

#Cores
Black = (0, 0, 0)
White = (255, 255, 255)

#Peças
Sheep = pygame.image.load('Mini_Sheep.png')
Wolf = pygame.image.load('Mini_Wolf.png')
