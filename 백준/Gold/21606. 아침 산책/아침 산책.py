import sys
input = sys.stdin.readline

vertex_count = int(input())
road_list = list(input().strip())
tree_list = [[]for _ in range(vertex_count+1)]
for _ in range(vertex_count - 1):
    a, b = map(int, input().split())
    tree_list[a].append(b)
    tree_list[b].append(a)


def dfs(tree_list, start):
    global count
    visited_list[start] = True
    for i in tree_list[start]:
        if visited_list[i] == False:
            if road_list[i-1] == '1':
                count += 1
                continue
            visited_list[i] = True
            dfs(tree_list, i)


count = 0
for start in range(vertex_count):
    if road_list[start] == '1':
        visited_list = [False] * (vertex_count+1)
        dfs(tree_list, start+1)

print(count)