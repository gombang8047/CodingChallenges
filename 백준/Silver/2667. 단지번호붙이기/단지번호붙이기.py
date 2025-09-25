import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

map_list = []

for _ in range(n):
    map_list.append(list(map(int, input().strip())))

def search_apt():

    visited_list = [[False] * n for _ in range(n)]
    queue_list = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = []

    for i in range(n):
        for j in range(n):
            if map_list[i][j] == 1 and visited_list[i][j] == False:
                queue_list.append([i, j])
                visited_list[i][j] = True
                count = 0

                while queue_list:
                    pop_x, pop_y = queue_list.popleft()
                    count += 1

                    for k in range(4):
                        nx = pop_x + dx[k]
                        ny = pop_y + dy[k]

                        if 0<=nx< n and 0<=ny<n:
                            if map_list[nx][ny] == 1 and visited_list[nx][ny] == False:
                                visited_list[nx][ny] = True
                                queue_list.append([nx, ny])

                result.append(count)
    
    result.sort()
    print(len(result))
    print("\n".join(map(str, result)))

search_apt()


