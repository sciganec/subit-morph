# SUBIT‑Address

## Concept

The SUBIT‑address is a three‑dimensional coordinate that locates an informational flow within morphological space. It is derived from the 64‑state SUBIT‑morph and summarizes its global structural properties. The address is defined as:

```
(E, A, T)
```

Each component captures a distinct aspect of morphological behavior: randomness, directionality, and radial distribution.

---

## Entropy (E)

Entropy measures the degree of randomness in the 64‑state distribution.

Let p[k] be the normalized frequency of state k.

```
H = − Σ p[k] * log₂(p[k])
E = H / 6
```

E ranges from 0 to 1.

- Low E indicates order, repetition, or structural regularity.
- High E indicates noise, uniformity, or high variability.

---

## Anisotropy (A)

Anisotropy measures directional structure in the distribution.

Each state k is mapped to a 3‑dimensional vector vₖ using its 4×4×4 cube coordinates.  
The mean vector is:

```
μ = Σ p[k] * vₖ
```

The covariance matrix is:

```
C = Σ p[k] * (vₖ − μ)(vₖ − μ)ᵀ
```

Let λ₁ ≥ λ₂ ≥ λ₃ be the eigenvalues of C.

Anisotropy is defined as:

```
A = 1 − (λ₂ / λ₁)
```

A ranges from 0 to 1.

- Low A indicates isotropic, evenly distributed structure.
- High A indicates strong directional bias.

---

## Morphological Tension (T)

Tension measures how mass is distributed radially around the center μ.

For each state:

```
rₖ = ||vₖ − μ||
```

Tension is defined as:

```
T = std(rₖ) / std(p[k])
```

- Low T indicates smooth radial distribution.
- High T indicates concentrated or polarized mass.

---

## Interpretation

The SUBIT‑address provides a compact summary of morphological identity.

- Streams with similar addresses are morphological isomorphs.
- Streams with different semantic content may share the same address.
- The address enables clustering, comparison, and classification of flows.

---

## Properties

- Independent of semantics  
- Independent of model architecture  
- Stable across encodings  
- Applicable to any byte stream  
- Compact and comparable  

The SUBIT‑address is the canonical coordinate system for morphological analysis.

---

## Output Format

A complete SUBIT‑address is expressed as:

```
E: <float>
A: <float>
T: <float>
```

or as a tuple:

```
(E, A, T)
```

This coordinate is included in every SUBIT‑morph output.
