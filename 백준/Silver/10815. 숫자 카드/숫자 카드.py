import sys
input = sys.stdin.readline

N = int(input())
a = set(map(int, input().split()))

M = int(input())
b = list(map(int, input().split()))

k = []

for n in b:
    if n in a:
        k.append("1")
    else:
        k.append("0")

sys.stdout.write(" ".join(k) + "\n")