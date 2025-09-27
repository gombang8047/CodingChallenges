import sys
input = sys.stdin.readline

item_count, target_weight = map(int, input().split())

dp = [[0] * (item_count+1) for _ in range(target_weight+1)]

def max_cost(item_pointer, target_weight):

    if target_weight <= 0 or item_pointer >= item_count:
        return 0

    if dp[target_weight][item_pointer] != 0:
        return dp[target_weight][item_pointer]
    
    if target_weight >= item_list[item_pointer][0]:
        dp[target_weight][item_pointer] = max(max_cost(item_pointer+1, target_weight-item_list[item_pointer][0]) + item_list[item_pointer][1], max_cost(item_pointer+1, target_weight))

    return dp[target_weight][item_pointer]

item_list = []
for _ in range(item_count):
    item_weight, item_cost = map(int, input().split())
    item_list.append([item_weight, item_cost])

item_list.sort(key=lambda x: x[0])

print(max_cost(0, target_weight))