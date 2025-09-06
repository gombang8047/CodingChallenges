import sys

input = sys.stdin.readline

def hanoi(start, end, other, n):

    if n == 1:
        print(f"{start} {end}")
        return
    
    hanoi(start, other, end, n-1)
    print(f"{start} {end}")
    hanoi(other, end, start, n-1)

N = int(input())

if N <= 20:
    print(( 2 ** N ) - 1)

    hanoi(1, 3, 2, N)
else:
    print(( 2 ** N ) - 1)
