### **SUBIT‑Lingua v3.0 — Orders of Form (n×6‑bit Structures)**

SUBIT‑Lingua is built from a single atomic unit: the **form**.  
A form is a 6‑bit structural configuration defined by:

```
K V1 – T V2 – M V3
```

Higher‑order expressions are created by **concatenating forms**.  
This document defines the rules for constructing:

- **first‑order forms** (6 bits)  
- **second‑order forms** (12‑bit words)  
- **third‑order forms** (18 bits)  
- **n‑th order forms** (n × 6 bits)

SUBIT‑Lingua is fully regular:  
every higher‑order structure is a linear sequence of forms.

---

# **1. First‑Order Forms (6 bits)**

A first‑order form is the atomic unit of SUBIT‑Lingua.

```
K V1 – T V2 – M V3
```

- 3 axes (K/T/M)  
- 3 vowels (V1/V2/V3)  
- each vowel encodes 2 bits  
- total = **6 bits**

There are **64** possible first‑order forms.

---

# **2. Second‑Order Forms (12 bits)**  
### **Words = Form‑Pairs**

A second‑order form is a **pair of first‑order forms**:

```
Form‑1 + Form‑2
```

Written as:

```
K V1 – T V2 – M V3  –  K V4 – T V5 – M V6
```

Bit structure:

```
V1 V2 V3   V4 V5 V6
```

Total:

- 6 bits (inner form)  
- 6 bits (outer form)  
- **12 bits**

There are **4096** possible second‑order forms.

These are the **words** of SUBIT‑Lingua.

---

# **3. Third‑Order Forms (18 bits)**  
### **Sequences of Three Forms**

A third‑order form is:

```
Form‑1 + Form‑2 + Form‑3
```

Bit structure:

```
V1 V2 V3   V4 V5 V6   V7 V8 V9
```

Total:

- 3 forms  
- **18 bits**

Interpretation:

- multi‑step transition  
- structural sequence  
- micro → meso → macro  
- three‑layer configuration

Third‑order forms are used for:

- processes  
- flows  
- composite states  
- multi‑stage mappings

---

# **4. Fourth‑Order Forms (24 bits)**  
### **Composite Structures**

A fourth‑order form is:

```
Form‑1 + Form‑2 + Form‑3 + Form‑4
```

Bit structure:

```
24 bits = 4 × 6 bits
```

Interpretation:

- extended processes  
- structural chains  
- multi‑layer composites  
- higher‑order mappings

---

# **5. N‑th Order Forms (n × 6 bits)**  
### **General Case**

An n‑th order form is defined as:

```
Form‑1 + Form‑2 + ... + Form‑n
```

Bit structure:

```
n × 6 bits
```

This is the general mechanism for building:

- sentences  
- structural programs  
- process flows  
- multi‑stage transformations  
- hierarchical configurations  

SUBIT‑Lingua does not impose a maximum order.

---

# **6. Interpretation of Higher‑Order Forms**

Higher‑order forms represent:

### **1. Sequences**
A → B → C → D  
(stepwise transitions)

### **2. Composites**
A + B + C  
(simultaneous structural layers)

### **3. Processes**
A evolves into B evolves into C  
(dynamic flows)

### **4. Mappings**
A maps to B maps to C  
multi‑stage transformations

### **5. Structural Programs**
A formal chain of structural operations.

SUBIT‑Lingua is **pre‑semantic**:  
meaning emerges from the structure of the sequence.

---

# **7. Notation**

Recommended notation:

- **form‑1**: KA‑TE‑MO  
- **form‑2**: KA‑TE‑MO – KU‑TA‑ME  
- **form‑3**: KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU  
- **form‑n**: sequence of n forms

Hyphens separate axes; en‑dashes separate forms.

---

# **8. Summary**

- All SUBIT expressions are built from **6‑bit forms**  
- A word = **form‑pair (12 bits)**  
- Higher‑order forms = **n × 6 bits**  
- The system is **fully regular, combinatorial, and scalable**  
- SUBIT‑Lingua models **structure, transitions, and processes**  

This document defines the complete mechanism for constructing higher‑order forms.

---
