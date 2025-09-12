import sys
input = sys.stdin.readline

def tree_height_search(inputVal, target, start, end):

    while True:

        inputVal2 = inputVal[:]

        middle = (start + end) // 2

        for i in range(len(inputVal2)):
            if inputVal2[i] - middle <= 0:
                inputVal2[i] = 0
            else:
                inputVal2[i] -= middle

        if start > end:
            break
        elif target > sum(inputVal2):
            end = middle - 1
        elif target <= sum(inputVal2):
            start = middle + 1
            total_tree_height.append(middle)

n, m = map(int, input().split())

tree_height = list(map(int, input().split()))

total_tree_height = []

tree_height_search(tree_height, m, 0, max(tree_height))

print(max(total_tree_height))
