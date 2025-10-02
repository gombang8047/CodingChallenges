import sys
input = sys.stdin.readline

map_list = []

n = int(input())
for _ in range(n):
    map_list.append(list(map(int, input().split())))

dp = [[-1] * (n+1) for _ in range(n+1)]

def jump(cur_x, cur_y):

    if cur_x == n-1 and cur_y == n-1:
        return 0
    
    if map_list[cur_y][cur_x] == 0:
        return float('inf')

    if dp[cur_x][cur_y] != -1:
        return dp[cur_x][cur_y]
    
    dx = [map_list[cur_y][cur_x], 0]
    dy = [0, map_list[cur_y][cur_x]]

    for i in range(2):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if nx < n and ny < n:
            tmp = jump(nx, ny)
            if tmp != float('inf'):
                dp[cur_x][cur_y] += (tmp + 1)
    
    return dp[cur_x][cur_y]

result = jump(0, 0)

if result != -1 and result != float('inf'):
    print(result + 1)
else:
    print(0)
