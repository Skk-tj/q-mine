from board import MinesweeperBoard
from tile import Tile
class GameBoard():
    def __init__(self, w: int, h: int, mines: int):
        self.board = MinesweeperBoard(w,h,mines)
        self.count = 0
        self.total_reveals = (w*h) - mines
        self.visualBoard = []
        self.dimensions = (w,h)
        for row in range(self.getDimensions()[0]):
            rowtoadd = []
            for col in range(self.getDimensions()[1]):
                val = self.board.board[row][col]
                num_mines = self.board.get_mines_around_coordinate((col, row))
                num = len(num_mines)
                if val == "*":
                    tile = Tile((row,col), "MINE", mines)
                else:
                    tile = Tile((row,col),str(num), mines)
                    
                rowtoadd.append(tile)
            self.visualBoard.append(rowtoadd)

    def getDimensions(self):
        return self.dimensions
    
    def getBoard(self):
        return self.visualBoard
    
    def getTile(self, index):
        return self.visualBoard[index[0]][index[1]]

    def handleClick(self, index):
        tile = self.visualBoard[index[0]][index[1]]
        if not tile.getClicked():
            tile.toggleDisplay()
            self.count = self.count + 1
        if tile.type == "MINE":
            tile.setDisplay("EXPLODE")
            # returns true when game is over ?
            return "GAMEOVER"
        elif (self.count == self.total_reveals):
            return "GAMECOMPLETE"