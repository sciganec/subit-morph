#!/usr/bin/env python3
"""
SUBIT-Lingua v3.0
parser.py

Parses:
- forms (KA-TE-MO or 000110)
- words (KA-TE-MO – KU-TA-ME or 000110110001)

Place in: tools/parser.py
"""

import re

# --- Core SUBIT-Lingua definitions ---

AXES = ["K", "T", "M"]
VOWELS = ["A", "E", "O", "U"]

BITS = {
    "A": "00",
    "E": "01",
    "O": "10",
    "U": "11",
}

INV_BITS = {v: k for k, v in BITS.items()}


# ---------------------------------------------------------------------------
# FORM PARSING
# ---------------------------------------------------------------------------

def parse_form_string(form: str) -> dict:
    """
    Parse a form like "KA-TE-MO" into:
    {
      "form": "KA-TE-MO",
      "bits": "000110",
      "vowels": ["A","E","O"],
      "axes": ["K","T","M"]
    }
    """
    if not re.fullmatch(r"[K][AEOU]-[T][AEOU]-[M][AEOU]", form):
        raise ValueError(f"Invalid form string: {form}")

    syllables = form.split("-")
    axes = [s[0] for s in syllables]
    vowels = [s[1] for s in syllables]

    bits = "".join(BITS[v] for v in vowels)

    return {
        "form": form,
        "bits": bits,
        "axes": axes,
        "vowels": vowels,
    }


def parse_form_bits(bits: str) -> dict:
    """
    Parse a 6-bit string like "000110" into:
    {
      "form": "KA-TE-MO",
      "bits": "000110",
      "vowels": ["A","E","O"],
      "axes": ["K","T","M"]
    }
    """
    if not re.fullmatch(r"[01]{6}", bits):
        raise ValueError(f"Invalid 6-bit form: {bits}")

    v1 = INV_BITS[bits[0:2]]
    v2 = INV_BITS[bits[2:4]]
    v3 = INV_BITS[bits[4:6]]

    form = f"K{v1}-T{v2}-M{v3}"

    return {
        "form": form,
        "bits": bits,
        "axes": AXES,
        "vowels": [v1, v2, v3],
    }


# ---------------------------------------------------------------------------
# WORD PARSING (FORM-PAIRS)
# ---------------------------------------------------------------------------

def parse_word_string(word: str) -> dict:
    """
    Parse a word like:
      "KA-TE-MO – KU-TA-ME"

    Returns:
    {
      "inner": {...form object...},
      "outer": {...form object...},
      "word_bits": "000110110001",
      "word": "KA-TE-MO – KU-TA-ME"
    }
    """
    if "–" not in word:
        raise ValueError("Word must contain an en-dash (–) between forms.")

    left, right = [p.strip() for p in word.split("–")]

    inner = parse_form_string(left)
    outer = parse_form_string(right)

    return {
        "inner": inner,
        "outer": outer,
        "word_bits": inner["bits"] + outer["bits"],
        "word": word,
    }


def parse_word_bits(bits: str) -> dict:
    """
    Parse a 12-bit word like:
      "000110110001"

    Returns:
    {
      "inner": {...},
      "outer": {...},
      "word_bits": "000110110001",
      "word": "KA-TE-MO – KU-TA-ME"
    }
    """
    if not re.fullmatch(r"[01]{12}", bits):
        raise ValueError(f"Invalid 12-bit word: {bits}")

    inner_bits = bits[0:6]
    outer_bits = bits[6:12]

    inner = parse_form_bits(inner_bits)
    outer = parse_form_bits(outer_bits)

    word_str = f"{inner['form']} – {outer['form']}"

    return {
        "inner": inner,
        "outer": outer,
        "word_bits": bits,
        "word": word_str,
    }


# ---------------------------------------------------------------------------
# DEMO (optional)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print(parse_form_string("KA-TE-MO"))
    print(parse_form_bits("000110"))
    print(parse_word_string("KA-TE-MO – KU-TA-ME"))
    print(parse_word_bits("000110110001"))
