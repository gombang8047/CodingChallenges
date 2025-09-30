import sys
input = sys.stdin.readline

n = int(input())

cost_list = []

for _ in range(n):
    cost_list.append(list(map(int, input().split())))

dp = [[-1] * (1<<n) for _ in range(n+1)]

def min_cost(target, city):
    
    if dp[target][city] != -1:
        return dp[target][city]
    
    if city == (1<<n)-1 and cost_list[target][0] != 0:
        return cost_list[target][0]

    tmp = float('inf')
    for i in range(n):
        if cost_list[target][i] != 0 and (city & 1<<(n-i-1))==0:
            tmp = min(tmp, min_cost(i, city|1<<(n-i-1)) + cost_list[target][i])
    dp[target][city] = tmp

    return dp[target][city]


print(min_cost(0, (1<<n-1)))