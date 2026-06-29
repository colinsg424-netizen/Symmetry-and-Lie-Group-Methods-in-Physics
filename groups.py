import numpy as np
from scipy.linalg import expm
#Function to create elementary matrices
def E(i,j,n):
    M = np.zeros((n,n), dtype=complex)
    M[i,j] = 1
    return M


#Construction of list of any generators for Special Unitary groups
def SU(n):
    generators = []

    for i in range(n):
        for j in range(i+1, n):
            S = 0.5 * (E(i,j,n) + E(j,i,n))
            A = -0.5j * (E(i,j,n) - E(j,i,n))
            generators.append(S)
            generators.append(A)

    for k in range (1,n):
        H = np.zeros((n,n), dtype=complex)
        for i in range(k):
            H[i,i] = 1
        H[k,k] = -k
        H = H / np.sqrt(2*k*(k+1))
        generators.append(H)
    return generators
#Construction of list of any generators for Unitary groups
def U(n):
    generators = SU(n).copy()
    I = np.eye(n, dtype=complex)
    T0 = (1 / np.sqrt(2 * n)) * I
    generators.append(T0)

    return generators