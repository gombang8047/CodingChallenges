import sys
sys.setrecursionlimit(10**6)

def safe_area(x, y, ground, height):

    global count

    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and ground[nx][ny] > height:
                safe_area(nx, ny, ground, height)


N = int(input())

ground = []
fin = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(N):
    ground.append(list(map(int, input().split())))

for height in range(max(max(i) for i in ground)):
    count = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if ground[i][j] <= height:
                visited[i][j] = True

    for i in range(N):
        for j in range(N):
            if ground[i][j] > height and not visited[i][j]:
                safe_area(i, j, ground, height)
                count += 1

    fin.append(count)

print(max(fin))