import sys
from collections import deque
input = sys.stdin.readline

vertex_count, edge_count, target_distance, start_vertex = map(int, input().split())

edge_direct = {}

for _ in range(edge_count):
    a, b = map(int, input().split())
    if a not in edge_direct:
        edge_direct[a] = []
    if b not in edge_direct:
        edge_direct[b] = []
    edge_direct[a].append(b)

def bfs(vertex):
    used_vertex = [False] * (vertex_count+1)
    used_vertex[vertex] = True
    queue_list = deque([[vertex, 0]])
    result = []

    while queue_list:
        tmp = queue_list.popleft()
        if tmp[1] == target_distance:
            result.append(tmp[0])
        for i in range(len(edge_direct[tmp[0]])):
            if used_vertex[edge_direct[tmp[0]][i]] == False:
                queue_list.append([edge_direct[tmp[0]][i], tmp[1] + 1])
                used_vertex[edge_direct[tmp[0]][i]] = True
    
    if result:
        result.sort()
        print("\n".join(map(str, result)))
    else:
        print(-1)

bfs(start_vertex)