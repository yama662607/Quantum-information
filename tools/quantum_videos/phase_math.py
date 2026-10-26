"""Phase convention shared by the rendered curves and independent circuit tests."""

import numpy as np


def hadamard_probability(theta, sine=False):
    """Probability of probe 0 after H, C(U), optional S†, H; U|u> = exp(iθ)|u>."""
    return (1 + (np.sin(theta) if sine else np.cos(theta))) / 2


def principal_energy(p_cos, p_sin, time):
    """Return the principal-branch estimate; other energies differ by 2π/time (ℏ=1)."""
    if time <= 0:
        raise ValueError("time must be positive")
    return -np.arctan2(2 * p_sin - 1, 2 * p_cos - 1) / time
