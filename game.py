import pygame
import os
from board import MinesweeperBoard

class Game():
    def __init__(self, board, dimensions):
        self.board = board
        self.dimensions = dimensions
        
    def run(self):
        pygame.init()
        display = pygame.display.set_mode(self.dimensions)
        ingame = True
        while ingame:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    ingame = False
            pygame.display.flip()
        pygame.quit()