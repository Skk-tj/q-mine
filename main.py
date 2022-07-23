from gameboard import GameBoard
from game import Game
import q_measure

if __name__ == "__main__":
    #qc = q_measure.get_q_circuit()
    #print(q_measure.get_measurement_result_for_one_shot(qc))
    gameboard = GameBoard(9,9,10)
    dimensions = (900, 600)
    game = Game(gameboard, dimensions)
    game.run()
