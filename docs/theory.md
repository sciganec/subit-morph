# Theory

## Morphology as Form

SUBIT‑morph treats information as a geometric object. A byte stream is not interpreted for meaning; instead, its structural form is extracted through a uniform, domain‑agnostic procedure. The resulting morphology reflects how information is shaped at the bit level, revealing patterns that persist across semantics, domains, and encodings.

The central premise is that every informational flow has a *shape*—a distributional and geometric signature—arising from the way its bits are arranged. This shape can be measured, compared, and visualized.

---

## 6‑Bit Windows as Atoms of Form

The 6‑bit sliding window is the fundamental atom of SUBIT‑morph. It provides:

- 64 possible states  
- enough resolution to capture local structure  
- enough compression to reveal global patterns  
- invariance to semantic content  

The choice of 6 bits balances granularity and tractability. Smaller windows lose structure; larger windows dilute local patterns. Six bits produce a stable, expressive morphological signature across domains.

---

## 64‑State Distribution

Scanning a bitstring with overlapping 6‑bit windows yields a frequency distribution over 64 states. This distribution is the raw morphological fingerprint of the stream.

Properties:

- sensitive to repetition and periodicity  
- responsive to alphabet size and encoding  
- stable under semantic variation  
- domain‑agnostic  

The distribution is the substrate from which all higher‑level metrics are derived.

---

## 8×8 Grid as Spatial Projection

Arranging the 64 frequencies into an 8×8 grid provides a spatial visualization of morphological density. This grid is not arbitrary: it preserves adjacency relationships in the 6‑bit state space and reveals:

- clusters  
- gradients  
- voids  
- symmetry or asymmetry  

The grid is a 2D projection of the deeper 3D structure encoded in the 4×4×4 cube.

---

## 4×4×4 Cube Coordinates

Each 6‑bit state maps naturally to a coordinate in a 4×4×4 cube:

- the top two bits → x  
- the middle two bits → y  
- the bottom two bits → z  

This embedding transforms the distribution into a geometric object. The cube provides a continuous space in which:

- mean vectors  
- covariance matrices  
- radial distances  

can be computed. These geometric quantities form the basis of the SUBIT‑address.

---

## The SUBIT‑Address

The SUBIT‑address is a three‑component coordinate:

```
(E, A, T)
```

It summarizes the morphology of a stream in terms of:

### Entropy (E)
Measures randomness or uniformity.  
High entropy → noise‑like structure.  
Low entropy → constrained or repetitive structure.

### Anisotropy (A)
Measures directional bias in the cube.  
High anisotropy → elongated or polarized distribution.  
Low anisotropy → isotropic or uniform distribution.

### Tension (T)
Measures radial variation.  
High tension → mass concentrated at specific radii.  
Low tension → smooth radial distribution.

Together, these coordinates position any informational flow in morphological space.

---

## Morphological Space

Morphological space is the geometric domain spanned by (E, A, T). It is continuous, bounded, and domain‑agnostic. Streams that differ semantically may cluster together morphologically; streams that are semantically similar may diverge morphologically due to encoding or stylistic differences.

This space reveals:

- clusters  
- boundaries  
- gradients  
- attractors  

It provides a universal coordinate system for informational form.

---

## Domain Signatures

Different domains occupy characteristic regions:

- numerical constants → high entropy, low anisotropy  
- DNA → low entropy, high anisotropy  
- source code → medium entropy, high tension  
- natural language → medium‑high entropy, moderate anisotropy  
- model output → similar to natural language but with distinct anisotropy patterns  

These signatures are stable across samples and lengths.

---

## Interpretability

SUBIT‑morph provides an interpretability layer that is:

- content‑agnostic  
- model‑agnostic  
- encoding‑agnostic  

It reveals structural properties invisible to semantic analysis:

- repetition  
- formatting artifacts  
- tokenization biases  
- distributional irregularities  

This makes it useful for:

- model analysis  
- anomaly detection  
- authorship and style studies  
- cross‑domain comparison  

Morphology exposes the shape of information before meaning.

---

## Universality

The SUBIT‑morph framework is universal because:

- every byte stream can be processed  
- the algorithm is deterministic  
- the metrics are geometric  
- the representation is compact  
- the space is continuous  

This universality allows diverse data types to be compared on equal footing.

---

## Summary

SUBIT‑morph defines a complete theory of informational form:

- 6‑bit windows capture local structure  
- 64‑state distributions encode global patterns  
- the 4×4×4 cube provides geometric grounding  
- entropy, anisotropy, and tension summarize morphology  
- morphological space enables comparison across domains  

The theory unifies disparate informational flows under a single geometric framework, revealing the deep structure of data independent of meaning.
