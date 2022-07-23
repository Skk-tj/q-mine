class Tile():
    def __init__(self, index, type, neighbour_mines):
        self.type = type
        self.display = "NONE"
        self.clicked = False
        self.mines = neighbour_mines
        self.index = index

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getDisplay(self):
        return self.display 

    def getClicked(self):
        return self.clicked
    
    def handleClick(self):
        if self.clicked == False:
            self.display = self.type
            self.clicked = True
    
    def toggleDisplay(self):
        if self.clicked == False:
            self.display = self.type
            self.clicked = True

    def setDisplay(self, type):
        self.display = type

    def getMines(self):
        return self.mines
        