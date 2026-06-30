# Lie Algebra for Physics Applications

A Python framework for simulating physical systems governed by Lie group symmetries using matrix representations.

The library connects abstract symmetry structures directly to physical dynamics, including quantum time evolution, conserved quantities, and rotational symmetries.

A key application demonstrates quantum spin-½ precession in a magnetic field using the $\mathfrak{su}(2)$ Lie algebra, where time evolution is generated through Hamiltonian-driven unitary dynamics.

---
# 

# Mathematical Framework

This framework represents Lie algebras as matrix subalgebras of $\mathfrak{gl}(n, \mathbb{C})$.

The Lie bracket is defined by:

$$
[X, Y] = XY - YX
$$

where $X, Y$ are matrices in a chosen representation. This operation encodes how physics observables interact under symmetry transformations.

---

## Matrix Basis Construction

The elementary matrix units are defined as:

$$
(E_{ij})_{kl} = \delta_{ik}\delta_{jl}
$$

These are used to construct Lie algebra generators used in physics symmetry groups.

---

## Construction of $\mathfrak{su}(n)$

The special unitary algebra $\mathfrak{su}(n)$ describes symmetries of quantum systems with $n$ internal states.

Generators are constructed as:

**Symmetric part:**

$$
S_{ij} = \frac{1}{2}(E_{ij} + E_{ji})
$$

**Antisymmetric part:**

$$
A_{ij} = -\frac{i}{2}(E_{ij} - E_{ji})
$$

Diagonal traceless generators complete the basis that underlies quantum mechanical symmetries.

---

## Construction of $\mathfrak{u}(n)$

The unitary algebra is:

$$
\mathfrak{u}(n) = \mathfrak{su}(n) \oplus \mathfrak{u}(1)
$$

with identity generator:

$$
T_0 = \frac{1}{\sqrt{2n}} I_n
$$

This normalization ensures consistent physical scaling across generators.

---

## Jacobi Identity

The Lie bracket satisfies:

$$
[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0
$$

This implementation verifies the Jacobi identity numerically across all generator triples.

---

## Structure Constants

In a basis $\{T_a\}$:

$$
[T_a, T_b] = \sum_c f_{abc} T_c
$$

The structure constants are computed using projection onto the generator basis. These coefficients decide the dynamics of a physical system.

---

## Adjoint Representation

Defined by:

$$
\mathrm{ad}_X(Y) = [X, Y]
$$

with components:

$$
(\mathrm{ad}_{T_a})_{bc} = f_{abc}
$$

This represents how a Lie algebra's own symmetries act on the algebra itself.

---

## Killing Form

The Killing form provides an invariant measure of symmetry structure.

Computed as:

$$
K(X, Y) = \mathrm{Tr}(\mathrm{ad}_X \, \mathrm{ad}_Y)
$$

It is used in physics to compare symmetry algebras.

---

## Casimir Operator

The quadratic Casimir is:

$$
C_2 = \sum_{a,b} (K^{-1})_{ab} T_a T_b
$$

and commutes with all generators. This makes it a conserved quantity under symmetry transformations.

---

## Lie Group Exponential Map
Continuous symmetry transformations are generated via:

$$
U = e^{iX}
$$

In quantum mechanics -- as seen in the Larmor precession simulation -- this becomes the time evolution operator:

$$
U = e^{-iHt}
$$

This is the central mechanics connecting Lie algebras to dynamic quantum systems.

---

## Physical Application: Quantum Spin-½ Dynamics

The framework is applied to $\mathfrak{su}(2)$.

Spin operators satisfy:

$$
[S_i, S_j] = i \epsilon_{ijk} S_k
$$

The Hamiltonian for a spin in a magnetic field is:

$$
H = \mathbf{B} \cdot \mathbf{S}
$$

Time evolution is computed as:

$$
\psi(t) = e^{-iHt} \psi(0)
$$

This models quantum spin precession under Larmor dynamics, where SU(2) symmetry generators govern the evoltuion of the quantum state.

---

# Examples

## 1. Constructing a Lie Algebra

```python
from groups import SU
from lie_algebra import LieAlgebra

gens = SU(2)
alg = LieAlgebra(gens, name="su(2)")

print("Number of generators:", alg.n)
```

## 2. Checking Lie Algebra Closure

```python
from groups import SU
from lie_algebra import LieAlgebra

gens = SU(2)
alg = LieAlgebra(gens, name="su(2)")

print("Closed under commutator:", alg.check_closure())
```

## 3. Computing Structure Constants

```python
from groups import SU
from lie_algebra import LieAlgebra

gens = SU(2)
alg = LieAlgebra(gens, name="su(2)")
```
