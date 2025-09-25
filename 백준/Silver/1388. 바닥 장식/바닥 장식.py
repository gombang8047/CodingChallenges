import sys
input = sys.stdin.readline

n, m = map(int, input().split())

map_list = []

for _ in range(n):
    map_list.append(list(map(str, input().strip())))
    
result = []

for i in range(n):
    count = 0
    for j in range(m):
        if map_list[i][j] == '-':
            if j == m-1:
                count += 1
            if j+1 < m :
                if map_list[i][j+1] == '|':
                    count += 1
    result.append(count)

for i in range(m):
    count = 0
    for j in range(n):
        if map_list[j][i] == '|':
            if j == n-1:
                count += 1
            if j+1 < n :
                if map_list[j+1][i] == '-':
                    count += 1
    result.append(count)
    
print(sum(result))