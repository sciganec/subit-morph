# grid.py
# 8×8 grid construction for SUBIT‑morphs

def grid_from_freqs(freqs):
    """
    Convert a 64‑element frequency vector into an 8×8 grid.
    freqs: list of 64 floats
    returns: 8×8 nested list of floats
    """
    if len(freqs) != 64:
        raise ValueError("Expected 64 frequency values")

    grid = [[0.0 for _ in range(8)] for _ in range(8)]
    for k, p in enumerate(freqs):
        r = k // 8
        c = k % 8
        grid[r][c] = p
    return grid


def print_grid(grid):
    """
    Pretty‑print an 8×8 grid with fixed‑width formatting.
    """
    if len(grid) != 8 or any(len(row) != 8 for row in grid):
        raise ValueError("Grid must be 8×8")

    for row in grid:
        print(" ".join(f"{v:0.6f}" for v in row))
