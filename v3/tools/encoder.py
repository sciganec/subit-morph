#!/usr/bin/env python3
"""
SUBIT-Lingua v3.0
encoder.py

Encodes:
- forms (KA-TE-MO) → 6-bit strings
- words (KA-TE-MO – KU-TA-ME) → 12-bit strings
- sequences of forms → n×6-bit strings

Place in: tools/encoder.py
"""

import re

# --- Core SUBIT-Lingua definitions -----------------------------------------

AXES = ["K", "T", "M"]
VOWELS = ["A", "E", "O", "U"]

BITS = {
    "A": "00",
    "E": "01",
    "O": "10",
    "U": "11",
}

# Regex patterns
FORM_RE = re.compile(r"^[K][AEOU]-[T][AEOU]-[M][AEOU]$")
WORD_RE = re.compile(r"^[K][AEOU]-[T][AEOU]-[M][AEOU]\s+–\s+[K][AEOU]-[T][AEOU]-[M][AEOU]$")


# ---------------------------------------------------------------------------
# FORM ENCODING
# ---------------------------------------------------------------------------

def encode_form(form: str) -> str:
    """
    Encode a SUBIT-Lingua form like:
        "KA-TE-MO"
    into a 6-bit string:
        "000110"
    """
    if not FORM_RE.fullmatch(form):
        raise ValueError(f"Invalid form: {form}")

    syllables = form.split("-")
    vowels = [s[1] for s in syllables]

    return "".join(BITS[v] for v in vowels)


# ---------------------------------------------------------------------------
# WORD ENCODING (FORM-PAIRS)
# ---------------------------------------------------------------------------

def encode_word(word: str) -> str:
    """
    Encode a SUBIT-Lingua word like:
        "KA-TE-MO – KU-TA-ME"
    into a 12-bit string:
        "000110110001"
    """
    if not WORD_RE.fullmatch(word):
        raise ValueError(f"Invalid word: {word}")

    left, right = [p.strip() for p in word.split("–")]

    inner_bits = encode_form(left)
    outer_bits = encode_form(right)

    return inner_bits + outer_bits


# ---------------------------------------------------------------------------
# SEQUENCE ENCODING (HIGHER-ORDER FORMS)
# ---------------------------------------------------------------------------

def encode_sequence(seq: list[str]) -> str:
    """
    Encode a sequence of forms:
        ["KA-TE-MO", "KU-TA-ME", "KE-TO-MU"]
    into an 18-bit string:
        "000110110001011011"
    """
    bits = []
    for form in seq:
        bits.append(encode_form(form))
    return "".join(bits)


# ---------------------------------------------------------------------------
# GENERIC DISPATCH
# ---------------------------------------------------------------------------

def encode(obj):
    """
    Generic encoder:
    - form string → 6 bits
    - word string → 12 bits
    - list of forms → n×6 bits
    """
    if isinstance(obj, str):
        if "–" in obj:
            return encode_word(obj)
        return encode_form(obj)

    if isinstance(obj, list):
        return encode_sequence(obj)

    raise TypeError("encode() accepts a form string, word string, or list of forms.")


# ---------------------------------------------------------------------------
# DEMO
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Form:", encode("KA-TE-MO"))
    print("Word:", encode("KA-TE-MO – KU-TA-ME"))
    print("Sequence:", encode(["KA-TE-MO", "KU-TA-ME", "KE-TO-MU"]))
