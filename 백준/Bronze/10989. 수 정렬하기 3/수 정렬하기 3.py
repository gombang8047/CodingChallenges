import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
lst = [0] * (10001)

for _ in range(N):
    num = int(input())
    lst[num] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        for _ in range(lst[i]): 
            print(f"{i}\n")