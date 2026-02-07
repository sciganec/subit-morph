# subit.py
# Reference implementation of the SUBIT‑morph algorithm

import math


def bytes_to_bits(data: bytes) -> str:
    return "".join(f"{b:08b}" for b in data)


def sliding_windows_6(bits: str):
    n = len(bits)
    if n < 6:
        return []
    for i in range(n - 5):
        yield bits[i:i+6]


def compute_counts(bits: str):
    counts = [0] * 64
    for w in sliding_windows_6(bits):
        k = int(w, 2)
        counts[k] += 1
    return counts


def normalize(counts):
    total = sum(counts)
    if total == 0:
        return [0.0] * 64
    return [c / total for c in counts]


def grid_from_freqs(freqs):
    grid = [[0.0 for _ in range(8)] for _ in range(8)]
    for k, p in enumerate(freqs):
        r = k // 8
        c = k % 8
        grid[r][c] = p
    return grid


def cube_coords(k):
    x = (k >> 4) & 0b11
    y = (k >> 2) & 0b11
    z = k & 0b11
    return (x, y, z)


def entropy(freqs):
    H = 0.0
    for p in freqs:
        if p > 0:
            H -= p * math.log(p, 2)
    return H / 6.0


def anisotropy(freqs):
    # mean vector
    mu = [0.0, 0.0, 0.0]
    for k, p in enumerate(freqs):
        x, y, z = cube_coords(k)
        mu[0] += p * x
        mu[1] += p * y
        mu[2] += p * z

    # covariance matrix
    C = [[0.0, 0.0, 0.0] for _ in range(3)]
    for k, p in enumerate(freqs):
        x, y, z = cube_coords(k)
        dx = x - mu[0]
        dy = y - mu[1]
        dz = z - mu[2]
        C[0][0] += p * dx * dx
        C[0][1] += p * dx * dy
        C[0][2] += p * dx * dz
        C[1][0] += p * dy * dx
        C[1][1] += p * dy * dy
        C[1][2] += p * dy * dz
        C[2][0] += p * dz * dx
        C[2][1] += p * dz * dy
        C[2][2] += p * dz * dz

    # eigenvalues of 3×3 covariance matrix
    # using a simple numeric method (Jacobi)
    def jacobi_eigen(M):
        A = [row[:] for row in M]
        for _ in range(50):
            # find largest off‑diag element
            a = 0
            p = 0
            q = 1
            for i in range(3):
                for j in range(i+1, 3):
                    if abs(A[i][j]) > a:
                        a = abs(A[i][j])
                        p, q = i, j
            if a < 1e-12:
                break
            phi = 0.5 * math.atan2(2*A[p][q], A[q][q] - A[p][p])
            c = math.cos(phi)
            s = math.sin(phi)

            # rotate
            App = c*c*A[p][p] - 2*s*c*A[p][q] + s*s*A[q][q]
            Aqq = s*s*A[p][p] + 2*s*c*A[p][q] + c*c*A[q][q]
            Apq = 0.0

            for k in range(3):
                if k != p and k != q:
                    Akp = c*A[k][p] - s*A[k][q]
                    Akq = s*A[k][p] + c*A[k][q]
                    A[k][p] = Akp
                    A[p][k] = Akp
                    A[k][q] = Akq
                    A[q][k] = Akq

            A[p][p] = App
            A[q][q] = Aqq
            A[p][q] = Apq
            A[q][p] = Apq

        return [A[0][0], A[1][1], A[2][2]]

    lambdas = sorted(jacobi_eigen(C), reverse=True)
    if lambdas[0] == 0:
        return 0.0
    return 1.0 - (lambdas[1] / lambdas[0])


def tension(freqs):
    # mean vector
    mu = [0.0, 0.0, 0.0]
    for k, p in enumerate(freqs):
        x, y, z = cube_coords(k)
        mu[0] += p * x
        mu[1] += p * y
        mu[2] += p * z

    # radial distances
    rs = []
    for k, p in enumerate(freqs):
        x, y, z = cube_coords(k)
        dx = x - mu[0]
        dy = y - mu[1]
        dz = z - mu[2]
        rs.append(math.sqrt(dx*dx + dy*dy + dz*dz))

    # std(r)
    mean_r = sum(rs) / len(rs)
    var_r = sum((r - mean_r)**2 for r in rs) / len(rs)
    std_r = math.sqrt(var_r)

    # std(p)
    mean_p = sum(freqs) / len(freqs)
    var_p = sum((p - mean_p)**2 for p in freqs) / len(freqs)
    std_p = math.sqrt(var_p)

    if std_p == 0:
        return 0.0
    return std_r / std_p


def subit_morph(data: bytes):
    bits = bytes_to_bits(data)
    counts = compute_counts(bits)
    freqs = normalize(counts)
    grid = grid_from_freqs(freqs)

    E = entropy(freqs)
    A = anisotropy(freqs)
    T = tension(freqs)

    return {
        "counts": counts,
        "freqs": freqs,
        "grid": grid,
        "E": E,
        "A": A,
        "T": T,
    }


if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    with open(path, "rb") as f:
        data = f.read()
    m = subit_morph(data)
    print("SUBIT‑address:", m["E"], m["A"], m["T"])
