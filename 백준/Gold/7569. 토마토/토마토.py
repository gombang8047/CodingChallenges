import sys
from collections import deque
input = sys.stdin.readline

row, col, box_count = map(int, input().split())

all_box = [[]for _ in range(box_count)]
for i in range(box_count):
    for _ in range(col):
        all_box[i].append(list(map(int,input().split())))

def bfs():

    queue_list = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dz = [-1, 1]
    count = 0
    result = 0
    for k in range(box_count):
        for j in range(col):
            for i in range(row):
                if all_box[k][j][i] == 1:
                    queue_list.append([k, j, i, count])
    
    while queue_list:
        pop_z, pop_y, pop_x, count = queue_list.popleft()

        if result < count:
            result = count

        for i in range(2):
            nz = pop_z + dz[i]
            if 0<=nz<box_count:
                if all_box[nz][pop_y][pop_x] == 0:
                    all_box[nz][pop_y][pop_x] = 1
                    queue_list.append([nz, pop_y, pop_x, count+1])

        for i in range(4):
            nx = pop_x + dx[i]
            ny = pop_y + dy[i]
            if 0<=nx<row and 0<=ny<col:
                if all_box[pop_z][ny][nx] == 0:
                    all_box[pop_z][ny][nx] = 1
                    queue_list.append([pop_z, ny, nx, count+1])
    
    zero_exist = False
    for k in range(box_count):
        for j in range(col):
            for i in range(row):
                if all_box[k][j][i] == 0:
                    zero_exist = True
                    break
    if zero_exist == False:
        print(count)
    else:
        print(-1)

bfs()