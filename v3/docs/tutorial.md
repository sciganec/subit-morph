### **SUBIT‑Lingua v3.0 — Tutorial**

This tutorial introduces SUBIT‑Lingua step‑by‑step, from the smallest unit (a vowel) to full higher‑order structures.  
It assumes no prior knowledge and focuses on **doing**, not theory.

---

# **1. The Smallest Unit: Vowels → Bits**

SUBIT‑Lingua uses four vowels.  
Each vowel encodes **2 bits**:

| Vowel | Bits |
|-------|-------|
| A | 00 |
| E | 01 |
| O | 10 |
| U | 11 |

**Try it:**

- A → `00`  
- O → `10`  
- U → `11`  

This is the foundation of the entire system.

---

# **2. The Form Template (CV‑CV‑CV)**

Every form has the same structure:

```
K V1 – T V2 – M V3
```

Where:

- **K**, **T**, **M** are fixed consonants (axes)  
- **V1**, **V2**, **V3** are vowels (A/E/O/U)  

Example:

```
KA‑TE‑MO
```

Breakdown:

- K + A  
- T + E  
- M + O  

---

# **3. Encoding a Form (6 bits)**

To encode a form:

1. Extract the vowels  
2. Convert each vowel to its 2‑bit value  
3. Concatenate the bits  

### **Example**

Form:

```
KA‑TE‑MO
```

Vowels:

```
A, E, O
```

Bits:

```
A = 00
E = 01
O = 10
```

Final:

```
000110
```

---

# **4. Decoding a Form (bits → form)**

To decode:

1. Split the 6 bits into 3 groups of 2  
2. Convert each pair to a vowel  
3. Insert vowels into K‑T‑M template  

### **Example**

Bits:

```
011011
```

Split:

```
01 10 11
```

Vowels:

```
E O U
```

Form:

```
KE‑TO‑MU
```

---

# **5. Words (12‑bit form‑pairs)**

A word is:

```
Form‑1 – Form‑2
```

Example:

```
KA‑TE‑MO – KU‑TA‑ME
```

Encoding:

```
KA‑TE‑MO = 000110
KU‑TA‑ME = 110001
```

Word bits:

```
000110110001
```

Decoding works the same way:

- first 6 bits → inner form  
- last 6 bits → outer form  

---

# **6. Higher‑Order Forms (n×6 bits)**

A sequence is:

```
Form‑1 – Form‑2 – Form‑3 – ... – Form‑n
```

Example:

```
KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU
```

Bits:

```
000110 110001 011011
```

There is no upper limit on sequence length.

---

# **7. Practice: Encode These Forms**

Try encoding:

1. `KA‑TA‑MA`  
2. `KE‑TE‑MO`  
3. `KO‑TU‑MU`  
4. `KU‑TO‑ME`  

**Answers:**

```
KA‑TA‑MA → 000000
KE‑TE‑MO → 010110
KO‑TU‑MU → 101111
KU‑TO‑ME → 111001
```

---

# **8. Practice: Decode These Bitstrings**

Decode:

1. `001001`  
2. `100111`  
3. `011100`  

**Answers:**

```
001001 → KA‑TO‑ME
100111 → KO‑TE‑MU
011100 → KE‑TU‑MA
```

---

# **9. Practice: Encode These Words**

Encode:

1. `KA‑TE‑MO – KU‑TA‑ME`  
2. `KE‑TO‑MU – KA‑TE‑MA`  

**Answers:**

```
KA‑TE‑MO – KU‑TA‑ME → 000110110001
KE‑TO‑MU – KA‑TE‑MA → 011011000100
```

---

# **10. Structural Patterns to Explore**

### **Axis sweep**
```
KA‑TA‑MA
KE‑TA‑MA
KO‑TA‑MA
KU‑TA‑MA
```

### **Vowel sweep**
```
KA‑TE‑MA
KA‑TE‑ME
KA‑TE‑MO
KA‑TE‑MU
```

### **Diagonal sweep**
```
KA‑TA‑MA
KE‑TE‑ME
KO‑TO‑MO
KU‑TU‑MU
```

These patterns reveal the geometry of the form‑space.

---

# **11. Using the Tools**

The repository includes:

- `encoder.py` — encode forms, words, sequences  
- `decoder.py` — decode bitstreams  
- `parser.py` — parse SUBIT‑Lingua notation  
- `generator.py` — generate full form and lexicon tables  
- `playground.ipynb` — interactive environment  

Try:

```python
encode("KA‑TE‑MO")
decode("000110")
encode("KA‑TE‑MO – KU‑TA‑ME")
decode("000110110001")
```

---

# **12. Summary**

This tutorial taught you how to:

- read and write SUBIT‑Lingua forms  
- encode and decode bitstreams  
- construct words and sequences  
- explore structural patterns  
- use the tools in the repository  

SUBIT‑Lingua is a **structural language**, not a semantic one.  
It represents **configurations and transitions** in a minimal, universal, bit‑driven form.

---

