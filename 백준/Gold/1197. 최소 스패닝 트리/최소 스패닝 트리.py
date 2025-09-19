import sys
input = sys.stdin.readline

vertex_count, edge_count = map(int, input().split())

parent = {}
adjacency_list = []

for i in range(1, vertex_count + 1):
    parent[i] = i

for _ in range(edge_count):
    adjacency_list.append(list(map(int, input().split())))

adjacency_list.sort(key=lambda x : x[2])

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

sum_cost = 0
count = 0
for i in range(len(adjacency_list)):
    if count == vertex_count - 1:
        break
    if find(adjacency_list[i][0]) == find(adjacency_list[i][1]):
        continue
    else:
        union(adjacency_list[i][0], adjacency_list[i][1])
        sum_cost += adjacency_list[i][2]
        count += 1

print(sum_cost)
