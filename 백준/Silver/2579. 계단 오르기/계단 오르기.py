import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)

n = int(input())
lst = [0]
dp = [[-1] * (n+1) for _ in range(n+1)]

for _ in range(n):
    lst.append(int(input()))

def stairs(x, step_count):

    if x == 0:
        return 0

    if x <= -1 or step_count >= 3:
        return float('-inf')
    
    if dp[x][step_count] != -1:
        return dp[x][step_count]

    dp[x][step_count] = max(stairs(x-1, step_count+1), stairs(x-2, 1)) + lst[x]

    return dp[x][step_count]

print(stairs(n, 1))