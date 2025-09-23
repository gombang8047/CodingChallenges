import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
map_list = []

for _ in range(r):
    map_list.append(list(map(str, input().strip())))

def bfs():
    queue_hedgehog = deque()
    queue_water = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    safe = False

    for j in range(r):
        for i in range(c):
            if map_list[j][i] == 'S':
                queue_hedgehog.append([j, i, 1])
            if map_list[j][i] == '*':
                queue_water.append([j, i])

    while queue_hedgehog or queue_water:
        wave = len(queue_water)
        for _ in range(wave):
            pop_water_y, pop_water_x = queue_water.popleft()
            for i in range(4):
                ny_water, nx_water = pop_water_y + dy[i], pop_water_x + dx[i]
                if 0<=ny_water<r and 0<=nx_water<c:
                    if map_list[ny_water][nx_water] == '.':
                        map_list[ny_water][nx_water] = '*'
                        queue_water.append([ny_water, nx_water])
        
        wave_hedgehog = len(queue_hedgehog)
        for _ in range(wave_hedgehog):
            if queue_hedgehog:
                pop_hedgehog_y, pop_hedgehog_x, count  = queue_hedgehog.popleft()
                for i in range(4):
                    ny_hedgehog, nx_hedgehog = pop_hedgehog_y + dy[i], pop_hedgehog_x + dx[i]
                    if 0<=ny_hedgehog<r and 0<=nx_hedgehog<c:
                        if map_list[ny_hedgehog][nx_hedgehog] == 'D':
                            safe = True
                            print(count)
                            break
                        if map_list[ny_hedgehog][nx_hedgehog] == '.':
                            map_list[ny_hedgehog][nx_hedgehog] = 'S'
                            queue_hedgehog.append([ny_hedgehog, nx_hedgehog, count+1])
                else:
                    continue
                break
        else:
            continue
        break

    if safe == False:
        print('KAKTUS')

bfs()
    
