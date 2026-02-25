### **SUBIT‑Lingua v3.0 — A Minimal Structural Language**

SUBIT‑Lingua is a **formal, structural, bit‑driven language** built on a universal template:

- three fixed axes (**K**, **T**, **M**)  
- four vowel‑states (**A**, **E**, **O**, **U**)  
- one form structure (**CV‑CV‑CV**)  
- one bit‑mapping (**A/E/O/U → 00/01/10/11**)  
- one combinatorial rule (**6‑bit forms → 12‑bit words → n×6‑bit sequences**)  

It is not a natural language and not a semantic system.  
SUBIT‑Lingua is a **structural calculus** for representing configurations, transitions, and processes.

This repository contains the complete SUBIT‑Lingua v3.0 specification, tools, examples, and interactive playground.

---

# **1. Features**

- **64 atomic forms** (6‑bit units)  
- **4096 words** (12‑bit transitions)  
- **unbounded higher‑order sequences** (n×6 bits)  
- **deterministic encoding/decoding**  
- **strict notation rules**  
- **complete generator + parser + encoder + decoder**  
- **interactive playground notebook**  

SUBIT‑Lingua is fully finite, fully regular, and fully machine‑readable.

---

# **2. Quick Overview**

### **Forms (6 bits)**  
```
KA‑TE‑MO
```
→ `000110`

### **Words (12 bits)**  
```
KA‑TE‑MO – KU‑TA‑ME
```
→ `000110110001`

### **Sequences (n×6 bits)**  
```
KA‑TE‑MO – KU‑TA‑ME – KE‑TO‑MU
```
→ `000110 110001 011011`

---

# **3. Repository Structure**

```
/
├── introduction.md        # What SUBIT‑Lingua is
├── philosophy.md          # Why the system exists
├── notation.md            # Official notation rules
├── examples.md            # Worked examples
├── tutorial.md            # Step‑by‑step learning path
│
├── phonology.md           # CV‑CV‑CV structure
├── axes.md                # K/T/M axis definitions
├── bit-mapping.md         # A/E/O/U → 00/01/10/11
│
├── forms-64.csv           # 64 forms (table)
├── forms-64.json          # 64 forms (JSON)
├── lexicon-4096.json      # 4096 words (JSON)
│
├── tools/
│   ├── generator.py       # Generate forms + lexicon
│   ├── parser.py          # Parse forms/words/bitstreams
│   ├── encoder.py         # Encode forms/words/sequences
│   ├── decoder.py         # Decode bitstreams
│
└── playground.ipynb       # Interactive environment
```

Everything in the repository is **self‑contained** and **dependency‑free**.

---

# **4. Getting Started**

### **Encode a form**
```python
from tools.encoder import encode
encode("KA‑TE‑MO")
# "000110"
```

### **Decode a form**
```python
from tools.decoder import decode
decode("000110")
# "KA‑TE‑MO"
```

### **Encode a word**
```python
encode("KA‑TE‑MO – KU‑TA‑ME")
# "000110110001"
```

### **Decode a sequence**
```python
decode("000110110001011011")
# ["KA‑TE‑MO", "KU‑TA‑ME", "KE‑TO‑MU"]
```

---

# **5. Philosophy (Short Version)**

SUBIT‑Lingua is built on three principles:

### **1. Structure precedes meaning**  
Forms encode configurations, not concepts.

### **2. Transitions define meaning**  
Words represent structural mappings, not lexical items.

### **3. Process is primary**  
Sequences represent flows, not descriptions.

For the full conceptual foundation, see **philosophy.md**.

---

# **6. Specification Files**

- **introduction.md** — overview of the system  
- **notation.md** — canonical writing rules  
- **phonology.md** — form structure  
- **axes.md** — K/T/M definitions  
- **bit-mapping.md** — vowel → bit mapping  
- **examples.md** — worked examples  
- **tutorial.md** — guided learning path  

These documents define the entire SUBIT‑Lingua v3.0 standard.

---

# **7. Tools**

The `tools/` directory contains:

- **generator.py** — build forms + lexicon  
- **parser.py** — parse forms/words/bitstreams  
- **encoder.py** — encode forms/words/sequences  
- **decoder.py** — decode bitstreams  

All tools are:

- single‑file  
- dependency‑free  
- deterministic  
- aligned with the spec  

---

# **8. Interactive Playground**

The repository includes:

```
playground.ipynb
```

A full Jupyter notebook with:

- encoder/decoder cells  
- bitstream visualizer  
- lexicon lookup  
- structural patterns  
- SUBIT cube viewer  

This is the recommended way to explore the system.

---

# **9. License**

SUBIT‑Lingua v3.0 is released under an open, permissive license suitable for:

- research  
- experimentation  
- agent communication  
- structural modeling  
- educational use  

(Insert your preferred license here.)

---

# **10. Summary**

SUBIT‑Lingua v3.0 is a:

- **minimal**  
- **regular**  
- **bit‑driven**  
- **structural**  
- **combinatorial**  
- **universal**  

language for representing forms, transitions, and processes.

It is the formal linguistic layer of the SUBIT system.

---
