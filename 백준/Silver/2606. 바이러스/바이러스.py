import sys
from collections import deque
input = sys.stdin.readline

vertex_count = int(input())
edge_count = int(input())
tree = {}

for _ in range(edge_count):
    a, b = map(int, input().split())
    if a not in tree:
        tree[a] = []
    tree[a].append(b)
    if b not in tree:
        tree[b] = []
    tree[b].append(a)

def bfs(vertex):
    used_vertex = [False] * (vertex_count+1)
    used_vertex[vertex] = True
    queue_list = deque([vertex])
    virus_count = 0

    while queue_list:
        tmp = queue_list.popleft()
        if tmp in tree:
            for i in range(len(tree[tmp])):
                if used_vertex[tree[tmp][i]] == False:
                    queue_list.append(tree[tmp][i])
                    virus_count += 1
                    used_vertex[tree[tmp][i]] = True
    print(virus_count)

bfs(1)