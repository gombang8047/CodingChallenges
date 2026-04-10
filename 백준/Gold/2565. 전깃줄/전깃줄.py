import sys
input = sys.stdin.readline

n = int(input())
lst = []
dp = [[-1] * (n+1) for _ in range(n+1)]
for _ in range(n):
    lst.append(list(map(int, input().split())))

lst = sorted(lst)

def LIS(curPos, lastIdx):
    
    if curPos == n:
        return 0
    
    if dp[curPos][lastIdx+1] != -1:
        return dp[curPos][lastIdx+1]
    
    res = LIS(curPos+1, lastIdx)
    
    if lastIdx == -1 or lst[lastIdx][1] < lst[curPos][1]:
        res = max(1 + LIS(curPos+1, curPos), res)
    
    dp[curPos][lastIdx+1] = res

    return res


print(n - LIS(0, -1))
