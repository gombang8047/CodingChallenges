import sys
input = sys.stdin.readline

def search_coin(target, coin_list):

    dp = [0] * (target+1)

    dp[0] = 1

    for k in coin_list:
        for i in range(1, target+1):
            if i-k >= 0:
                dp[i] += dp[i-k]
    
    print(dp[target])


T = int(input())

for _ in range(T):
    n  = int(input())

    coin_list = list(map(int, input().split()))

    target = int(input())

    search_coin(target, coin_list)

