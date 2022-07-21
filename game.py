import pygame
import os
from gameboard import GameBoard

class Game():
    def __init__(self, board, dimensions):
        self.board = board
        self.dimensions = dimensions
        self.tileSize = self.dimensions[0] // self.board.getDimensions()[1], self.dimensions[1] // self.board.getDimensions()[0]
        self.loadImages()
        
    def run(self):
        pygame.init()
        self.display = pygame.display.set_mode(self.dimensions)
        ingame = True
        while ingame:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    ingame = False
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        initial = (0,0)
        for row in range(self.board.getDimensions()[0]):
            for col in range(self.board.getDimensions()[1]):
                image = self.images["NONE"]
                self.display.blit(image,initial)
                initial = initial[0] + self.tileSize[0], initial[1]
            initial = 0, initial[1] + self.tileSize[1]
    
    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if(fileName.endswith(".png")):
                image = pygame.image.load(r"images/"+fileName)
                image = pygame.transform.scale(image, self.tileSize)
                self.images[fileName.split(".")[0]] = image