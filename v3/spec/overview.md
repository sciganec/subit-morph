### **SUBIT‑Lingua v3.0 — Structural Overview**

SUBIT‑Lingua is a **formal structural language** based on a minimal combinatorial system of **forms**.  
It is not a semantic language, nor a symbolic system, nor a natural language.  
SUBIT‑Lingua encodes **structure itself** through a compact, regular, bit‑driven architecture.

At its core, SUBIT‑Lingua defines:

- **64 forms** (6‑bit units)  
- **4096 form‑pairs** (12‑bit words)  
- **higher‑order forms** (18‑bit, 24‑bit, n×6‑bit structures)

The system is fully regular, closed, and mathematically complete.

---

## **1. Forms (6‑bit units)**

A **form** is the atomic unit of SUBIT‑Lingua.  
Each form is defined by a triple:

```
K V1 – T V2 – M V3
```

Where:

- **K / T / M** are fixed structural axes  
- **V1 / V2 / V3** are vowels encoding 2‑bit states  
- **A / E / O / U** map to **00 / 01 / 10 / 11**

Thus each form = **6 bits**, and the full set of combinations yields:

```
4 × 4 × 4 = 64 forms
```

These 64 forms constitute the **complete structural space** of SUBIT‑Lingua.

---

## **2. Words (12‑bit form‑pairs)**

A SUBIT‑word is a **pair of forms**:

- **inner form** (micro‑configuration)  
- **outer form** (macro‑configuration)

Together they produce a 12‑bit structure:

```
Form‑1 (6 bits) + Form‑2 (6 bits) = 12 bits
```

The total number of possible words is:

```
64 × 64 = 4096
```

A word represents a **transition** or **mapping** between two structural states.

---

## **3. Higher‑Order Forms**

SUBIT‑Lingua extends naturally to higher orders:

- **form‑3** = 18 bits  
- **form‑4** = 24 bits  
- **form‑n** = n × 6 bits  

Higher‑order forms represent:

- sequences  
- processes  
- composite structures  
- multi‑layer configurations  

The system scales without introducing new primitives.

---

## **4. Axes (K / T / M)**

All forms are built on three fixed axes:

- **K** — internal / source / identity axis  
- **T** — structural / spatial / form axis  
- **M** — process / temporal / dynamic axis  

These axes do not encode bits; they define the **geometry** of the form.

---

## **5. Bit Mapping (A/E/O/U)**

Vowels encode the 2‑bit states:

- **A = 00**  
- **E = 01**  
- **O = 10**  
- **U = 11**

This mapping is consistent across all forms and all orders.

---

## **6. Notation**

Forms are written as:

```
KA‑TE‑MO
```

Words (form‑pairs) are written as:

```
KA‑TE‑MO – KU‑TA‑ME
```

Higher‑order forms are concatenations of 6‑bit units.

---

## **7. Purpose of SUBIT‑Lingua**

SUBIT‑Lingua is designed to:

- encode structural states  
- express transitions between states  
- model processes, flows, and configurations  
- provide a minimal, universal formal language  
- serve as a foundation for structural reasoning, analysis, and generation  

It is **pre‑semantic**: meaning emerges from structure, not from vocabulary.

---

## **8. System Properties**

SUBIT‑Lingua is:

- **finite** (64 forms, 4096 words)  
- **regular** (no exceptions or irregularities)  
- **combinatorial** (n×6‑bit scaling)  
- **bit‑driven** (A/E/O/U = 2‑bit states)  
- **axis‑based** (K/T/M geometry)  
- **fully deterministic**  
- **universally extensible**  

The system is closed, complete, and minimal.

---

## **9. Repository Structure**

The repository includes:

- **spec/** — formal definitions  
- **data/** — machine‑readable tables  
- **tools/** — generators and parsers  
- **docs/** — human‑readable explanations  
- **playground/** — interactive learning modules  
- **printable/** — physical sheets and cards  

Each layer reflects the structural logic of the language.

---

## **10. Summary**

SUBIT‑Lingua v3.0 is a **formal structural language** built from:

- 64 **forms** (6‑bit)  
- 4096 **form‑pairs** (12‑bit words)  
- n‑order **composite forms**  

It provides a minimal, universal framework for representing structure, transitions, and processes.

---
