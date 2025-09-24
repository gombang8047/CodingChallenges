import sys
input = sys.stdin.readline

result_count = 0

vertex_count, edge_count = map(int, input().split())

adjacency_list = [[float('inf')] * vertex_count for _ in range(vertex_count)]

for i in range(vertex_count):
    adjacency_list[i][i] = 0

for _ in range(edge_count):
    a, b = map(int, input().split())
    adjacency_list[a-1][b-1] = 1

for node in range(vertex_count):
    for i in range(vertex_count):
        for j in range(vertex_count):
            adjacency_list[i][j] = min(adjacency_list[i][j], adjacency_list[i][node] + adjacency_list[node][j])

for i in range(vertex_count):
    count_row = 0
    count_col = 0
    
    for j in range(vertex_count):
        if 0 < adjacency_list[i][j] < float('inf'):
            count_row += 1
        if 0 < adjacency_list[j][i] < float('inf'):
            count_col += 1
    if count_row > vertex_count//2:
        result_count += 1
    if count_col > vertex_count//2:
        result_count += 1    

print(result_count)
        