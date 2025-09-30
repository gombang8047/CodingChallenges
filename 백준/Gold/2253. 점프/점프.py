import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

target, m = map(int, input().split())
small_rock = [True] * (target+1)
for _ in range(m):
    small_rock[int(input())] = False

dp = [[-1] * (int((2 * target) ** 0.5) + 2) for _ in range(target+1)]

def jump(cur_p, cur_val):

    if dp[cur_p][cur_val] != -1:
        return dp[cur_p][cur_val]
    
    if cur_p == target:
        return 0

    jump_size = [cur_val-1, cur_val, cur_val+1]

    tmp = float('inf')
    for i in range(3):
        tmp_pt = cur_p + jump_size[i]
        if tmp_pt <= target:
            if jump_size[i] > 0 and small_rock[tmp_pt] == True:
                tmp = min(tmp, jump(tmp_pt, jump_size[i])+1)
    dp[cur_p][cur_val] = tmp

    return dp[cur_p][cur_val]


k = jump(1, 0)

if k == float('inf'):
    print(-1)
else:
    print(k)
