### **SUBIT‑Lingua v3.0 — Structural Atlas**

The SUBIT‑Lingua Atlas is the **complete structural map** of the language:

- the 64‑form cube  
- the 4096‑word transition grid  
- higher‑order sequences  
- axes and bit‑mapping  
- diagrams and motifs  
- examples and patterns  
- structural programs  

This atlas is **pre‑semantic**: it describes *structure*, not meaning.

---

# **1. Foundations**

SUBIT‑Lingua is built on:

- **three axes**: K (internal), T (structural), M (process)  
- **four states per axis**: A, E, O, U  
- **one form template**: CV‑CV‑CV  
- **one bit‑mapping**:  
  - A = 00  
  - E = 01  
  - O = 10  
  - U = 11  

A form is **6 bits**.  
A word is **12 bits**.  
A sequence is **n×6 bits**.

---

# **2. The 64‑Form Cube**

Each form is:

```
K V1 – T V2 – M V3
```

Where each vowel ∈ {A, E, O, U}.

This yields a **4×4×4 cube**:

```
K-axis: A E O U
T-axis: A E O U
M-axis: A E O U
```

Example slice (K = A):

```
+-------------------------------+
| KA-TA-MA | KA-TE-MA | KA-TO-MA | KA-TU-MA |
| KA-TA-ME | KA-TE-ME | KA-TO-ME | KA-TU-ME |
| KA-TA-MO | KA-TE-MO | KA-TO-MO | KA-TU-MO |
| KA-TA-MU | KA-TE-MU | KA-TO-MU | KA-TU-MU |
+-------------------------------+
```

---

# **3. Bit‑Mapping**

Each vowel encodes 2 bits:

| Vowel | Bits |
|-------|-------|
| A | 00 |
| E | 01 |
| O | 10 |
| U | 11 |

A form’s bit layout:

```
[ K-bits ][ T-bits ][ M-bits ]
```

Example:

```
KA‑TE‑MO → 00 01 10 → 000110
```

---

# **4. The 4096‑Word Grid**

A word is:

```
Form‑1 – Form‑2
```

Bit layout:

```
[ 6 bits inner ][ 6 bits outer ]
```

The full word‑space is a **64×64 grid**:

```
           Outer Form (0–63)
        +----------------------------------+
Inner   | F00 F01 F02 ... F63              |
Form    | F00                               |
(0–63)  | F01                               |
        | ...                               |
        | F63                               |
        +----------------------------------+
```

Each cell is a **12‑bit transition**.

---

# **5. Higher‑Order Sequences**

A sequence is:

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

Sequences represent **paths** through the cube.

---

# **6. Structural Diagrams**

### **Axes**

```
          M-axis
             ^
             |
             |
             +--------> T-axis
            /
           /
          v
      K-axis
```

---

### **Local Neighborhood (Hamming‑1)**

```
          KA-TE-MU
             |
KA-TE-MA -- KA-TE-MO -- KA-TE-ME
             |
          KA-TO-MO
```

---

### **Primary Diagonal**

```
KA‑TA‑MA → KE‑TE‑ME → KO‑TO‑MO → KU‑TU‑MU
```

---

### **Cycle**

```
KA‑TE‑MO → KE‑TE‑MO → KE‑TE‑ME → KA‑TE‑ME → KA‑TE‑MO
```

---

### **Sequence**

```
KA‑TE‑MO → KU‑TA‑ME → KE‑TO‑MU → KO‑TU‑MA
```

---

# **7. Motifs**

Motifs are recurring structural patterns.

### **Axis Sweeps**
- K‑axis: KA‑TE‑MO → KE‑TE‑MO → KO‑TE‑MO → KU‑TE‑MO  
- T‑axis: KA‑TA‑MO → KA‑TE‑MO → KA‑TO‑MO → KA‑TU‑MO  
- M‑axis: KA‑TE‑MA → KA‑TE‑ME → KA‑TE‑MO → KA‑TE‑MU  

---

### **Diagonals**
- Primary: KA‑TA‑MA → KE‑TE‑ME → KO‑TO‑MO → KU‑TU‑MU  
- Mixed: KA‑TE‑MO → KE‑TO‑MU → KO‑TU‑ME → KU‑TA‑MO  

---

### **Cycles**
- 4‑cycle  
- 8‑cycle (2×2×2 subcube)  
- axis‑alternating cycles  

---

### **Programs**
- linear  
- branching  
- converging  
- spirals  
- zig‑zags  

---

# **8. Examples**

### **Forms**
```
KA‑TE‑MO → 000110
KE‑TO‑MU → 011011
KO‑TA‑MA → 100000
```

### **Words**
```
KA‑TE‑MO – KU‑TA‑ME → 000110110001
KE‑TO‑MU – KA‑TE‑MA → 011011000100
```

### **Sequences**
```
KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU
000110 110001 011011
```

---

# **9. Atlas Tables**

### **Form Table (64 entries)**  
(Provided in `forms-64.csv` and `forms-64.json`.)

### **Word Table (4096 entries)**  
(Provided in `lexicon-4096.json`.)

---

# **10. Tools**

The atlas is supported by:

- `encoder.py` — form/word/sequence → bits  
- `decoder.py` — bits → form/word/sequence  
- `parser.py` — parse SUBIT‑Lingua notation  
- `generator.py` — generate forms + lexicon  
- `playground.ipynb` — interactive environment  

All tools are **deterministic** and **dependency‑free**.

---

# **11. Summary**

The SUBIT‑Lingua Atlas provides:

- the full geometry of the 64‑form cube  
- the 4096‑word transition grid  
- higher‑order sequences  
- structural diagrams  
- canonical motifs  
- examples and patterns  
- complete toolchain  

It is the **master reference** for SUBIT‑Lingua v3.0.

---

