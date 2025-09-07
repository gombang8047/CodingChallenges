import sys

input = sys.stdin.readline

N = int(input())
k = [0]*(10000+1)

for _ in range(N):
    k[int(input())] += 1

for i in range(len(k)):
    if k[i] != 0:
        for _ in range(k[i]):
            sys.stdout.write(str(i) + "\n")