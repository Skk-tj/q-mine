class Tile():
    def __init__(self, type):
        self.type = type
        self.clicked = False
    
    def getType(self):
        return self.type