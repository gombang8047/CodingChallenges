import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
lst = []
dp  = [[-1] * 3 for _ in range(n)]

for _ in range(n):
    lst.append(int(input()))

def wein(x, count):
    
    if x >= n:
        return 0
    
    if dp[x][count] != -1:
        return dp[x][count]
    
    no = wein(x+1, 0)
    yes = -1
    if count < 2:
        yes = lst[x] + wein(x+1, count+1)

    dp[x][count] = max(no, yes)

    return dp[x][count]

print(wein(0,0))