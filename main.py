from board import MinesweeperBoard
import q_measure

if __name__ == "__main__":
    qc = q_measure.get_q_circuit()
    print(q_measure.get_measurement_result_for_one_shot(qc))
