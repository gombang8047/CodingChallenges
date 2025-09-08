import sys

N = int(input())
a = []

for i in range(N):
    a.append(int(sys.stdin.readline().strip()))

a.sort()
for i in range(N):
    sys.stdout.write(str(a[i]) + "\n")
