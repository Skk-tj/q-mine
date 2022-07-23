import pygame
import os
from gameboard import GameBoard

class Game():
    def __init__(self, board, dimensions):
        self.winOrLose = "NONE"
        self.inGame = True
        self.board = board
        self.dimensions = dimensions
        self.display = pygame.display.set_mode(self.dimensions)
        self.tileSize = self.dimensions[0] // self.board.getDimensions()[1], self.dimensions[1] // self.board.getDimensions()[0]
        self.loadImages()
        
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        while self.inGame:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    ingame = False
                if (event.type == pygame.MOUSEBUTTONDOWN):
                    position = pygame.mouse.get_pos()
                    self.handleClick(position)
            self.draw()
            pygame.display.flip()
            clock.tick(60)
        if self.winOrLose == "LOSS":
            image = self.images["death"]
        else:
            image = self.images["win"]
        image = pygame.transform.scale(image, (600, 200))
        self.display.blit(image, (self.dimensions[0]//2 - 300, self.dimensions[1]//2 - 100))
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()

    def draw(self):
        initial = (0,0)
        for row in range(self.board.getDimensions()[0]):
            for col in range(self.board.getDimensions()[1]):
                tile = self.board.getTile((row, col))
                image = self.images[tile.getDisplay()]
                self.display.blit(image,initial)
                initial = initial[0] + self.tileSize[0], initial[1]
            initial = 0, initial[1] + self.tileSize[1]
    
    def loadImages(self):
        self.images = {}
        for fileName in os.listdir("images"):
            if(fileName.endswith(".png")):
                image = pygame.image.load(r"images/"+fileName)
                firstname = fileName.split(".")[0]
                if (firstname != "death" or firstname != "win"):
                    image = pygame.transform.scale(image, self.tileSize)
                self.images[firstname] = image

    def handleClick(self, position):
        index = position[1] // self.tileSize[1], position[0] // self.tileSize[0]
        result = self.board.handleClick(index)
        if result == "GAMEOVER":
            pygame.display.flip()
            self.winOrLose = "LOSS"
            self.inGame = False
        if result == "GAMECOMPLETE":
            self.inGame = False
