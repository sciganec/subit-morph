### **SUBIT‑Lingua v3.0 — The 64 Forms (6‑bit Structural Units)**

SUBIT‑Lingua defines **64 atomic forms**, each representing a unique structural configuration in a 3‑axis system.  
Forms are the **first‑order units** of the language.  
All higher‑order expressions (words, sequences, processes) are built from these forms.

A form is defined as:

```
K V1 – T V2 – M V3
```

Where:

- **K / T / M** are fixed structural axes  
- **V1 / V2 / V3** are vowels encoding 2‑bit states  
- **A / E / O / U** map to **00 / 01 / 10 / 11**

Thus each form = **6 bits**, and the full combinatorial space yields:

```
4 × 4 × 4 = 64 forms
```

These 64 forms constitute the complete structural basis of SUBIT‑Lingua.

---

# **1. Bit Mapping**

Vowels encode 2‑bit states:

| Vowel | Bits |
|-------|-------|
| **A** | 00 |
| **E** | 01 |
| **O** | 10 |
| **U** | 11 |

This mapping is consistent across all forms and all orders.

---

# **2. Axes**

The three axes define the geometry of a form:

- **K** — internal / source axis  
- **T** — structural / spatial axis  
- **M** — process / dynamic axis  

Axes do not encode bits; they define the structural frame.

---

# **3. Table of 64 Forms**

Each form is listed with:

- **Code** (F00–F63)  
- **Form notation** (K?–T?–M?)  
- **6‑bit address**  
- **Short structural description**  

Descriptions are structural labels, not semantic meanings.

---

## **A‑A‑A → A‑A‑U (00 00 00 → 00 00 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F00 | KA‑TA‑MA | 00 00 00 | internal identity |
| F01 | KA‑TA‑ME | 00 00 01 | internal differentiation |
| F02 | KA‑TA‑MO | 00 00 10 | internal depth |
| F03 | KA‑TA‑MU | 00 00 11 | internal tension |

---

## **A‑E‑A → A‑E‑U (00 01 00 → 00 01 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F04 | KA‑TE‑MA | 00 01 00 | internal structure |
| F05 | KA‑TE‑ME | 00 01 01 | internal orientation |
| F06 | KA‑TE‑MO | 00 01 10 | internal variation |
| F07 | KA‑TE‑MU | 00 01 11 | internal modality |

---

## **A‑O‑A → A‑O‑U (00 10 00 → 00 10 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F08 | KA‑TO‑MA | 00 10 00 | internal layer |
| F09 | KA‑TO‑ME | 00 10 01 | internal gradient |
| F10 | KA‑TO‑MO | 00 10 10 | internal shift |
| F11 | KA‑TO‑MU | 00 10 11 | internal transition |

---

## **A‑U‑A → A‑U‑U (00 11 00 → 00 11 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F12 | KA‑TU‑MA | 00 11 00 | internal state |
| F13 | KA‑TU‑ME | 00 11 01 | internal signal |
| F14 | KA‑TU‑MO | 00 11 10 | internal function |
| F15 | KA‑TU‑MU | 00 11 11 | internal emergence |

---

## **E‑A‑A → E‑A‑U (01 00 00 → 01 00 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F16 | KE‑TA‑MA | 01 00 00 | structural identity |
| F17 | KE‑TA‑ME | 01 00 01 | structural differentiation |
| F18 | KE‑TA‑MO | 01 00 10 | structural depth |
| F19 | KE‑TA‑MU | 01 00 11 | structural tension |

---

## **E‑E‑A → E‑E‑U (01 01 00 → 01 01 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F20 | KE‑TE‑MA | 01 01 00 | structural form |
| F21 | KE‑TE‑ME | 01 01 01 | structural orientation |
| F22 | KE‑TE‑MO | 01 01 10 | structural variation |
| F23 | KE‑TE‑MU | 01 01 11 | structural modality |

---

