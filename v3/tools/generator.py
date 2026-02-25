#!/usr/bin/env python3
"""
SUBIT-Lingua v3.0
generator.py

Generates:
- forms-64.json
- forms-64.csv
- lexicon-4096.json
- lexicon-4096.csv

Place this file in: tools/generator.py
Run from repo root: python3 tools/generator.py
"""

import json
import csv
from itertools import product
from pathlib import Path

# --- Core SUBIT-Lingua definitions ---

VOWELS = ["A", "E", "O", "U"]
BITS = {
    "A": "00",
    "E": "01",
    "O": "10",
    "U": "11",
}
AXES = ["K", "T", "M"]  # K/T/M fixed order


# --- Form construction ------------------------------------------------------


def bits_to_vowels(bitstring: str) -> list[str]:
    """Convert 6-bit string into [V1, V2, V3] using inverse mapping."""
    if len(bitstring) != 6:
        raise ValueError("Form bitstring must be 6 bits.")
    inv = {v: k for k, v in BITS.items()}
    return [inv[bitstring[0:2]], inv[bitstring[2:4]], inv[bitstring[4:6]]]


def index_to_bits(i: int) -> str:
    """0–63 → 6-bit string."""
    if not (0 <= i < 64):
        raise ValueError("Form index must be in [0, 63].")
    return f"{i:06b}"


def form_from_index(i: int) -> dict:
    """
    Given an integer 0–63, return:
    {
      "code": "F00",
      "form": "KA-TA-MA",
      "bits": "000000",
      "description": "..."
    }
    Description is derived from K vowel band:
      A* = internal
      E* = structural
      O* = process
      U* = emergent
    and M vowel band:
      *A = identity/state
      *E = orientation/signal
      *O = depth/function
      *U = tension/emergence
    """
    bits = index_to_bits(i)
    v1, v2, v3 = bits_to_vowels(bits)

    syllables = [AXES[j] + [v1, v2, v3][j] for j in range(3)]
    form_str = "-".join(syllables)

    # High-level band from K vowel
    band_map = {
        "A": "internal",
        "E": "structural",
        "O": "process",
        "U": "emergent",
    }
    # Low-level nuance from M vowel
    nuance_map = {
        "A": "identity",
        "E": "signal" if band_map[v1] != "internal" else "differentiation",
        "O": "function" if band_map[v1] != "internal" else "depth",
        "U": "emergence" if band_map[v1] != "internal" else "tension",
    }

    band = band_map[v1]
    nuance = nuance_map[v3]
    description = f"{band} {nuance}"

    return {
        "code": f"F{i:02d}",
        "form": form_str,
        "bits": bits,
        "description": description,
    }


# --- Word construction ------------------------------------------------------


def word_object(inner_idx: int, outer_idx: int) -> dict:
    """
    Build a single word object:
    {
      "inner_code": "F00",
      "outer_code": "F37",
      "inner_form": "KA-TA-MA",
      "outer_form": "KO-TE-ME",
      "inner_bits": "000000",
      "outer_bits": "100101",
      "word_bits": "000000100101",
      "word": "KA-TA-MA – KO-TE-ME"
    }
    """
    inner = form_from_index(inner_idx)
    outer = form_from_index(outer_idx)

    inner_bits = inner["bits"]
    outer_bits = outer["bits"]
    word_bits = inner_bits + outer_bits

    word_str = f"{inner['form']} – {outer['form']}"

    return {
        "inner_code": inner["code"],
        "outer_code": outer["code"],
        "inner_form": inner["form"],
        "outer_form": outer["form"],
        "inner_bits": inner_bits,
        "outer_bits": outer_bits,
        "word_bits": word_bits,
        "word": word_str,
    }


# --- Generators -------------------------------------------------------------


def generate_forms_64():
    """Return list of 64 form dicts."""
    return [form_from_index(i) for i in range(64)]


def generate_lexicon_4096():
    """Return list of 4096 word dicts."""
    lexicon = []
    for inner_idx, outer_idx in product(range(64), range(64)):
        lexicon.append(word_object(inner_idx, outer_idx))
    return lexicon


# --- Writers ----------------------------------------------------------------


def write_forms_json(path: Path):
    forms = generate_forms_64()
    with path.open("w", encoding="utf-8") as f:
        json.dump(forms, f, ensure_ascii=False, separators=(",", ":"))


def write_forms_csv(path: Path):
    forms = generate_forms_64()
    fieldnames = ["code", "form", "bits", "description"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in forms:
            writer.writerow(row)


def write_lexicon_json(path: Path):
    lexicon = generate_lexicon_4096()
    with path.open("w", encoding="utf-8") as f:
        json.dump(lexicon, f, ensure_ascii=False, separators=(",", ":"))


def write_lexicon_csv(path: Path):
    lexicon = generate_lexicon_4096()
    fieldnames = [
        "inner_code",
        "outer_code",
        "inner_form",
        "outer_form",
        "inner_bits",
        "outer_bits",
        "word_bits",
        "word",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in lexicon:
            writer.writerow(row)


# --- Main -------------------------------------------------------------------


def main():
    root = Path(".")
    data_dir = root / "data"
    data_dir.mkdir(exist_ok=True)

    forms_json_path = data_dir / "forms-64.json"
    forms_csv_path = data_dir / "forms-64.csv"
    lex_json_path = data_dir / "lexicon-4096.json"
    lex_csv_path = data_dir / "lexicon-4096.csv"

    print("Generating forms-64.json ...")
    write_forms_json(forms_json_path)
    print("Generating forms-64.csv ...")
    write_forms_csv(forms_csv_path)
    print("Generating lexicon-4096.json ...")
    write_lexicon_json(lex_json_path)
    print("Generating lexicon-4096.csv ...")
    write_lexicon_csv(lex_csv_path)

    print("Done.")
    print("Written:")
    print(" -", forms_json_path)
    print(" -", forms_csv_path)
    print(" -", lex_json_path)
    print(" -", lex_csv_path)


if __name__ == "__main__":
    main()
