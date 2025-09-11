import sys
input = sys.stdin.readline

def binary_search(inputVal, target, start, end):

    middle = (start + end) // 2

    if start > end:
        return 0
    if target == inputVal[middle]:
        return 1
    elif target > inputVal[middle]:
        start = middle + 1
        return binary_search(inputVal, target, start, end)
    elif target < inputVal[middle]:
        end = middle - 1
        return binary_search(inputVal, target, start, end)
    

n = int(input())
inputVal1 = list(map(int, input().split()))
inputVal1.sort()

m = int(input())
inputVal2 = list(map(int, input().split()))

for i in range(m):
    print(binary_search(inputVal1, inputVal2[i], 0, len(inputVal1)-1))