# Glossary

## SUBIT‑morph
A byte‑level morphological analysis framework that converts any data stream into a 64‑state distribution, an 8×8 grid, and a three‑component SUBIT‑address. It measures informational *form* rather than meaning.

## 6‑bit window
The fundamental atom of SUBIT‑morph. A sliding window of six consecutive bits produces one of 64 possible states. Overlapping windows generate the full morphological fingerprint.

## 64‑state distribution
A frequency vector of length 64 produced by scanning a bitstring with 6‑bit windows. It captures the structural tendencies of the stream, including repetition, alphabet size, and formatting patterns.

## 8×8 grid
A spatial projection of the 64‑state distribution. Each of the 64 frequencies is placed into a fixed 8×8 layout, revealing clusters, gradients, symmetry, and voids.

## 4×4×4 cube
A geometric embedding of the 64 states. Each state maps to a coordinate (x, y, z) in a 4×4×4 cube using the top, middle, and bottom bit pairs. This embedding enables geometric metrics.

## SUBIT‑address
A three‑component coordinate summarizing morphology:
- **Entropy (E)** — randomness or uniformity  
- **Anisotropy (A)** — directional bias in the cube  
- **Tension (T)** — radial variation around the mean  

The SUBIT‑address places any stream in morphological space.

## Entropy (E)
A normalized measure of randomness in the 64‑state distribution. High entropy indicates noise‑like structure; low entropy indicates constrained or repetitive structure.

## Anisotropy (A)
A measure of directional structure. Computed from the eigenvalues of the covariance matrix in cube space. High anisotropy indicates elongated or polarized distributions.

## Tension (T)
A measure of radial irregularity. Defined as the ratio of radial standard deviation to frequency standard deviation. High tension indicates concentrated or uneven mass.

## Morphological space
A continuous geometric space spanned by (E, A, T). Different domains occupy characteristic regions, enabling clustering, comparison, and anomaly detection.

## Morphological signature
The combined identity of a stream’s 64‑state distribution, grid, and SUBIT‑address. It reflects structural form independent of semantics.

## Informational flow
Any sequence of bytes treated as a continuous stream for morphological analysis. Examples include text, code, DNA, numbers, and model output.

## Domain signature
A characteristic region of morphological space associated with a particular type of data. For example, DNA tends to low entropy and high anisotropy; π tends to high entropy and low anisotropy.

## Sliding window
The overlapping scan across the bitstring that generates the 6‑bit states. Each shift by one bit produces a new window.

## Frequency normalization
The process of dividing raw counts by their total to produce a probability distribution over the 64 states.

## Covariance matrix
A 3×3 matrix computed from cube coordinates weighted by frequencies. It encodes the geometric spread of the distribution and is used to compute anisotropy.

## Eigenvalues
The principal variances of the distribution in cube space. Their ratios determine directional bias.

## Radial distance
The Euclidean distance between a state’s cube coordinate and the mean vector. Used to compute tension.

## Byte‑level morphology
The structural form of a data stream as expressed through its bit patterns, independent of meaning, syntax, or semantics.

## Structural bias
A consistent pattern in the distribution caused by alphabet constraints, formatting habits, tokenization, or encoding.

## Tokenization artifact
A structural pattern introduced by model tokenization rather than human writing. Often visible in model‑generated text through anisotropy or tension.

## Anomaly
A deviation in morphological signature indicating corruption, drift, or unexpected structural change in a data stream.

## Drift
A gradual shift in a system’s morphological output over time, often used to monitor generative models or pipelines.

## Style signature
A morphological pattern characteristic of a particular author, model, or system, arising from consistent structural habits.

If you want this glossary expanded into a canonical 64‑entry version aligned with your SUBIT‑64 architecture, I can generate that next.
