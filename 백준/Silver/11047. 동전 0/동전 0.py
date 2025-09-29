import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

count = 0
for i in range(len(coin_list)-1, -1, -1):
    if k == 0:
        break
    elif k >= coin_list[i]:
        count = count + (k // coin_list[i])
        k = k % coin_list[i]

print(count)