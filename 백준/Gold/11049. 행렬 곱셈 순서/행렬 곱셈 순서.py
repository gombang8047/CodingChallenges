import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

n = int(input())
inputVal_list = []
for _ in range(n):
    r, c = map(int, input().split())
    inputVal_list.append([r, c])

dp = [[-1] * (len(inputVal_list)) for _ in range((len(inputVal_list)))]

def procession(start, end):

    if dp[start][end] != -1:
        return dp[start][end]

    if start == end:
        return 0
    
    output = float('inf')
    for mid in range(start, end):
        output = min(output, procession(start, mid) + procession(mid+1, end) + inputVal_list[start][0] * inputVal_list[mid][1] * inputVal_list[end][1])
    dp[start][end] = output

    return dp[start][end]

print(procession(0, len(inputVal_list)-1))
