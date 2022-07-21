from board import MinesweeperBoard
from tile import Tile
class GameBoard():
    def __init__(self, w: int, h: int, mines: int):
        self.board = MinesweeperBoard(w,h,mines)
        self.visualBoard = []
        self.dimensions = (w,h)
        for row in self.board.board:
            rowtoadd = []
            for val in row:
                if val == 1:
                    tile = Tile("MINE")
                else:
                    tile = Tile("NONE")
                rowtoadd.append(tile)
            self.visualBoard.append(rowtoadd)

    def getDimensions(self):
        return self.dimensions
    
    def getBoard(self):
        return self.visualBoard
    
    def getTile(self, index):
        return self.visualBoard[index[0]][index[1]]