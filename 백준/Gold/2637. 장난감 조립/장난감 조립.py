import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
tree_list = [[]for _ in range(n+1)]
tree_list[0] = float('inf')
memorization = [[0]*(n+1)for _ in range(n+1)]

for _ in range(m):
    x, y, k = map(int, input().split())
    tree_list[x].append([y, k])

def toy_make(start_vertex):

    if sum(memorization[start_vertex]) > 0:
        return

    if not tree_list[start_vertex]:
        memorization[start_vertex][start_vertex] = 1
        return

    for vertex, count in tree_list[start_vertex]:
        toy_make(vertex)

        for i in range(1, n+1):
            memorization[start_vertex][i] += count * memorization[vertex][i]


toy_make(n)

for i in range(len(memorization[n])):
    if memorization[n][i] != 0:
        print(i, memorization[n][i])


