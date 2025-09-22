import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
vertex_count = int(input())

tree_list = [[]for _ in range(vertex_count+1)]
for _ in range(vertex_count-1):
    a, b = map(int, input().split())
    tree_list[a].append(b)
    tree_list[b].append(a)

visited_list = [False] * (vertex_count + 1)
visited_list[0] = True
visited_list[1] = True
result = [[]for _ in range(vertex_count+1)]

def dfs(tree_list, start_vertex):
    for i in tree_list[start_vertex]:
        if visited_list[i] == False:
            visited_list[i] = True
            result[i] = start_vertex
            dfs(tree_list, i)

dfs(tree_list, 1)

print("\n".join(map(str, result[2:])))

