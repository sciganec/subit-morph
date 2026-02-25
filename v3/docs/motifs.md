### **SUBIT‑Lingua v3.0 — Structural Motifs**

SUBIT‑Lingua motifs are **recurring structural patterns** that appear in:

- the 64‑form cube  
- the 4096‑word transition grid  
- higher‑order sequences  
- lattice paths  
- finite‑state machines  
- bit‑geometry  

Motifs are **pre‑semantic**: they describe *shapes of structure*, not meanings.  
They are the building blocks of SUBIT‑Lingua reasoning.

---

# **1. Axis Motifs**

Axis motifs are flows that vary **one axis at a time**.

---

## **1.1 K‑Axis Sweep**

Only the **K vowel** changes:

```
KA‑TE‑MO → KE‑TE‑MO → KO‑TE‑MO → KU‑TE‑MO
```

This is a **pure internal‑axis progression**.

---

## **1.2 T‑Axis Sweep**

Only the **T vowel** changes:

```
KA‑TA‑MO → KA‑TE‑MO → KA‑TO‑MO → KA‑TU‑MO
```

A **structural‑axis progression**.

---

## **1.3 M‑Axis Sweep**

Only the **M vowel** changes:

```
KA‑TE‑MA → KA‑TE‑ME → KA‑TE‑MO → KA‑TE‑MU
```

A **process‑axis progression**.

---

# **2. Diagonal Motifs**

Diagonal motifs vary **multiple axes simultaneously**.

---

## **2.1 Primary Diagonal (A→E→O→U)**

```
KA‑TA‑MA → KE‑TE‑ME → KO‑TO‑MO → KU‑TU‑MU
```

This is the **canonical diagonal** through the cube.

---

## **2.2 Counter‑Diagonal**

```
KU‑TU‑MU → KO‑TO‑MO → KE‑TE‑ME → KA‑TA‑MA
```

The reverse traversal.

---

## **2.3 Mixed Diagonal**

```
KA‑TE‑MO → KE‑TO‑MU → KO‑TU‑ME → KU‑TA‑MO
```

A diagonal that rotates across axes.

---

# **3. Cyclic Motifs**

Cycles are **closed loops** in form‑space.

---

## **3.1 4‑Cycle (Square Loop)**

```
KA‑TE‑MO → KE‑TE‑MO → KE‑TE‑ME → KA‑TE‑ME → KA‑TE‑MO
```

ASCII:

```
KA-TE-MO --> KE-TE-MO
     ^               |
     |               v
KA-TE-ME <-- KE-TE-ME
```

---

## **3.2 8‑Cycle (Cube Perimeter)**

```
KA‑TA‑MA → KA‑TE‑MA → KA‑TE‑ME → KA‑TA‑ME
→ KE‑TA‑ME → KE‑TE‑ME → KE‑TE‑MA → KE‑TA‑MA → (back)
```

A loop around a **2×2×2 subcube**.

---

## **3.3 Axis‑Alternating Cycle**

```
KA‑TE‑MO → KA‑TO‑MO → KE‑TO‑MO → KE‑TE‑MO → (back)
```

Alternates between **T** and **K** changes.

---

# **4. Transition Motifs (Words)**

Words are **directed transitions** between forms.

---

## **4.1 Single‑Axis Transition**

```
KA‑TE‑MO – KE‑TE‑MO
```

Only K changes.

---

## **4.2 Dual‑Axis Transition**

```
KA‑TE‑MO – KE‑TO‑MO
```

K and T change.

---

## **4.3 Full‑Axis Transition**

```
KA‑TE‑MO – KU‑TU‑MU
```

All three axes change.

---

## **4.4 Minimal Hamming Transition**

```
KA‑TE‑MO – KA‑TE‑ME
```

Hamming distance = 1 (only last vowel changes).

---

## **4.5 Maximal Hamming Transition**

```
KA‑TA‑MA – KU‑TU‑MU
```

