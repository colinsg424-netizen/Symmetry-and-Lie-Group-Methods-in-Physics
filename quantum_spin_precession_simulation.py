import numpy as np
from scipy.linalg import expm
from groups import SU

# get SU(2) generators
gens = SU(2)

# spin operators (assuming your SU(2) ordering gives Pauli-like basis)
Sx = gens[0]
Sy = gens[1]
Sz = gens[2]

# magnetic field
Bx, By, Bz = 0.0, 0.0, 1.0

# Hamiltonian (set gamma = 1, ħ = 1 units)
H = Bx * Sx + By * Sy + Bz * Sz

# initial state ψ(0) (spin up)
psi0 = np.array([1, 0], dtype=complex)

# time value
t = 5.0

# time evolution operator
U = expm(-1j * H * t)

# evolved state ψ(t)
psi_t = U @ psi0

# print result in physics notation
print(f"ψ(t = {t}) =")
print(psi_t)