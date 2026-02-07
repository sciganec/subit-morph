# utils.py
# Utility functions for SUBIT‑morph processing

def read_bytes(path: str) -> bytes:
    """
    Read a file as raw bytes.
    """
    with open(path, "rb") as f:
        return f.read()


def chunk_bits(bits: str, size: int):
    """
    Yield non‑overlapping bit chunks of given size.
    Used for debugging or visualization, not for SUBIT windows.
    """
    for i in range(0, len(bits), size):
        yield bits[i:i+size]


def format_vector(vec, precision=6):
    """
    Format a numeric vector into a fixed‑width string list.
    """
    return "[" + ", ".join(f"{v:.{precision}f}" for v in vec) + "]"


def format_grid(grid, precision=6):
    """
    Format an 8×8 grid into aligned text rows.
    """
    lines = []
    for row in grid:
        line = " ".join(f"{v:.{precision}f}" for v in row)
        lines.append(line)
    return "\n".join(lines)


def save_text(path: str, text: str):
    """
    Save text to a file.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
