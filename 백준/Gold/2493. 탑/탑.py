import sys
input = sys.stdin.readline

n = int(input())
inputVal_list = list(map(int, input().split()))
result = []
index_high_top = []

i = 0
while i < len(inputVal_list):

    if not index_high_top:
        result.append(0)
        index_high_top.append(i)
    
    else:
        if inputVal_list[i] > inputVal_list[index_high_top[-1]]:
            while index_high_top and inputVal_list[i] > inputVal_list[index_high_top[-1]]:
                index_high_top.pop()
            if not index_high_top:
                result.append(0)
            else:
                result.append(index_high_top[-1] + 1)
            index_high_top.append(i)

        elif inputVal_list[i] < inputVal_list[index_high_top[-1]]:
            result.append(index_high_top[-1] + 1)
            index_high_top.append(i)
    
    i+=1

print(*result)