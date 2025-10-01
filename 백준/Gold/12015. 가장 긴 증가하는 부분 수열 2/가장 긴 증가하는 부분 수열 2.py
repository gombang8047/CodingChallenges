import sys
input = sys.stdin.readline

N = int(input())
inputVal = list(map(int, input().split()))

def lis(inputVal):

    i = 0
    lis_result = []

    while i < len(inputVal):
        if not lis_result:
            lis_result.append(inputVal[i])
            i += 1
        elif inputVal[i] > lis_result[-1]:
            lis_result.append(inputVal[i])
            i += 1
        else:
            binary_search(lis_result, inputVal[i], 0, len(lis_result))
            i += 1

    print(len(lis_result))

def binary_search(inputVal, target, start, end):
    
    while start <= end:

        mid  = (start + end) // 2

        if inputVal[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    inputVal[start] = target

lis(inputVal)