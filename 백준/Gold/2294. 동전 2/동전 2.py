import sys
from collections import deque
input = sys.stdin.readline
 
n, target_cost = map(int, input().split())

coin_cost = []

for _ in range(n):
    coin_cost.append(int(input()))

def min_coin(target_cost):
    queue_list = deque([[target_cost, 1]])
    exist = False
    visited_list = [False] * (target_cost+1)

    while queue_list:

        pop_tmp, count = queue_list.popleft()

        for i in coin_cost:
            if pop_tmp - i == 0:
                exist = True
                print(count)
                break
            if pop_tmp - i > 0:
                if visited_list[pop_tmp-i] == False:
                    visited_list[pop_tmp-i] = True
                    queue_list.append([pop_tmp-i, count+1])
        else:
            continue
        break

    if exist == False:
        print(-1)
        
min_coin(target_cost)