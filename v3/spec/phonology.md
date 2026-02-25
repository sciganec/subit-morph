### **SUBIT‑Lingua v3.0 — Phonology (K/T/M + A/E/O/U System)**

SUBIT‑Lingua uses a **minimal, fully regular phonological system** designed to encode structural information with maximal clarity and minimal redundancy.

The phonology consists of:

- **3 consonants** (K, T, M)  
- **4 vowels** (A, E, O, U)  
- **strict CV‑CV‑CV form structure**  
- **bit‑encoded vowels**  
- **fixed consonantal axes**

This document defines the complete phonological system.

---

# **1. Consonants (K / T / M)**

SUBIT‑Lingua uses exactly **three consonants**, each representing a structural axis:

| Consonant | Axis | Structural Role |
|-----------|-------|------------------|
| **K** | internal axis | source, identity, interiority |
| **T** | structural axis | form, orientation, spatial configuration |
| **M** | process axis | dynamics, change, temporal configuration |

Consonants **never encode bits**.  
They define the **geometry** of the form.

Every form begins with:

```
K – T – M
```

in that fixed order.

---

# **2. Vowels (A / E / O / U)**

SUBIT‑Lingua uses exactly **four vowels**, each encoding a 2‑bit state:

| Vowel | Bits | Structural Interpretation |
|--------|--------|---------------------------|
| **A** | 00 | identity, stability |
| **E** | 01 | orientation, direction |
| **O** | 10 | variation, depth |
| **U** | 11 | emergence, transition |

Vowels are the **only bit‑bearing elements** of the language.

---

# **3. Syllable Structure (CV)**

All forms follow a strict **CV‑CV‑CV** pattern:

```
K V1 – T V2 – M V3
```

Where:

- consonants are fixed (K, T, M)  
- vowels vary (A/E/O/U)  
- each vowel contributes 2 bits  

This yields:

- **3 vowels × 2 bits = 6 bits per form**  
- **64 possible forms**

There are **no other syllable types** in SUBIT‑Lingua.

---

# **4. Phonotactic Rules**

SUBIT‑Lingua has **absolute phonotactic regularity**:

### **Allowed:**
- CV syllables only  
- K‑initial, T‑medial, M‑final consonants  
- A/E/O/U vowels only  
- hyphens between syllables for readability  

### **Not allowed:**
- consonant clusters  
- vowel clusters  
- syllable deletion  
- reordering of axes  
- additional consonants or vowels  
- diphthongs  
- tone or stress distinctions  

SUBIT‑Lingua is intentionally **non‑naturalistic**.

---

# **5. Bit Encoding**

Vowels encode bits as follows:

```
A = 00
E = 01
O = 10
U = 11
```

Thus a form:

```
KA‑TE‑MO
```

encodes:

```
00 01 10
```

This mapping is consistent across:

- first‑order forms (6 bits)  
- second‑order forms (12 bits)  
- higher‑order forms (n × 6 bits)

---

# **6. Pronunciation Guide**

SUBIT‑Lingua uses **simple, unambiguous phonetics**:

| Symbol | IPA | Notes |
|--------|------|--------|
| **K** | /k/ | voiceless velar stop |
| **T** | /t/ | voiceless alveolar stop |
| **M** | /m/ | bilabial nasal |
| **A** | /a/ | open front vowel |
| **E** | /e/ | mid front vowel |
| **O** | /o/ | mid back vowel |
| **U** | /u/ | close back vowel |

All forms are pronounced with **equal stress** and **flat prosody**.

Example:

```
KA‑TE‑MO → /ka.te.mo/
```

---

# **7. Orthography**

SUBIT‑Lingua uses:

- uppercase Latin letters  
- hyphens between syllables  
- en‑dash (–) between forms in a word  

Examples:

```
KA‑TA‑MA
KA‑TE‑MO – KU‑TA‑ME
KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU
```

There are **no alternative spellings**.

---

# **8. Rationale for the Phonological System**

The phonology is designed to be:

### **Minimal**
Only 3 consonants and 4 vowels.

### **Regular**
No exceptions, no irregular forms.

### **Bit‑Driven**
Vowels encode all structural information.

### **Axis‑Based**
Consonants define the geometry of the form.

### **Universal**
No cultural or linguistic bias.

### **Composable**
Higher‑order forms are concatenations of CV units.

This makes SUBIT‑Lingua a **formal structural language**, not a naturalistic one.

---

# **9. Summary**

- SUBIT‑Lingua uses **3 consonants** and **4 vowels**  
- Forms follow **CV‑CV‑CV** structure  
- Vowels encode **6 bits per form**  
- Consonants define **axes**, not bits  
- Phonology is **minimal, regular, and deterministic**  
- All higher‑order structures inherit this system  

This document defines the complete phonological foundation of SUBIT‑Lingua v3.0.

---
