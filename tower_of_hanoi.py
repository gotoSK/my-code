def toh(S, T, A, n): # source, target, auziliary, disc no.
    if n == 1:
        print(f"Disc{n}: {S} -> {T}")
        return
    toh(S, A, T, n-1)
    print(f"Disc{n}: {S} -> {T}")
    toh(A, T, S, n-1)