import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))
result = []
prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + lst[i]

for _ in range(m):
    a, b = map(int, input().split())
    result.append(prefix_sum[b] - prefix_sum[a-1])

print(*result, sep="\n")