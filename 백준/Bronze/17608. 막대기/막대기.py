import sys
input = sys.stdin.readline

n = int(input())

inputVal_list = []

for i in range(n):
    inputVal_list.append(int(input()))

inputVal_list = inputVal_list[::-1]

best = 0
count = 0

for i in range(len(inputVal_list)):
    if inputVal_list[i] > best:
        count += 1
        best = inputVal_list[i]

print(count)