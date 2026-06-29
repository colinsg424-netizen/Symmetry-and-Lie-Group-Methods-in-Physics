import numpy as np
from scipy.linalg import expm

class LieAlgebra:
    def __init__(self, generators, structure_constants=None, name='LieAlgebra'):
        self.generators = generators #Generators of the Lie Algebra
        self.n = len(generators) #Gives the dimension of Lie Algebra(equal to d of Lie group as a manifold)
        self.name = name
        self.f = structure_constants

    #Define commutation with matrix multiplication (Lie bracket)
    def commutator(self, A, B):
        return A @ B - B @ A

    #Frobenius inner product
    def inner(self, A, B):
        return np.trace(A @ B)

    #Check any commutation is also found in the Lie algebra
    def check_closure(self, tol=1e-8):
        n = self.n
        gens = self.generators

        #Gram matrix for correct projection
        G = np.zeros((n, n), dtype=complex)
        for a in range(n):
            for b in range(n):
                G[a, b] = self.inner(gens[a], gens[b])

        for i in range(n):
            for j in range(n):
                comm = self.commutator(gens[i], gens[j])

                rhs = np.zeros(n, dtype=complex)
                for a in range(n):
                    rhs[a] = self.inner(gens[a], comm)

                #solve for coefficients in basis
                coeffs = np.linalg.solve(G, rhs)

                reconstructed = sum(coeffs[k] * gens[k] for k in range(n))

                if np.linalg.norm(comm - reconstructed) > tol:
                    print(f"Closure failed for i={i}, j={j}")
                    return False

        return True

    #Exponential map of a single Lie algebra generator (one-parameter subgroup)
    def exp(self, theta, generator_index):
        T = self.generators[generator_index]
        return expm(1j * theta * T)

    #Exponential map of an arbitrary Lie algebra element (general group element)
    def group_element(self, theta_vector):
        X = sum(theta_vector[a] * self.generators[a] for a in range(self.n))
        return expm(1j * X)

    #Compute structure constants f_{ijk} from [T_i, T_j] = sum_k f_{ijk} T_k
    def compute_structure_constants(self, tol=1e-10):
        n = self.n
        gens = self.generators

        # Gram matrix G_ij = <T_i, T_j>
        G = np.zeros((n, n), dtype=complex)
        for a in range(n):
            for b in range(n):
                G[a, b] = self.inner(gens[a], gens[b])

        # structure constants tensor
        f = np.zeros((n, n, n), dtype=complex)

        for i in range(n):
            for j in range(n):

                #commutator [T_i, T_j]
                comm = self.commutator(gens[i], gens[j])

                # projection RHS_k = <T_k, comm>
                rhs = np.zeros(n, dtype=complex)
                for a in range(n):
                    rhs[a] = self.inner(gens[a], comm)

                # solve G f = rhs (stable version)
                coeffs = np.linalg.lstsq(G, rhs, rcond=None)[0]

                # store f_{ij}^k
                for k in range(n):
                    f[i, j, k] = coeffs[k]

        self.f = f
        return f
    
    def adjoint_representation(self):
        if self.f is None:
            self.compute_structure_constants()

        n = self.n

        #ad[a] is an n×n matrix
        ad = np.zeros((n, n, n), dtype=complex)

        for a in range(n):
            for b in range(n):
                for c in range(n):
                    # (ad_a)_bc = f_{ab}^c
                    ad[a, b, c] = self.f[a, b, c]

        return ad
    
    def killing_form(self):
        ad = self.adjoint_representation()
        n = self.n

        K = np.zeros((n, n), dtype=complex)

        for a in range(n):
            for b in range(n):
                K[a, b] = np.trace(ad[a] @ ad[b])
        return K
    
    def casimir(self):
        K = self.killing_form()
        K_inv = np.linalg.inv(K)
        n = self.n
        dim = self.generators[0].shape[0]
        C = np.zeros((dim,dim), dtype=complex)
        for a in range(n):
            for b in range(n):
                C += K_inv[a,b] * self.generators[a] @ self.generators[b]
        return C
    def check_jacobi_identity(self, tol=1e-8):
        gens = self.generators
        n = len(gens)

        for i in range(n):
            Xi = gens[i]

            for j in range(n):
                Xj = gens[j]

                for k in range(n):
                    Xk = gens[k]

                    # Jacobi combination
                    jacobi = (
                        self.commutator(Xi, self.commutator(Xj, Xk)) +
                        self.commutator(Xj, self.commutator(Xk, Xi)) +
                        self.commutator(Xk, self.commutator(Xi, Xj))
                    )
                    if np.linalg.norm(jacobi) > tol:
                        print(f"Jacobi failed at (i={i}, j={j}, k={k})")
                        return False
        print("Jacobi identity holds for all generator triples.")
        return True
