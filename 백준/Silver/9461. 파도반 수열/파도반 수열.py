import sys
input = sys.stdin.readline

def calculate(n):
    dp = [1,1,1,2,2]

    for i in range(5, n+1):
        dp.append(dp[i-1] + dp[i-5])

    return dp[n-1]

T = int(input())

for _ in range(T):
    n = int(input())

    print(calculate(n))

