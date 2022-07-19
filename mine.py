import matplotlib.pyplot as plt
import qiskit
import qiskit.visualization as qv

if __name__ == "__main__":
    # Initialize qubits
    # 1st qubit is the photon bit
    # 2nd qubit is the bomb bit
    qc = qiskit.QuantumCircuit(2)

    # Both qubits to |0>
    qc.i(0)
    qc.i(1)

    qc.barrier()

    qc.h(0)

    qc.barrier()

    # The bomb
    qc.cx(0, 1)

    qc.barrier()

    qc.h(0)

    qc.measure_all()

    qc.draw(output='mpl')
    plt.show()

    backend = qiskit.BasicAer.get_backend('qasm_simulator')
    shots = 1024

    results = qiskit.execute(qc, backend=backend, shots=shots).result()
    answer = results.get_counts()

    qv.plot_histogram(answer, title="Quantum bomb")
    plt.show()