## **E‑O‑A → E‑O‑U (01 10 00 → 01 10 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F24 | KE‑TO‑MA | 01 10 00 | structural layer |
| F25 | KE‑TO‑ME | 01 10 01 | structural gradient |
| F26 | KE‑TO‑MO | 01 10 10 | structural shift |
| F27 | KE‑TO‑MU | 01 10 11 | structural transition |

---

## **E‑U‑A → E‑U‑U (01 11 00 → 01 11 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F28 | KE‑TU‑MA | 01 11 00 | structural state |
| F29 | KE‑TU‑ME | 01 11 01 | structural signal |
| F30 | KE‑TU‑MO | 01 11 10 | structural function |
| F31 | KE‑TU‑MU | 01 11 11 | structural emergence |

---

## **O‑A‑A → O‑A‑U (10 00 00 → 10 00 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F32 | KO‑TA‑MA | 10 00 00 | process identity |
| F33 | KO‑TA‑ME | 10 00 01 | process differentiation |
| F34 | KO‑TA‑MO | 10 00 10 | process depth |
| F35 | KO‑TA‑MU | 10 00 11 | process tension |

---

## **O‑E‑A → O‑E‑U (10 01 00 → 10 01 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F36 | KO‑TE‑MA | 10 01 00 | process form |
| F37 | KO‑TE‑ME | 10 01 01 | process orientation |
| F38 | KO‑TE‑MO | 10 01 10 | process variation |
| F39 | KO‑TE‑MU | 10 01 11 | process modality |

---

## **O‑O‑A → O‑O‑U (10 10 00 → 10 10 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F40 | KO‑TO‑MA | 10 10 00 | process layer |
| F41 | KO‑TO‑ME | 10 10 01 | process gradient |
| F42 | KO‑TO‑MO | 10 10 10 | process shift |
| F43 | KO‑TO‑MU | 10 10 11 | process transition |

---

## **O‑U‑A → O‑U‑U (10 11 00 → 10 11 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F44 | KO‑TU‑MA | 10 11 00 | process state |
| F45 | KO‑TU‑ME | 10 11 01 | process signal |
| F46 | KO‑TU‑MO | 10 11 10 | process function |
| F47 | KO‑TU‑MU | 10 11 11 | process emergence |

---

## **U‑A‑A → U‑A‑U (11 00 00 → 11 00 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F48 | KU‑TA‑MA | 11 00 00 | emergent identity |
| F49 | KU‑TA‑ME | 11 00 01 | emergent differentiation |
| F50 | KU‑TA‑MO | 11 00 10 | emergent depth |
| F51 | KU‑TA‑MU | 11 00 11 | emergent tension |

---

## **U‑E‑A → U‑E‑U (11 01 00 → 11 01 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F52 | KU‑TE‑MA | 11 01 00 | emergent form |
| F53 | KU‑TE‑ME | 11 01 01 | emergent orientation |
| F54 | KU‑TE‑MO | 11 01 10 | emergent variation |
| F55 | KU‑TE‑MU | 11 01 11 | emergent modality |

---

## **U‑O‑A → U‑O‑U (11 10 00 → 11 10 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F56 | KU‑TO‑MA | 11 10 00 | emergent layer |
| F57 | KU‑TO‑ME | 11 10 01 | emergent gradient |
| F58 | KU‑TO‑MO | 11 10 10 | emergent shift |
| F59 | KU‑TO‑MU | 11 10 11 | emergent transition |

---

## **U‑U‑A → U‑U‑U (11 11 00 → 11 11 11)**

| Code | Form | Bits | Description |
|------|--------|--------|--------------|
| F60 | KU‑TU‑MA | 11 11 00 | emergent state |
| F61 | KU‑TU‑ME | 11 11 01 | emergent signal |
| F62 | KU‑TU‑MO | 11 11 10 | emergent function |
| F63 | KU‑TU‑MU | 11 11 11 | emergent emergence |

---

# **Summary**

- **64 forms** = complete 6‑bit structural space  
- **Form = K?–T?–M?** with vowel‑encoded bits  
- **Words = form‑pairs (12 bits)**  
- **Higher‑order forms = n×6‑bit structures**  
- SUBIT‑Lingua is a **formal, structural, combinatorial language**

---
