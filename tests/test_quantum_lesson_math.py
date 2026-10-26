"""Independent circuit checks for the phase convention drawn in the teaching videos."""

import importlib.util
from pathlib import Path

import numpy as np
import pytest
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFTGate
from qiskit.quantum_info import Statevector, partial_trace

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "phase_math", ROOT / "tools/quantum_videos/phase_math.py"
)
phase_math = importlib.util.module_from_spec(spec)
spec.loader.exec_module(phase_math)


@pytest.mark.parametrize("theta", [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 1.3])
@pytest.mark.parametrize("sine", [False, True])
def test_rendered_probability_against_controlled_phase_circuit(theta, sine):
    circuit = QuantumCircuit(2)
    circuit.x(0)
    circuit.h(1)
    circuit.cp(theta, 1, 0)
    if sine:
        circuit.sdg(1)
    circuit.h(1)
    actual = Statevector.from_instruction(circuit).probabilities([1])[0]
    assert actual == pytest.approx(phase_math.hadamard_probability(theta, sine))


@pytest.mark.parametrize("energy", [-1.6, -0.8, 0.8, 1.6])
def test_reconstruction_and_aliasing(energy):
    time = 0.5
    pc = phase_math.hadamard_probability(-energy * time)
    ps = phase_math.hadamard_probability(-energy * time, sine=True)
    assert phase_math.principal_energy(pc, ps, time) == pytest.approx(energy)
    alias = energy + 2 * np.pi / time
    assert phase_math.hadamard_probability(-alias * time) == pytest.approx(pc)
    assert phase_math.hadamard_probability(-alias * time, sine=True) == pytest.approx(
        ps
    )


def test_two_bit_qpe_reads_normalized_phase():
    circuit = QuantumCircuit(3)
    circuit.x(2)
    circuit.h([0, 1])
    for j in range(2):
        circuit.cp((2**j) * np.pi / 2, j, 2)
    circuit.append(QFTGate(2).inverse(), [0, 1])
    probabilities = Statevector.from_instruction(circuit).probabilities_dict([0, 1])
    assert probabilities["01"] == pytest.approx(1)


def test_bv_zero_target_can_reveal_the_whole_secret():
    circuit = QuantumCircuit(4)
    circuit.h([1, 2, 3])
    # Non-palindromic secret 110; target q0, logical input order q3 q2 q1.
    circuit.cx(3, 0)
    circuit.cx(2, 0)
    circuit.h(range(4))
    p = Statevector.from_instruction(circuit).probabilities_dict()
    assert p["0000"] == pytest.approx(0.5)
    assert p["1101"] == pytest.approx(0.5)


def test_partial_overlap_keeps_local_coherence():
    # (|0>|0> + |1>|+>)/sqrt(2), with top bit q1 and bottom q0.
    state = Statevector([1 / np.sqrt(2), 0, 0.5, 0.5])
    rho = partial_trace(state, [0]).data
    assert rho[0, 1] == pytest.approx(1 / (2 * np.sqrt(2)))
    assert np.linalg.det(rho) > 0  # Entangled pure input, yet nonzero coherence.
