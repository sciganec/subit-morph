# Metrics E, A, T

## Overview

The SUBIT‑morph framework reduces the structure of an informational flow to three global morphological metrics. These metrics describe randomness, directional bias, and radial distribution within the 64‑state frequency profile derived from 6‑bit sliding windows. Together they form the SUBIT‑address.

---

## Entropy (E)

Entropy measures the degree of randomness in the 64‑state distribution.

Let p[k] be the normalized frequency of state k.

```
H = − Σ p[k] * log₂(p[k])
E = H / 6
```

Interpretation:

- **Low E** — ordered, repetitive, structurally constrained streams  
- **High E** — noisy, uniform, high‑variability streams  

E is normalized to the range 0–1.

---

## Anisotropy (A)

Anisotropy measures directional structure in the distribution by examining how mass is arranged in the 4×4×4 cube embedding.

Each state k is mapped to coordinates vₖ = (x, y, z).

Mean vector:

```
μ = Σ p[k] * vₖ
```

Covariance matrix:

```
C = Σ p[k] * (vₖ − μ)(vₖ − μ)ᵀ
```

Let λ₁ ≥ λ₂ ≥ λ₃ be eigenvalues of C.

Anisotropy:

```
A = 1 − (λ₂ / λ₁)
```

Interpretation:

- **Low A** — isotropic, evenly distributed structure  
- **High A** — strong directional bias, elongated or polarized structure  

A ranges from 0 to 1.

---

## Morphological Tension (T)

Tension measures radial variation around the center μ.

Radial distance:

```
rₖ = ||vₖ − μ||
```

Tension:

```
T = std(rₖ) / std(p[k])
```

Interpretation:

- **Low T** — smooth, balanced radial distribution  
- **High T** — concentrated, polarized, or uneven radial mass  

T is scale‑invariant due to the ratio of standard deviations.

---

## Combined Interpretation

The triplet (E, A, T) forms the SUBIT‑address of a stream.

- E describes **randomness**  
- A describes **directionality**  
- T describes **radial structure**  

Together they define a compact, model‑independent coordinate in morphological space.

---

## Properties

- independent of semantics  
- independent of model architecture  
- stable across encodings  
- applicable to any byte stream  
- compact and comparable  

These metrics form the core analytical layer of the SUBIT‑morph system.
