### **SUBIT‑Lingua v3.0 — Bit Mapping (A/E/O/U → 2‑bit States)**

SUBIT‑Lingua is a **bit‑driven structural language**.  
All structural information is encoded through **vowels**, each of which corresponds to a 2‑bit state.

Consonants (K/T/M) define the axes of the form.  
Vowels (A/E/O/U) define the **bit pattern** of the form.

This document specifies the complete bit‑mapping system.

---

# **1. Vowel → Bit Mapping**

SUBIT‑Lingua uses exactly **four vowels**, each encoding a 2‑bit value:

| Vowel | Bits | Structural Interpretation |
|--------|--------|---------------------------|
| **A** | 00 | identity, stability |
| **E** | 01 | orientation, direction |
| **O** | 10 | variation, depth |
| **U** | 11 | emergence, transition |

This mapping is **fixed and universal** across all forms and all orders.

---

# **2. Form Bit Structure (6 bits)**

A form is defined as:

```
K V1 – T V2 – M V3
```

Each vowel contributes **2 bits**:

- V1 = 2 bits  
- V2 = 2 bits  
- V3 = 2 bits  

Total:

```
2 + 2 + 2 = 6 bits
```

Thus each form corresponds to a unique 6‑bit address.

Example:

```
KA‑TE‑MO
```

Vowels:

- A = 00  
- E = 01  
- O = 10  

Bits:

```
00 01 10
```

---

# **3. Word Bit Structure (12 bits)**  
### **Form‑Pair = 12‑bit Word**

A SUBIT word is a **pair of forms**:

```
Form‑1 (inner) + Form‑2 (outer)
```

Bit structure:

```
V1 V2 V3   V4 V5 V6
```

Total:

```
6 bits + 6 bits = 12 bits
```

Example:

```
KA‑TE‑MO – KU‑TA‑ME
```

Vowels:

- A = 00  
- E = 01  
- O = 10  
- U = 11  

Bits:

```
00 01 10   11 00 01
```

This is a complete 12‑bit SUBIT word.

---

# **4. Higher‑Order Bit Structure (n × 6 bits)**

Higher‑order forms are linear concatenations of 6‑bit units:

- **form‑3** = 18 bits  
- **form‑4** = 24 bits  
- **form‑n** = n × 6 bits  

General structure:

```
Form‑1 | Form‑2 | Form‑3 | ... | Form‑n
```

Each form contributes **6 bits**, derived from its vowels.

---

# **5. Bit Ordering**

SUBIT‑Lingua uses **left‑to‑right bit ordering**:

- V1 bits come first  
- V2 bits follow  
- V3 bits follow  
- next form begins immediately after  

Example (form‑3):

```
V1 V2 V3   V4 V5 V6   V7 V8 V9
```

There is **no padding**, **no separators**, and **no metadata** in the bitstream.

---

# **6. Bitspace Completeness**

The bit‑mapping system ensures:

- **64 possible 6‑bit forms**  
- **4096 possible 12‑bit words**  
- **complete coverage** of the structural space  
- **no unused bit patterns**  
- **no ambiguous encodings**  

SUBIT‑Lingua is a **closed, finite, combinatorial system**.

---

# **7. Rationale for the Bit System**

The bit‑mapping is designed to be:

### **Minimal**
Only 2 bits per vowel, 6 bits per form.

### **Regular**
No exceptions, no irregular forms.

### **Composable**
Higher‑order forms scale linearly.

### **Deterministic**
Every bitstring corresponds to exactly one form sequence.

### **Universal**
Bit patterns are independent of culture, semantics, or natural language.

---

# **8. Summary**

- SUBIT‑Lingua encodes structure through **vowel‑based bit mapping**  
- A/E/O/U = **00/01/10/11**  
- A form = **6 bits**  
- A word = **12 bits**  
- Higher‑order forms = **n × 6 bits**  
- The bit system is **complete, regular, and deterministic**

This document defines the complete bit‑mapping foundation of SUBIT‑Lingua v3.0.

---
