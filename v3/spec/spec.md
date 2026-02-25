### **SUBIT‑Lingua v3.0 — Formal Specification**

SUBIT‑Lingua is a **minimal, regular, bit‑driven structural language**.  
It encodes configurations, transitions, and processes using:

- three fixed axes (K, T, M)  
- four vowel‑states (A, E, O, U)  
- a strict CV‑CV‑CV form template  
- a universal 2‑bit vowel mapping  
- 6‑bit atomic forms  
- 12‑bit words (form‑pairs)  
- n×6‑bit higher‑order sequences  

This document defines the **complete SUBIT‑Lingua v3.0 standard**.

---

# **1. Alphabet**

SUBIT‑Lingua uses a fixed, closed alphabet.

## **1.1 Consonants (Axes)**

| Axis | Symbol | Role |
|------|--------|------|
| Internal | **K** | identity, interiority |
| Structural | **T** | orientation, spatial configuration |
| Process | **M** | change, temporal configuration |

These consonants **never vary** and **never encode bits**.

---

## **1.2 Vowels (States)**

| Vowel | Bits |
|--------|--------|
| **A** | 00 |
| **E** | 01 |
| **O** | 10 |
| **U** | 11 |

Vowels encode **2‑bit states** and are the only bit‑bearing elements.

---

# **2. Form Structure**

A form is a **three‑syllable CV‑CV‑CV structure**:

```
K V1 – T V2 – M V3
```

Where:

- V1, V2, V3 ∈ {A, E, O, U}  
- hyphens separate syllables  
- consonants are fixed and ordered: K → T → M  

Example:

```
KA‑TE‑MO
```

---

# **3. Form Encoding (6 bits)**

Each vowel contributes 2 bits:

```
Form bits = V1_bits V2_bits V3_bits
```

Example:

```
KA‑TE‑MO
A = 00
E = 01
O = 10

Bits = 000110
```

There are **64 possible forms**.

---

# **4. Form Decoding**

Given a 6‑bit string:

1. Split into 3 groups of 2 bits  
2. Convert each to a vowel  
3. Insert vowels into K‑T‑M template  

Example:

```
011011 → KE‑TO‑MU
```

---

# **5. Words (12‑bit transitions)**

A word is a **pair of forms**:

```
Form‑1 – Form‑2
```

Bit layout:

```
[ 6 bits inner ][ 6 bits outer ]
```

Example:

```
KA‑TE‑MO – KU‑TA‑ME
000110 110001
```

There are **4096 possible words**.

---

# **6. Word Decoding**

Given a 12‑bit string:

- first 6 bits → inner form  
- last 6 bits → outer form  

Example:

```
000110110001 → KA‑TE‑MO – KU‑TA‑ME
```

---

# **7. Higher‑Order Forms (n×6 bits)**

A higher‑order form is a **sequence of forms**:

```
Form‑1 – Form‑2 – ... – Form‑n
```

Bitstream:

```
n × 6 bits
```

Example:

```
KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU
000110 110001 011011
```

Sequences represent **paths** through the form‑space.

---

# **8. Notation Rules**

SUBIT‑Lingua uses strict notation:

- **Hyphens** separate syllables: `KA‑TE‑MO`  
- **En‑dashes** separate forms: `KA‑TE‑MO – KU‑TA‑ME`  
- **No spaces** inside forms  
- **Single spaces** around en‑dash  
- **Uppercase only**  
- **No alternative spellings**  

Bitstreams:

- may be grouped (`000110 110001`)  
- or ungrouped (`000110110001`)  
- must contain only `0` and `1`  

---

# **9. Structural Geometry**

## **9.1 Form‑Space**

The 64 forms occupy a **4×4×4 cube**:

- K‑axis: A/E/O/U  
- T‑axis: A/E/O/U  
- M‑axis: A/E/O/U  

Each form is a coordinate:

```
(K_state, T_state, M_state)
```

---

## **9.2 Word‑Space**

Words form a **64×64 grid**:

- rows = inner forms  
- columns = outer forms  

Each cell is a **12‑bit transition**.

---

## **9.3 Sequence‑Space**

Sequences are **paths** through the cube:

- linear  
- branching  
- cyclic  
- diagonal  
- spiral  
- zig‑zag  

All are valid.

---

# **10. Validity Conditions**

A SUBIT‑Lingua expression is valid if:

### **Forms**
- matches `K[AEOU]-T[AEOU]-M[AEOU]`  
- encodes to exactly 6 bits  

### **Words**
- matches `Form – Form`  
- encodes to exactly 12 bits  

### **Sequences**
- list of valid forms  
- encodes to n×6 bits  

### **Bitstreams**
- 6 bits → form  
- 12 bits → word  
- n×6 bits → sequence  

No other lengths are valid.

---

# **11. Canonical Operations**

SUBIT‑Lingua defines four core operations:

## **11.1 Encode**
```
form → 6 bits
word → 12 bits
sequence → n×6 bits
```

## **11.2 Decode**
```
6 bits → form
12 bits → word
n×6 bits → sequence
```

## **11.3 Parse**
```
notation → structured object
```

## **11.4 Generate**
```
produce full form table and lexicon
```

All operations are **deterministic**.

---

# **12. Motifs (Structural Patterns)**

SUBIT‑Lingua motifs include:

- axis sweeps  
- diagonals  
- cycles  
- spirals  
- zig‑zags  
- Hamming spheres  
- lattice paths  
- higher‑order programs  

These motifs describe **geometry**, not semantics.

(See `motifs.md` and `motifs-visual.md`.)

---

# **13. Tools (Reference)**

The official toolchain:

- `encoder.py` — encode forms/words/sequences  
- `decoder.py` — decode bitstreams  
- `parser.py` — parse notation  
- `generator.py` — generate forms + lexicon  
- `playground.ipynb` — interactive environment  

All tools are:

- single‑file  
- dependency‑free  
- canonical  

---

# **14. Summary**

SUBIT‑Lingua v3.0 is a:

- **minimal**  
- **regular**  
- **bit‑driven**  
- **structural**  
- **combinatorial**  
- **universal**  

language for representing configurations, transitions, and processes.

This specification defines the **complete standard**.

---

