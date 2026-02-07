# Overview

## Purpose

This repository provides a complete, reference‑grade implementation and documentation set for the SUBIT‑morph framework. It includes code, metrics, examples, interpretability notes, and conceptual explanations that together define the full lifecycle of computing and analyzing 64‑state morphological signatures from arbitrary byte streams.

SUBIT‑morphs treat information as form rather than meaning. Any data stream—text, code, DNA, numbers, or model output—can be converted into a 64‑state distribution, an 8×8 grid, and a three‑component SUBIT‑address (E, A, T). These representations enable comparison, clustering, and interpretability across domains.

---

## Contents

### Algorithms and Code
- **subit.py** — full reference implementation of the SUBIT‑morph algorithm  
- **metrics.py** — entropy, anisotropy, and tension computations  
- **grid.py** — 8×8 grid construction and printing utilities  
- **utils.py** — byte reading, formatting, and helper functions  
- **subit-algorithm.txt** — pseudocode specification of the full pipeline  
- **code-snippet.py** — minimal example implementation

### Data Samples
- **pi.txt** — numerical data (π digits)  
- **dna-sample.txt** — biological sequence (ASCII‑encoded DNA)  
- **natural-language.txt** — human‑written text  
- **model-output.txt** — model‑generated text

### Documentation
- **example-morphs.md** — morphological examples across domains  
- **morphological-space.md** — geometric interpretation of SUBIT‑addresses  
- **comparison-table.md** — cross‑domain morphological comparison  
- **interpretability-notes.md** — interpretability and analysis guidance  
- **artifact-claude.md** — description of the Claude artifact documenting early development

---

## Core Concepts

### 64‑State Distribution
A byte stream is converted into a bitstring and scanned with sliding 6‑bit windows. Each window maps to one of 64 states (0–63), producing a frequency distribution that captures the stream’s structural form.

### 8×8 Grid
The 64 frequencies are arranged into an 8×8 grid, providing a spatial visualization of morphological density.

### 4×4×4 Cube Coordinates
Each of the 64 states corresponds to a coordinate in a 4×4×4 cube, enabling geometric analysis.

### SUBIT‑Address (E, A, T)
A compact, three‑component summary of morphology:
- **Entropy (E)** — randomness  
- **Anisotropy (A)** — directional structure  
- **Tension (T)** — radial variation  

These coordinates place any informational flow into morphological space.

---

## Applications

- clustering and classification of data streams  
- anomaly and drift detection  
- style and authorship analysis  
- model interpretability  
- cross‑domain comparison  
- visualization of informational form  

SUBIT‑morphs provide a universal, domain‑agnostic framework for analyzing the structure of information.

---

## Status

The repository contains a complete, working implementation and a full conceptual layer. It is suitable for research, experimentation, documentation, and integration into larger systems that require byte‑level morphological analysis.
