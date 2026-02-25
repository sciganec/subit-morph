#!/usr/bin/env python3
"""
SUBIT-Lingua v3.0
decoder.py

Decodes:
- 6-bit strings → forms (KA-TE-MO)
- 12-bit strings → words (KA-TE-MO – KU-TA-ME)
- n×6-bit strings → sequences of forms

Place in: tools/decoder.py
"""

import re

# ---------------------------------------------------------------------------
# Canonical SUBIT-Lingua definitions
# ---------------------------------------------------------------------------

AXES = ["K", "T", "M"]

BITS = {
    "A": "00",
    "E": "01",
    "O": "10",
    "U": "11",
}

INV_BITS = {v: k for k, v in BITS.items()}

FORM_BITS_RE = re.compile(r"^[01]{6}$")
WORD_BITS_RE = re.compile(r"^[01]{12}$")
SEQ_BITS_RE  = re.compile(r"^[01]+$")


# ---------------------------------------------------------------------------
# FORM DECODING
# ---------------------------------------------------------------------------

def decode_form_bits(bits: str) -> str:
    """
    Decode a 6-bit string like:
        "000110"
    into a SUBIT-Lingua form:
        "KA-TE-MO"
    """
    if not FORM_BITS_RE.fullmatch(bits):
        raise ValueError(f"Invalid 6-bit form: {bits}")

    v1 = INV_BITS[bits[0:2]]
    v2 = INV_BITS[bits[2:4]]
    v3 = INV_BITS[bits[4:6]]

    return f"K{v1}-T{v2}-M{v3}"


# ---------------------------------------------------------------------------
# WORD DECODING (FORM-PAIRS)
# ---------------------------------------------------------------------------

def decode_word_bits(bits: str) -> str:
    """
    Decode a 12-bit string like:
        "000110110001"
    into a SUBIT-Lingua word:
        "KA-TE-MO – KU-TA-ME"
    """
    if not WORD_BITS_RE.fullmatch(bits):
        raise ValueError(f"Invalid 12-bit word: {bits}")

    inner = decode_form_bits(bits[0:6])
    outer = decode_form_bits(bits[6:12])

    return f"{inner} – {outer}"


# ---------------------------------------------------------------------------
# SEQUENCE DECODING (HIGHER-ORDER FORMS)
# ---------------------------------------------------------------------------

def decode_sequence_bits(bits: str) -> list[str]:
    """
    Decode an n×6-bit string like:
        "000110110001010011"
    into:
        ["KA-TE-MO", "KU-TA-ME", "KE-TO-MU"]
    """
    if not SEQ_BITS_RE.fullmatch(bits):
        raise ValueError(f"Invalid bitstream: {bits}")

    if len(bits) % 6 != 0:
        raise ValueError("Bitstream length must be a multiple of 6.")

    forms = []
    for i in range(0, len(bits), 6):
        chunk = bits[i:i+6]
        forms.append(decode_form_bits(chunk))

    return forms


# ---------------------------------------------------------------------------
# GENERIC DISPATCH
# ---------------------------------------------------------------------------

def decode(bits: str):
    """
    Generic decoder:
    - 6 bits → form
    - 12 bits → word
    - n×6 bits → sequence of forms
    """
    if not isinstance(bits, str):
        raise TypeError("decode() accepts a bitstring.")

    if len(bits) == 6:
        return decode_form_bits(bits)

    if len(bits) == 12:
        return decode_word_bits(bits)

    return decode_sequence_bits(bits)


# ---------------------------------------------------------------------------
# DEMO
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("Form:", decode("000110"))
    print("Word:", decode("000110110001"))
    print("Sequence:", decode("000110110001010011"))
