import sys
from collections import deque
import heapq
input = sys.stdin.readline

maze_list = []

n = int(input())
for _ in range(n):
    maze_list.append(list(input().strip()))

def dijkstra(start_city, end_city):
    min_distance_list = [[float('inf')]*n for _ in range(n)]
    min_distance_list[start_city[0]][start_city[1]] = 0
    heap_list = [(0, start_city)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while heap_list:
        current_cost, current_city = heapq.heappop(heap_list)
        if current_cost > min_distance_list[current_city[0]][current_city[1]]:
            continue
        for i in range(4):
            nx = current_city[0] + dx[i]
            ny = current_city[1] + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if maze_list[nx][ny] == '1':
                    cost = 0
                else:
                    cost = 1
                new_cost = min_distance_list[current_city[0]][current_city[1]] + cost
                if new_cost < min_distance_list[nx][ny]:
                    min_distance_list[nx][ny] = new_cost
                    heapq.heappush(heap_list, (new_cost, [nx, ny]))

    print(min_distance_list[end_city[0]][end_city[1]])

dijkstra([0, 0], [n-1, n-1])
