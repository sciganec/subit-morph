### **SUBIT‑Lingua v3.0 — Examples**

This document provides **worked examples** of forms, words, sequences, and bitstreams in SUBIT‑Lingua v3.0.  
All examples follow the canonical notation:

- forms: `KA‑TE‑MO`  
- words: `KA‑TE‑MO – KU‑TA‑ME`  
- sequences: `KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU`  
- bits: `00 01 10`  

These examples illustrate **structure**, not semantics.

---

# **1. Forms (6‑bit units)**

A form is:

```
K V1 – T V2 – M V3
```

### **Example 1**
```
Form: KA‑TE‑MO
Bits: 00 01 10
```

Breakdown:

| Axis | Vowel | Bits |
|------|--------|--------|
| K | A | 00 |
| T | E | 01 |
| M | O | 10 |

---

### **Example 2**
```
Form: KE‑TO‑MU
Bits: 01 10 11
```

Breakdown:

| Axis | Vowel | Bits |
|------|--------|--------|
| K | E | 01 |
| T | O | 10 |
| M | U | 11 |

---

### **Example 3**
```
Form: KO‑TA‑MA
Bits: 10 00 00
```

---

# **2. Words (12‑bit form‑pairs)**

A word is:

```
Form‑1 – Form‑2
```

### **Example 1**
```
Word: KA‑TE‑MO – KU‑TA‑ME
Bits: 000110 110001
```

Breakdown:

| Part | Form | Bits |
|------|--------|--------|
| Inner | KA‑TE‑MO | 000110 |
| Outer | KU‑TA‑ME | 110001 |

---

### **Example 2**
```
Word: KE‑TO‑MU – KA‑TE‑MA
Bits: 011011 000100
```

---

### **Example 3**
```
Word: KO‑TE‑ME – KE‑TU‑MO
Bits: 100101 011110
```

---

# **3. Higher‑Order Forms (n×6 bits)**

A sequence is:

```
Form‑1 – Form‑2 – ... – Form‑n
```

### **Example 1 — 3‑form sequence**
```
Sequence:
KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU

Bits:
000110 110001 011011
```

---

### **Example 2 — 4‑form sequence**
```
Sequence:
KA‑TA‑MA – KE‑TE‑MO – KO‑TO‑MU – KU‑TU‑MA

Bits:
000000 010110 101011 111100
```

---

### **Example 3 — 6‑form sequence**
```
Sequence:
KA‑TE‑MO – KE‑TE‑ME – KO‑TE‑MU – KU‑TE‑MA – KA‑TO‑ME – KE‑TU‑MO

Bits:
000110 010101 100111 110100 001001 011110
```

---

# **4. Bitstream → Form Examples**

### **Example 1**
```
Bits: 000111
Form: KA‑TE‑MU
```

---

### **Example 2**
```
Bits: 101010
Form: KO‑TO‑MO
```

---

### **Example 3**
```
Bits: 111011
Form: KU‑TO‑MU
```

---

# **5. Bitstream → Word Examples**

### **Example 1**
```
Bits: 000110110001
Word: KA‑TE‑MO – KU‑TA‑ME
```

---

### **Example 2**
```
Bits: 011011000100
Word: KE‑TO‑MU – KA‑TE‑MA
```

---

### **Example 3**
```
Bits: 100101011110
Word: KO‑TE‑ME – KE‑TU‑MO
```

---

# **6. Bitstream → Sequence Examples**

### **Example 1**
```
Bits:
000110 110001 011011

Sequence:
KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU
```

---

### **Example 2**
```
Bits:
000000 010110 101011 111100

Sequence:
KA‑TA‑MA – KE‑TE‑MO – KO‑TO‑MU – KU‑TU‑MA
```

---

### **Example 3**
```
Bits:
000110 010101 100111 110100 001001 011110

Sequence:
KA‑TE‑MO – KE‑TE‑ME – KO‑TE‑MU – KU‑TE‑MA – KA‑TO‑ME – KE‑TU‑MO
```

---

# **7. Structural Patterns**

### **Axis sweep (K‑axis)**
```
KA‑TA‑MA
KE‑TA‑MA
KO‑TA‑MA
KU‑TA‑MA
```

### **Vowel sweep (M‑axis)**
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

---

# **8. Summary**

This file demonstrates:

- how forms map to 6‑bit units  
- how words map to 12‑bit transitions  
- how sequences map to n×6‑bit streams  
- how to read and write SUBIT‑Lingua structures  
- how to visualize structural patterns  

These examples are **structural**, not semantic.  
They illustrate the **geometry** of SUBIT‑Lingua.

---
