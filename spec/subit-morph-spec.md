# SUBIT‑Morph Specification

## Definition

A SUBIT‑morph is a morphological fingerprint of an informational flow. It is derived from a sliding window of 6 bits applied to a byte stream, producing a 64‑state frequency distribution. This distribution is represented as an 8×8 grid and can be embedded into a 4×4×4 cube. Three metrics—entropy, anisotropy, and morphological tension—form the SUBIT‑address, a coordinate locating the flow in morphological space.

## Input Stream

Any input is treated as a raw byte sequence.

- Text is encoded as UTF‑8 unless otherwise specified.
- Binary data is used as‑is.
- No semantic interpretation is applied.

Let the byte stream be:

```
b₀, b₁, b₂, …, bₙ
```

Each byte is expanded into 8 bits, forming a bitstream:

```
β = β₀ β₁ β₂ … βₘ
```

## 6‑Bit Sliding Window

A sliding window of width 6 is applied to the bitstream with stride 1.

For each position i:

```
sᵢ = βᵢ βᵢ₊₁ βᵢ₊₂ βᵢ₊₃ βᵢ₊₄ βᵢ₊₅
kᵢ = integer value of sᵢ in [0, 63]
```

The total number of windows is:

```
N = m − 5
```

## 64‑State Frequency Distribution

For each state k ∈ {0…63}:

```
count[k] = number of windows where kᵢ = k
p[k] = count[k] / N
```

The vector p is the morphological profile of the stream.

## 8×8 Morphological Grid

The 64 states are arranged into an 8×8 grid:

```
row = k // 8
col = k % 8
grid[row][col] = p[k]
```

This grid is the canonical 2D representation of a SUBIT‑morph.

## 4×4×4 Morphological Cube

A volumetric embedding is defined by splitting the 6‑bit index:

```
x = (k >> 4) & 0b11
y = (k >> 2) & 0b11
z =  k       & 0b11
cube[x][y][z] = p[k]
```

This representation reveals directional and radial structure.

## Metric: Entropy (E)

Entropy measures randomness of the distribution.

```
H = − Σ p[k] * log₂(p[k])
E = H / 6
```

E ranges from 0 (fully ordered) to 1 (maximally random).

## Metric: Anisotropy (A)

Each state k is mapped to a 3‑dimensional vector vₖ using the cube coordinates (x, y, z).

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

A measures directional bias.

## Metric: Morphological Tension (T)

Radial distance of each state:

```
rₖ = ||vₖ − μ||
```

Tension:

```
T = std(rₖ) / std(p[k])
```

T measures how mass is distributed relative to the center.

## SUBIT‑Address

Each informational flow receives a coordinate:

```
(E, A, T)
```

This is its location in morphological space.

Flows with similar addresses are morphological isomorphs, regardless of semantic content.

## Normalization

- p[k] sums to 1.
- E is normalized by dividing by 6.
- A is bounded by construction.
- T is scale‑invariant due to ratio of standard deviations.

No additional normalization is applied.

## Invariance Properties

SUBIT‑morphs are invariant under:

- semantic changes  
- encoding of meaning  
- model architecture  
- tokenization  
- data type (text, code, DNA, audio, logs, model output)

They are sensitive only to the morphological structure of the byte stream.

## Output Formats

A SUBIT‑morph consists of:

- the 64‑state frequency vector  
- the 8×8 grid  
- the 4×4×4 cube  
- the SUBIT‑address (E, A, T)

These components form the complete morphological description.

## Reference Implementation

The reference implementation in `/src/python` defines:

- byte‑to‑bit conversion  
- sliding window extraction  
- frequency computation  
- grid and cube construction  
- metric computation  

This implementation is the canonical baseline for reproducing results.

## Specification Status

This document defines version 1.0 of the SUBIT‑morph standard. Future versions may extend:

- alternative window sizes  
- higher‑dimensional embeddings  
- additional morphological metrics  
- domain‑specific adaptations  

The core 6‑bit, 64‑state system is stable and canonical.
