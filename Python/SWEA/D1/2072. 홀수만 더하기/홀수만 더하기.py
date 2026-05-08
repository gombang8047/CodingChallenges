


T = int(input())
lst = []
result = [0] * T

for _ in range(T):
    lst.append(list(map(int, input().split())))

for i in range(T):
    for j in range(10):
        if lst[i][j] % 2 == 1:
            result[i] += lst[i][j]
        else:
            continue

for i in range(T):
    print(f"#{i+1} {result[i]}")