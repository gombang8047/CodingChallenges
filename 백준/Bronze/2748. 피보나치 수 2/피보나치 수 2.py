import sys
input = sys.stdin.readline

dp = [0, 1]

n = int(input())

def fibo(n):

    for i in range(n-1):
        dp.append(dp[i] + dp[i+1])

    print(dp[n])

fibo(n)