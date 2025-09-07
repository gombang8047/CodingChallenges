def Z(N, r, c):
    global fin

    if N == 0:
        return

    if r <= 2 ** (N-1) -1 and c <= 2 ** (N-1) -1 :
        count = 0
        fin += 2**(2*N-2) * count
        if r > 2**(N-1) -1:
            r = r - 2**(N-1)
        if c > 2**(N-1) -1:
            c = c - 2**(N-1)
        Z(N-1, r, c)
    elif r <= 2 ** (N-1) -1 and c > 2 ** (N-1) -1 :
        count = 1
        fin += 2**(2*N-2) * count
        if r > 2**(N-1) -1:
            r = r - 2**(N-1)
        if c > 2**(N-1) -1:
            c = c - 2**(N-1)
        Z(N-1, r, c)
    elif r > 2 ** (N-1) -1 and c <= 2 ** (N-1) -1 :
        count = 2
        fin += 2**(2*N-2) * count
        if r > 2**(N-1) -1:
            r = r - 2**(N-1)
        if c > 2**(N-1) -1:
            c = c - 2**(N-1)        
        Z(N-1, r, c)
    elif r > 2 ** (N-1) -1 and c > 2 ** (N-1) -1 :
        count = 3
        fin += 2**(2*N-2) * count
        if r > 2**(N-1) -1:
            r = r - 2**(N-1)
        if c > 2**(N-1) -1:
            c = c - 2**(N-1)
        Z(N-1, r, c)

N, r, c = map(int, input().split())

fin = 0

Z(N, r, c)

print(fin)