import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

dp = deque([1, 2])

def tile(n):

    if n <= 2:
        print(dp[n-1])
    else:
        for _ in range(n-2):
            dp.append((dp[0] + dp[1]) % 15746)
            dp.popleft()
        
        print(dp[1])

tile(n)