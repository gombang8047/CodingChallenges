import sys
n = int(sys.stdin.readline())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    # 1. 기본적으로 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    
    # 2. 2로 나누어 떨어지는 경우 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
        
    # 3. 3으로 나누어 떨어지는 경우 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])