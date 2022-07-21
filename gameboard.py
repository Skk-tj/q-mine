from board import MinesweeperBoard
class GameBoard():
    def __init__(self, w: int, h: int, mines: int):
        self.board = MinesweeperBoard(w,h,mines)
        self.dimensions = (w,h)
        for row in self.board.board:
            for val in row:
                print(val, end = " ")
            print()

    def getDimensions(self):
        return self.dimensions