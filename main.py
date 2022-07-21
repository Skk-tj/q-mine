from board import MinesweeperBoard
from game import Game
import q_measure

if __name__ == "__main__":
    qc = q_measure.get_q_circuit()
    print(q_measure.get_measurement_result_for_one_shot(qc))
    board = MinesweeperBoard(9,9,10)
    dimensions = (900, 600)
    game = Game(board, dimensions)
    game.run()
