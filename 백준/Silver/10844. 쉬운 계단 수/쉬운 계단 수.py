import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

n = int(input())

dp = [[-1] * (10) for _ in range(n+1)] 

result = []

def stair(x, y):

    if x == 1 and y != 0:
        return 1
    elif x == 1 and y == 0:
        return 0
    
    if dp[x][y] != -1:
        return dp[x][y]
    
    if y == 0:
        dp[x][y] = stair(x-1, y+1)
    elif y == 9:
        dp[x][y] = stair(x-1, y-1)
    else:
        dp[x][y] = stair(x-1, y-1) + stair(x-1, y+1)

    return dp[x][y]

for i in range(10):
    result.append(stair(n,i))

print(sum(result) % 1000000000)