import random
import itertools


class MinesweeperBoard:
    def __init__(self, w: int, h: int, mines: int):
        """
        Generate a random minesweeper board.

        :param w: The width of the board
        :param h: The height of the board
        :param mines: Number of mines. The number of mine must not be greater than w*h.
        :return: A random minesweeper board, represented as an 2D list. 0 means no mine, 1 means a mine.
        """
        if mines >= w * h:
            raise "Number of mines greater than the board's dimension. "

        self.original_number_of_mines = mines
        self.current_number_of_mines = mines
        self.board = [[0] * w for _ in range(h)]

        # Populate the mines
        all_coordinates = list(itertools.product(range(w), range(h)))

        self.mine_coordinates = random.sample(all_coordinates, mines)

        for c in self.mine_coordinates:
            self.board[c[1]][c[0]] = 1

    def __repr__(self):
        str_repr_of_board = "\n".join([str(row) for row in self.board])

        return f"""
Current number of mines: {self.current_number_of_mines}
        
{str_repr_of_board}
        """

    def get_number_of_mines_around_coordinate(self, coordinate: tuple[int, int]) -> int:
        """
        Get the number of mines around a coordinate.

        :param coordinate: In (x, y) format, x is the column and y is the row, both from top to bottom.
        :return: Number of mines.
        """
        rows, cols = len(self.board), len(self.board[0])

        if coordinate[1] >= rows:
            return 0

        if coordinate[0] >= cols:
            return 0

        result = 0

        # top segment
        if coordinate[1] - 1 >= 0:
            # top center
            if self.board[coordinate[1] - 1][coordinate[0]] == 1:
                result += 1

            # top left
            if coordinate[0] - 1 >= 0:
                if self.board[coordinate[1] - 1][coordinate[0] - 1] == 1:
                    result += 1

            # top right
            if coordinate[0] + 1 < cols:
                if self.board[coordinate[1] - 1][coordinate[0] + 1] == 1:
                    result += 1

        # middle left
        if coordinate[0] - 1 >= 0:
            if self.board[coordinate[1]][coordinate[0] - 1] == 1:
                result += 1

        # middle right
        if coordinate[0] + 1 < cols:
            if self.board[coordinate[1]][coordinate[0] + 1] == 1:
                result += 1

        # bottom segment
        if coordinate[1] + 1 < rows:
            # bottom center
            if self.board[coordinate[1] + 1][coordinate[0]] == 1:
                result += 1

            # bottom left
            if coordinate[0] - 1 >= 0:
                if self.board[coordinate[1] + 1][coordinate[0] - 1] == 1:
                    result += 1

            # bottom right
            if coordinate[0] + 1 <= cols:
                if self.board[coordinate[1] + 1][coordinate[0] + 1] == 1:
                    result += 1

        return result
