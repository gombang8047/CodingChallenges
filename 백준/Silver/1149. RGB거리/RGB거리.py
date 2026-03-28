import sys
input = sys.stdin.readline

n = int(input())
lst = []

for j in range(n):
    lst.append(list(map(int, input().split())))

dp = [[0] * 3  for _ in range(n)]

for i in range(0,n):
    for j in range(3):
        dp[i][j] = lst[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))