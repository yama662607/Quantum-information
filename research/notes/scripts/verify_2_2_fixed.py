import numpy as np
from qiskit.quantum_info import Kraus, SuperOp, Choi, DensityMatrix

# 1. Bit Flip Channel の Kraus 演算子を定義
p = 0.3  # 反転確率
I = np.eye(2)  # noqa: E741
X = np.array([[0, 1], [1, 0]])

K0 = np.sqrt(1 - p) * I
K1 = np.sqrt(p) * X

# Kraus オブジェクトの作成
channel = Kraus([K0, K1])

# 2. 表現の変換
# Natural Representation (Qiskitでは SuperOp)
super_op = SuperOp(channel)
print("--- Superoperator (Natural Rep) ---")
print(np.round(super_op.data, 3))

# Choi Representation
choi_op = Choi(channel)
print("\n--- Choi Matrix ---")
print(np.round(choi_op.data, 3))

# 3. 性質の確認
print(f"\nIs CP? {channel.is_cp()}")
print(f"Is TP? {channel.is_tp()}")

# 4. 状態への適用
rho_in = np.array([[1, 0], [0, 0]])  # |0><0|
# Correct way depending on Qiskit version, assume 2.x needs DensityMatrix object for evolve
rho_dm = DensityMatrix(rho_in)
rho_out = rho_dm.evolve(channel)
print("\n--- Input State (|0><0|) ---")
print(rho_in)
print("--- Output State ---")
print(np.round(rho_out.data, 3))
