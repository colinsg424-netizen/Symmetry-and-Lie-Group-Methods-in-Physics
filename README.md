# Lie Algebra for Physics Applications

A Python framework for the construction and analysis of finite-dimensional Lie algebras using matrix representations.

The project is designed for applications in theoretical physics, particularly quantum mechanics and gauge theory, and provides computational tools for exploring Lie algebra structure, including commutators, structure constants, Killing forms, Casimir operators, and exponential maps.

A key application is included demonstrating quantum spin-½ dynamics via the $\mathfrak{su}(2)$ Lie algebra.

---

# Mathematical Framework

This framework represents Lie algebras as matrix subalgebras of $\mathfrak{gl}(n, \mathbb{C})$. A Lie algebra $\mathfrak{g}$ is a vector space equipped with the Lie bracket:

$$
[X, Y] = XY - YX
$$

where $X, Y \in \mathfrak{g}$ are matrices in a chosen representation.

---

## Matrix Basis Construction

The implementation constructs Lie algebra bases using elementary matrix units:

$$
(E_{ij})_{kl} = \delta_{ik}\delta_{jl}
$$

From these, generators are formed for standard Lie algebras such as $\mathfrak{su}(n)$ and $\mathfrak{u}(n)$.

---

## Construction of $\mathfrak{su}(n)$

The special unitary algebra is constructed using:

Symmetric generators:

$$
S_{ij} = \frac{1}{2}(E_{ij} + E_{ji})
$$

Antisymmetric generators:

$$
A_{ij} = -\frac{i}{2}(E_{ij} - E_{ji})
$$

- Diagonal traceless generators completing the basis

These satisfy closure under the Lie bracket:

$$
[T_a, T_b] = \sum_c f_{abc} T_c
$$

where $f_{abc}$ are the structure constants.

---

## Construction of $\mathfrak{u}(n)$

The unitary algebra is obtained as:

$$
\mathfrak{u}(n) = \mathfrak{su}(n) \oplus \mathfrak{u}(1)
$$

with identity generator:

$$
T_0 = \frac{1}{\sqrt{2n}} I_n
$$

---

## Lie Algebra Structure

The Lie bracket defines the algebraic structure:

$$
[X, Y] = XY - YX
$$

In a basis $\{T_a\}$, this induces structure constants:

$$
[T_a, T_b] = \sum_c f_{abc} T_c
$$

---

## Adjoint Representation

The adjoint representation is defined by:

$$
\mathrm{ad}_X(Y) = [X, Y]
$$

and in components:

$$
(\mathrm{ad}_{T_a})_{bc} = f_{abc}
$$

---

## Killing Form

The Killing form is computed as:

$$
K(X, Y) = \mathrm{Tr}(\mathrm{ad}_X \, \mathrm{ad}_Y)
$$

and defines an invariant bilinear structure on the algebra.

---

## Casimir Operator

The quadratic Casimir operator is:

$$
C_2 = \sum_{a,b} (K^{-1})_{ab} T_a T_b
$$

and commutes with all generators:

$$
[C_2, T_a] = 0
$$

---

## Lie Group Elements

Lie group elements are obtained via the exponential map:

$$
U = e^{X}, \quad X \in \mathfrak{g}
$$

In physics applications:

$$
U(t) = e^{-iHt}
$$

---

## Physical Application: Quantum Spin Dynamics

As an application, the framework is used to model spin-½ dynamics using $\mathfrak{su}(2)$.

Spin operators satisfy:

$$
[S_i, S_j] = i \epsilon_{ijk} S_k
$$

A spin in a magnetic field evolves under:

$$
H = \mathbf{B} \cdot \mathbf{S}
$$

with time evolution:

$$
\psi(t) = e^{-iHt} \psi(0)
$$

This produces quantum spin precession (Larmor precession) on the Bloch sphere.

---

# Examples

## 1. Constructing a Lie Algebra

```python
from groups import SU
from lie_algebra import LieAlgebra

gens = SU(2)
alg = LieAlgebra(gens, name="su(2)")

print("Number of generators:", alg.n)
print("First generator:\n", alg.generators[0])
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

f = alg.compute_structure_constants()

print("Structure constants shape:", f.shape)
print("Example f[0,1,k]:", f[0,1])
```