Hamming distance = 3 (all vowels change).

---

# **5. Sequence Motifs**

Sequences are **paths** through the form‑space.

---

## **5.1 Linear Sequence**

```
KA‑TE‑MO → KU‑TA‑ME → KE‑TO‑MU → KO‑TU‑MA
```

A simple chain.

---

## **5.2 Ladder Sequence**

```
KA‑TA‑MA
KA‑TE‑MA
KA‑TE‑ME
KE‑TE‑ME
KE‑TO‑ME
KO‑TO‑ME
```

A monotonic lattice path.

---

## **5.3 Spiral Sequence (Cube Spiral)**

```
KA‑TA‑MA
→ KA‑TE‑MA
→ KA‑TE‑ME
→ KA‑TA‑ME
→ KE‑TA‑ME
→ KE‑TE‑ME
→ KE‑TE‑MA
→ KE‑TA‑MA
```

A spiral around a 2×2 face.

---

## **5.4 Zig‑Zag Sequence**

```
KA‑TE‑MO → KE‑TE‑MO → KE‑TE‑ME → KO‑TE‑ME → KO‑TE‑MO → KU‑TE‑MO
```

Alternates direction across axes.

---

# **6. Bit‑Geometry Motifs**

Motifs expressed directly in bit‑space.

---

## **6.1 Hamming Sphere (Radius 1)**

Center: `000110` (KA‑TE‑MO)

Neighbors:

```
000111  KA‑TE‑MU
000100  KA‑TE‑MA
000101  KA‑TE‑ME
001110  KA‑TU‑MO
010110  KE‑TE‑MO
100110  KO‑TE‑MO
```

---

## **6.2 Hamming Path**

```
000000 → 000001 → 000011 → 000111 → 001111 → 011111 → 111111
```

A monotonic bit‑ascending path.

---

## **6.3 Bit‑Diagonal**

```
00 01 10 → 01 10 11 → 10 11 00 → 11 00 01
```

The bit‑space analogue of the primary diagonal.

---

# **7. Program Motifs (Higher‑Order Structures)**

Higher‑order motifs represent **structural programs**.

---

## **7.1 Three‑Stage Program**

```
KA‑TE‑MO
→ KU‑TA‑ME
→ KE‑TO‑MU
```

---

## **7.2 Four‑Stage Program**

```
KA‑TA‑MA
→ KE‑TE‑MA
→ KO‑TE‑ME
→ KU‑TO‑MU
```

---

## **7.3 Branching Program**

```
KA‑TE‑MO
   | \
   |  \
   v   v
KE‑TE‑MO   KA‑TO‑MO
```

A **fork** in structural evolution.

---

## **7.4 Converging Program**

```
KE‑TE‑MO → KA‑TE‑MO ← KO‑TE‑MO
```

A **merge** motif.

---

# **8. Composite Motifs**

Motifs can be combined.

---

## **8.1 Sweep + Cycle**

```
KA‑TE‑MO → KE‑TE‑MO → KE‑TE‑ME → KA‑TE‑ME → KA‑TE‑MO
→ KA‑TO‑MO → KA‑TU‑MO
```

Cycle followed by axis sweep.

---

## **8.2 Diagonal + Ladder**

```
KA‑TA‑MA → KE‑TE‑ME → KO‑TO‑MO → KU‑TU‑MU
→ KU‑TU‑ME → KU‑TU‑MA
```

Diagonal then monotonic descent.

---

# **9. Summary**

This document defines the canonical SUBIT‑Lingua motifs:

- axis sweeps  
- diagonals  
- cycles  
- transitions  
- sequences  
- spirals  
- zig‑zags  
- Hamming spheres  
- higher‑order programs  
- composite flows  

Motifs reveal the **deep geometry** of SUBIT‑Lingua v3.0 and serve as the foundation for structural reasoning, process modeling, and agent communication.

---
