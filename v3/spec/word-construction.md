### **SUBIT‑Lingua v3.0 — Word Construction (12‑bit Form‑Pairs)**

SUBIT‑Lingua constructs words by combining **two 6‑bit forms** into a single **12‑bit structure**.  
A word is not a “meaningful token” in the natural‑language sense.  
It is a **structural transition** between two states in the SUBIT form‑space.

A SUBIT word is defined as:

```
Form‑1 (inner) + Form‑2 (outer)
```

This yields:

- **6 bits** from the inner form  
- **6 bits** from the outer form  
- **12 bits total**

The full word‑space contains:

```
64 × 64 = 4096 words
```

---

# **1. Form Structure (6 bits)**

Each form is defined as:

```
K V1 – T V2 – M V3
```

Where:

- **K / T / M** are fixed axes  
- **V1 / V2 / V3** are vowels encoding 2‑bit states  
- **A / E / O / U** map to **00 / 01 / 10 / 11**

Thus each form = **6 bits**.

---

# **2. Word Structure (12 bits)**

A word is written as:

```
K V1 – T V2 – M V3  –  K V4 – T V5 – M V6
```

Where:

- **V1 V2 V3** = inner form (6 bits)  
- **V4 V5 V6** = outer form (6 bits)

The combined bitstring is:

```
V1 V2 V3 V4 V5 V6
```

Example:

```
KA‑TE‑MO – KU‑TA‑ME
```

Vowels → bits:

- A = 00  
- E = 01  
- O = 10  
- U = 11  

Binary:

```
00 01 10   11 00 01
```

This is a complete 12‑bit SUBIT word.

---

# **3. Inner and Outer Forms**

### **Inner Form (micro‑configuration)**  
Represents:

- internal state  
- source configuration  
- micro‑structure  
- the “starting point” of the transition  

### **Outer Form (macro‑configuration)**  
Represents:

- external state  
- contextual configuration  
- macro‑structure  
- the “resulting point” of the transition  

A word is therefore a **mapping**:

```
inner form → outer form
```

This is the fundamental semantic mechanism of SUBIT‑Lingua.

---

# **4. Word Space (4096 Units)**

The full SUBIT lexicon is a **64×64 grid**:

- rows = inner forms  
- columns = outer forms  

Each cell corresponds to a unique 12‑bit word.

This grid is the **complete adjacency matrix** of the SUBIT form‑space.

---

# **5. Reading a Word**

To read a SUBIT word:

1. Split it into two forms  
2. Decode each form’s vowels into bits  
3. Interpret the inner form as the micro‑state  
4. Interpret the outer form as the macro‑state  
5. Understand the word as the **transition** between them

Example:

```
KE‑TE‑MA – KA‑TU‑ME
```

- inner: structural form  
- outer: internal signal  
- meaning: “a structural configuration expressing itself as an internal signal”

SUBIT‑Lingua is **pre‑semantic**; meaning emerges from structure.

---

# **6. Higher‑Order Words**

Words can be chained to form higher‑order structures:

- **form‑3** = 18 bits  
- **form‑4** = 24 bits  
- **form‑n** = n × 6 bits  

These represent:

- processes  
- sequences  
- multi‑layer transitions  
- structural flows  

Higher‑order forms follow the same rules as first‑order forms.

---

# **7. Summary**

- A SUBIT word = **two 6‑bit forms**  
- Total = **12 bits**  
- Word‑space = **4096 transitions**  
- Words represent **structural mappings**, not semantic tokens  
- All higher‑order expressions are built from form‑pairs  

SUBIT‑Lingua is a **formal, structural, combinatorial language**.

---
