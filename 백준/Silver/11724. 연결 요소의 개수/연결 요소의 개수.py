import sys
from collections import deque
input = sys.stdin.readline

vertex_count, edge_count = map(int, input().split())
tree = {}

for _ in range(edge_count):
    a, b = map(int, input().split())
    if a not in tree:
        tree[a] = []
    tree[a].append(b)
    if b not in tree:
        tree[b] = []
    tree[b].append(a)

def bfs():
    used_vertex = [False] * (vertex_count+1)
    used_vertex[0] = True
    queue_list = deque()
    count = 0
    
    for k in range(len(used_vertex)):
        if used_vertex[k] == False:    
            used_vertex[k] = True
            queue_list.append(k)
            while queue_list:
                tmp = queue_list.popleft()
                if tmp in tree:
                    for i in range(len(tree[tmp])):
                        if used_vertex[tree[tmp][i]] == False:
                            queue_list.append(tree[tmp][i])
                            used_vertex[tree[tmp][i]] = True
            count += 1
    
    print(count)


bfs()