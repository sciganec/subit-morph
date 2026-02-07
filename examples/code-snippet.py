def subit_morph(byte_stream: bytes) -> dict:
    """
    Compute a 64-state SUBIT-morph from a byte stream.
    Returns:
        {
            "counts": [64 ints],
            "freqs": [64 floats],
            "grid": [[8x8 floats]],
        }
    """
    # 1. bytes → bitstring
    bits = "".join(f"{b:08b}" for b in byte_stream)
    n = len(bits)
    if n < 6:
        raise ValueError("Stream too short for 6-bit windows")

    # 2. sliding 6-bit windows
    counts = [0] * 64
    for i in range(n - 5):
        window = bits[i:i+6]
        k = int(window, 2)
        counts[k] += 1

    total = sum(counts)
    freqs = [c / total for c in counts]

    # 3. 8×8 grid
    grid = [[0.0 for _ in range(8)] for _ in range(8)]
    for k, p in enumerate(freqs):
        row = k // 8
        col = k % 8
        grid[row][col] = p

    return {
        "counts": counts,
        "freqs": freqs,
        "grid": grid,
    }


if __name__ == "__main__":
    # Example: compute SUBIT-morph for this file itself
    with open(__file__, "rb") as f:
        data = f.read()

    morph = subit_morph(data)
    print("64-state frequencies:")
    for i, p in enumerate(morph["freqs"]):
        print(f"{i:02d}: {p:.6f}")
