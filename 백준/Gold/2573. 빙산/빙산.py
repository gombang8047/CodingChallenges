import sys
input = sys.stdin.readline

n, m = map(int, input().split())

inputMap = []

for _ in range(n):
    inputMap.append(list(map(int, input().split())))

def iceberg():

    year = 0

    while True:
        stack = []       
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visited_list = [[False] * m for _ in range(n)]
        non_zero_count = 0
        visited_count = 0
        all_zero_flag = False

        for i in range(n):
            for j in range(m):
                if inputMap[i][j] != 0:
                    visited_list[i][j] = True
                    all_zero_flag = True
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]

                        if 0<=nx<n and 0<=ny<m:
                            if inputMap[nx][ny] == 0 and visited_list[nx][ny] == False:
                                if inputMap[i][j] > 0:
                                    inputMap[i][j] -= 1

                    if inputMap[i][j] != 0:
                        if not stack:
                            stack.append([i, j])
                        non_zero_count += 1
        if all_zero_flag == False:
            print(0)
            break

        visited_list = [[False] * m for _ in range(n)]

        while stack:
            pop_x, pop_y = stack.pop()

            for k in range(4):
                nx = pop_x + dx[k]
                ny = pop_y + dy[k]
                if 0<=nx<n and 0<=ny<m:
                    if inputMap[nx][ny] != 0:
                        if visited_list[nx][ny] == False:
                            stack.append([nx, ny])
                            visited_list[nx][ny] = True
                            visited_count += 1

        year += 1
        
        if visited_count != non_zero_count:
            print(year)
            break

iceberg()


