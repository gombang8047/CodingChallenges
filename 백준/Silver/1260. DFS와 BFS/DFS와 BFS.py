import sys
from collections import deque
input = sys.stdin.readline

vertex_count, edge_count, start_vertex = map(int, input().split())
tree = {}
used_vertex = [False] * (vertex_count+1)
dfs_list = []
bfs_list = []

for _ in range(edge_count):
    a, b = map(int, input().split())
    if a not in tree:
        tree[a] = []
    tree[a].append(b)
    if b not in tree:
        tree[b] = []
    tree[b].append(a)

for vertex in tree:
    tree[vertex].sort()

def dfs(vertex, used_vertex):

    if used_vertex[vertex] == True:
        return

    dfs_list.append(vertex)
    used_vertex[vertex] = True
    
    if vertex in tree:
        for i in range(len(tree[vertex])):
            if used_vertex[tree[vertex][i]] == False:
                dfs(tree[vertex][i], used_vertex)

def bfs(vertex):
    used_vertex = [False] * (vertex_count+1)
    used_vertex[vertex] = True
    queue_list = deque()
    queue_list.append(vertex)
    
    while queue_list:
        tmp = queue_list.popleft()
        bfs_list.append(tmp)
        if tmp in tree:
            for i in range(len(tree[tmp])):
                if used_vertex[tree[tmp][i]] == False:
                    queue_list.append(tree[tmp][i])
                    used_vertex[tree[tmp][i]] = True

dfs(start_vertex, used_vertex)
bfs(start_vertex)

print(*dfs_list)
print(*bfs_list)