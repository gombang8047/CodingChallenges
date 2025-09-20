import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int,input().strip())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
queue_list = deque([[0, 0, 1]])
maze[0][0] = 0


min_cycle = []
while queue_list:

    tmp = queue_list.popleft()

    if tmp[0] == n-1 and tmp[1] == m-1:
        print(tmp[2])
        break
    
    for i in range(4):
        nx = tmp[0] + dx[i]
        ny = tmp[1] + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if maze[nx][ny] == 1:
                maze[nx][ny] = 0
                queue_list.append([nx, ny, tmp[2] + 1])

