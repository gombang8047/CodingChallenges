import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

def virus(x, y):
    queue_list = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    count = 0

    for i in range(n):
        for j in range(n):
            if map_list[i][j] != 0:
                queue_list.append([i, j])
    
    queue_list = deque(sorted(queue_list, key=lambda x : map_list[x[0]][x[1]]))
    time_counter = 0
    closing_time_counter = len(queue_list)
    while queue_list:
        time_counter += 1
        pop_x, pop_y = queue_list.popleft()

        for k in range(4):
            nx = pop_x + dx[k]
            ny = pop_y + dy[k]

            if 0<=nx< n and 0<=ny<n:
                if map_list[nx][ny] == 0:
                    map_list[nx][ny] = map_list[pop_x][pop_y]
                    queue_list.append([nx, ny])


        if time_counter == closing_time_counter:
            count += 1
            time_counter = 0
            closing_time_counter = len(queue_list)
        
        if count == s:
            break

    print(map_list[x-1][y-1])

virus(x, y)