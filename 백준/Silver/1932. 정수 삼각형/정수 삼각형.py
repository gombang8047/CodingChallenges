import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

n = int(input())

lst = []
dp = [[-1] * n for _ in range(n)]
result = []

for _ in range(n):
    lst.append(list(map(int, input().split())))

def triangle(x, y):

    if y < 0 or y > x:
        return 0

    if x == 0:
        return lst[0][0]
    
    if dp[x][y] != -1:
        return dp[x][y]

    left = triangle(x-1, y-1)
    right = triangle(x-1, y)

    dp[x][y] = lst[x][y] + max(left, right)

    return dp[x][y]

for i in range(n):
    result.append(triangle(n-1, i))

print(max(result))