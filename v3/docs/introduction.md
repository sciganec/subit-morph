### **SUBIT‑Lingua v3.0 — Introduction**

SUBIT‑Lingua is a **formal, structural, bit‑driven language** built on a minimal and universal foundation.  
It encodes structure using:

- **three fixed axes** (K, T, M)  
- **four vowel‑states** (A, E, O, U)  
- **strict CV‑CV‑CV forms**  
- **6‑bit atomic units**  
- **12‑bit words** (form‑pairs)  
- **n×6‑bit higher‑order sequences**

SUBIT‑Lingua is not a natural language and not a semantic system.  
It is a **structural calculus**: a way to represent transitions, configurations, and processes in a closed, finite, combinatorial space.

---

# **1. Purpose**

SUBIT‑Lingua provides:

- a **universal structural vocabulary**  
- a **bit‑exact representation** of forms and transitions  
- a **regular, deterministic grammar**  
- a **finite, complete lexicon** (4096 words)  
- a **scalable higher‑order syntax**  

It is designed for:

- structural modeling  
- process representation  
- agent communication  
- ontology encoding  
- symbolic reasoning  
- latent‑space alignment  

SUBIT‑Lingua is the linguistic layer of the broader SUBIT system.

---

# **2. Core Principles**

### **Minimalism**  
Only 3 consonants and 4 vowels.  
Only one syllable type (CV).  
Only one form template (K‑T‑M).

### **Regularity**  
No exceptions, no irregular forms, no alternative spellings.

### **Determinism**  
Every bitstring corresponds to exactly one form or sequence.

### **Composability**  
Higher‑order structures are linear concatenations of 6‑bit units.

### **Universality**  
No cultural, semantic, or natural‑language dependencies.

---

# **3. Forms (6 bits)**

A form is the atomic unit of SUBIT‑Lingua:

```
K V1 – T V2 – M V3
```

Where:

- **K / T / M** are fixed axes  
- **V1 / V2 / V3** ∈ {A, E, O, U}  
- each vowel encodes **2 bits**  

Total:

```
6 bits = 3 vowels × 2 bits
```

There are **64 possible forms**.

---

# **4. Words (12 bits)**

A word is a **pair of forms**:

```
Form‑1 – Form‑2
```

This yields:

- **6 bits** (inner form)  
- **6 bits** (outer form)  
- **12 bits total**

The full word‑space contains **4096 transitions**.

Words represent **structural mappings**, not semantic tokens.

---

# **5. Higher‑Order Forms (n×6 bits)**

Higher‑order expressions are sequences of forms:

```
Form‑1 – Form‑2 – ... – Form‑n
```

Bit length:

```
n × 6 bits
```

These represent:

- processes  
- flows  
- multi‑stage transitions  
- composite structures  
- structural programs  

SUBIT‑Lingua imposes no maximum order.

---

# **6. Axes (K / T / M)**

The three axes define the geometry of every form:

| Axis | Role | Domain |
|------|------|--------|
| **K** | internal | identity, source, interiority |
| **T** | structural | form, orientation, spatial configuration |
| **M** | process | dynamics, change, temporal configuration |

Axes are fixed, ordered, and non‑bit‑bearing.

---

# **7. Bit Mapping (A / E / O / U)**

Vowels encode 2‑bit states:

| Vowel | Bits |
|--------|--------|
| **A** | 00 |
| **E** | 01 |
| **O** | 10 |
| **U** | 11 |

This mapping is universal across all forms and orders.

---

# **8. Notation**

- Forms: `KA‑TE‑MO`  
- Words: `KA‑TE‑MO – KU‑TA‑ME`  
- Sequences: `KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU`  
- Bits: `00 01 10   11 00 01`  

Hyphens separate syllables; en‑dashes separate forms.

---

# **9. Files in This Repository**

- `phonology.md` — sound system  
- `axes.md` — structural axes  
- `bit-mapping.md` — vowel → bit mapping  
- `forms-64.csv` — full form table  
- `forms-64.json` — machine‑readable form table  
- `word-construction.md` — 12‑bit word structure  
- `orders-of-form.md` — higher‑order forms  
- `notation.md` — official notation rules  
- `generator.py` — form/lexicon generator  
- `parser.py` — bitstream parser  
- `encoder.py` — form/word encoder  
- `decoder.py` — bitstream decoder  
- `playground.ipynb` — interactive environment  

---

# **10. Summary**

SUBIT‑Lingua v3.0 is a:

- **minimal**  
- **regular**  
- **bit‑driven**  
- **structural**  
- **combinatorial**  
- **universal**  

language for representing forms, transitions, and processes.

It is the formal linguistic layer of the SUBIT system.

---
