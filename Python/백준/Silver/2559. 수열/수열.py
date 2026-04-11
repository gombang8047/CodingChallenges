import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lst = list(map(int, input().split()))
result = []
first = 0

for i in range(k):
    first += lst[i]
result.append(first)

for j in range(1, n-k+1):
    result.append(result[j-1] + lst[j+k-1] - lst[j-1])

print(max(result))