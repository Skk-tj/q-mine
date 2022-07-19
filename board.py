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

        mine_coordinates = random.sample(all_coordinates, mines)

        for c in mine_coordinates:
            self.board[c[1]][c[0]] = 1

    def __repr__(self):
        str_repr_of_board = "\n".join([str(row) for row in self.board])

        return f"""
Current number of mines: {self.current_number_of_mines}
        
{str_repr_of_board}
        """
