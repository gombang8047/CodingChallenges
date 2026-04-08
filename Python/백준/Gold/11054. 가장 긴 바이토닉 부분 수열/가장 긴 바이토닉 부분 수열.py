import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

lst = list(map(int, input().split()))

dp = [[[-1] * (3) for _ in range(1001)] for _ in range(1001)]

def bitonic(curPos, lastIdx, isDescend):

    if curPos == n:
        return 0
    
    if dp[curPos][lastIdx][isDescend] != -1:
        return dp[curPos][lastIdx][isDescend]
    
    prev_val = lst[lastIdx] if lastIdx != -1 else -1

    if lst[curPos] > prev_val:
        if isDescend == 1:
            dp[curPos][lastIdx][isDescend] = bitonic(curPos+1, lastIdx, 1)
        else:
            dp[curPos][lastIdx][isDescend] = max(bitonic(curPos+1, curPos, 0) + 1, bitonic(curPos+1, lastIdx, 0))
    elif lst[curPos] < prev_val:
        dp[curPos][lastIdx][isDescend] = max(bitonic(curPos+1, curPos, 1) + 1, bitonic(curPos+1, lastIdx, isDescend))
    else:
        dp[curPos][lastIdx][isDescend] = bitonic(curPos+1, lastIdx, isDescend)

    return dp[curPos][lastIdx][isDescend]

print(bitonic(0, -1, 0))
    
