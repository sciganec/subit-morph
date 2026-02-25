### **SUBIT‑Lingua v3.0 — Notation Standard**

This document defines the **official notation rules** for writing forms, words, higher‑order structures, and bit sequences in SUBIT‑Lingua v3.0.

The notation is:

- minimal  
- regular  
- unambiguous  
- machine‑readable  
- human‑readable  
- fully aligned with the phonology and bit‑mapping system  

All SUBIT‑Lingua artifacts must follow these rules.

---

# **1. Form Notation (6‑bit units)**

A form is written as:

```
K V1 – T V2 – M V3
```

Where:

- **K / T / M** are fixed consonants (axes)  
- **V1 / V2 / V3** are vowels (A/E/O/U)  
- hyphens separate syllables  
- uppercase letters are mandatory  

Examples:

```
KA‑TA‑MA
KE‑TE‑MO
KO‑TU‑MU
```

There are **no alternative spellings**.

---

# **2. Word Notation (12‑bit form‑pairs)**

A word is a **pair of forms**, written with an en‑dash (–) between them:

```
Form‑1 – Form‑2
```

Examples:

```
KA‑TE‑MO – KU‑TA‑ME
KE‑TO‑MA – KA‑TU‑MO
KO‑TE‑MU – KE‑TE‑MA
```

Rules:

- forms must remain intact  
- the separator must be an **en‑dash (–)**, not a hyphen  
- no spaces inside forms  
- one space on each side of the en‑dash is recommended for readability  

---

# **3. Higher‑Order Form Notation (n × 6 bits)**

Higher‑order forms are sequences of forms:

```
Form‑1 – Form‑2 – Form‑3 – ... – Form‑n
```

Examples:

**Third‑order form (18 bits):**

```
KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU
```

**Fourth‑order form (24 bits):**

```
KA‑TA‑MA – KE‑TE‑MO – KO‑TO‑MU – KU‑TU‑MA
```

Rules:

- always use en‑dashes between forms  
- no commas  
- no parentheses  
- no alternative separators  

---

# **4. Bitstring Notation**

Bitstrings are written as:

- groups of **2 bits per vowel**  
- grouped by form  
- separated by spaces for readability  

Example (single form):

```
00 01 10
```

Example (word = 12 bits):

```
00 01 10   11 00 01
```

Example (form‑3 = 18 bits):

```
00 01 10   11 00 01   01 10 11
```

Rules:

- no punctuation inside bit groups  
- no leading or trailing zeros removed  
- spacing is optional but recommended  

---

# **5. Axis Notation**

Axes are always written as:

- **K** for internal axis  
- **T** for structural axis  
- **M** for process axis  

They must appear in this order:

```
K – T – M
```

Axes are **never** reordered, omitted, or replaced.

---

# **6. Vowel Notation**

Vowels must be uppercase:

- **A**  
- **E**  
- **O**  
- **U**

Each vowel corresponds to a 2‑bit state:

```
A = 00
E = 01
O = 10
U = 11
```

There are no diphthongs, accents, or lowercase variants.

---

# **7. Hyphens vs. Dashes**

SUBIT‑Lingua uses two different separators:

| Symbol | Name | Usage |
|--------|--------|--------|
| **-** | hyphen | inside forms (between syllables) |
| **–** | en‑dash | between forms (form‑pairs, sequences) |

Examples:

```
KA‑TE‑MO – KU‑TA‑ME
```

This distinction is **mandatory**.

---

# **8. File Naming Conventions**

Files referencing forms or words must use:

- lowercase  
- hyphens  
- no spaces  

Examples:

```
forms-v3.md
word-construction.md
orders-of-form.md
forms-64.csv
lexicon-4096.json
```

---

# **9. Examples**

### **Form**

```
KE‑TO‑MU
```

### **Word**

```
KA‑TE‑MO – KU‑TA‑ME
```

### **Form‑3**

```
KA‑TA‑MA – KE‑TE‑MO – KO‑TU‑MU
```

### **Bitstring**

```
00 01 10   11 00 01   01 11 10
```

---

# **10. Summary**

SUBIT‑Lingua notation is:

- **CV‑CV‑CV** for forms  
- **form – form** for words  
- **form – form – form** for higher‑order structures  
- **bit‑groups** for binary representation  
- **hyphens inside forms**  
- **en‑dashes between forms**  
- **uppercase letters only**  

This notation ensures clarity, regularity, and universal readability across all SUBIT‑Lingua artifacts.

---
