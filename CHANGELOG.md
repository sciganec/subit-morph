# CHANGELOG

## 1.0.0 — Initial Canonical Release

### Added
- Complete reference implementation of the SUBIT‑morph pipeline  
  - 6‑bit sliding window scanner  
  - 64‑state distribution  
  - 8×8 grid projection  
  - 4×4×4 cube embedding  
  - Entropy, anisotropy, and tension metrics  
- Core modules:  
  - `subit.py` — full pipeline  
  - `metrics.py` — E/A/T computations  
  - `grid.py` — grid construction and formatting  
  - `utils.py` — byte I/O and helpers  
- Pseudocode specification (`subit-algorithm.txt`)  
- Conceptual documentation:  
  - `overview.md`  
  - `theory.md`  
  - `morphological-space.md`  
  - `applications.md`  
  - `interpretability-notes.md`  
  - `glossary.md`  
- Domain examples and reference morphs:  
  - natural language  
  - model‑generated text  
  - π digits  
  - DNA sequence  
  - source code  
- Comparative tables and summaries  
- Repository roadmap

### Status
This release establishes the canonical, minimal, and complete foundation of the SUBIT‑morph system, suitable for research, analysis, and integration.
