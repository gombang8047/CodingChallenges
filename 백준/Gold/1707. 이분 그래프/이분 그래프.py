import sys
from collections import deque
input = sys.stdin.readline

k = int(input())

def bfs(tree_list):
    queue_list = deque()
    visited_list = [False] * (vertex_count + 1)
    team_list = [3777] * (vertex_count+1)
    yes_or_no = True

    for vertex in range(1, vertex_count+1):
        if visited_list[vertex] == False:
            queue_list.append(vertex)
            visited_list[vertex] = True
            team_list[vertex] = True
            while queue_list:
                pop_vertex = queue_list.popleft()
                for i in tree_list[pop_vertex]:
                    if (team_list[pop_vertex] == 1 and team_list[i] == 1) or (team_list[pop_vertex] == 0 and team_list[i] == 0):
                        yes_or_no = False
                        break
                    if visited_list[i] == False:
                        team_list[i] = 0 if team_list[pop_vertex] == 1 else 1
                        visited_list[i] = True
                        queue_list.append(i)
                else:
                    continue
                break

    if yes_or_no == True:
        print("YES")
    else:
        print("NO")

for _ in range(k):
    vertex_count, edge_count = map(int, input().split())
    tree_list = [[]for _ in range(vertex_count+1)]
    for _ in range(edge_count):
        u, v = map(int, input().split())
        tree_list[u].append(v)
        tree_list[v].append(u)

    bfs(tree_list)
