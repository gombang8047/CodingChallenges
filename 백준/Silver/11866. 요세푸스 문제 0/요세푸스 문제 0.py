import sys
input = sys.stdin.readline

n, k = map(int, input().split())

inputVal_list = []
result = []

for i in range(n):
    inputVal_list.append(i + 1)

while len(inputVal_list) != 0:
    if len(inputVal_list) > k:
        inputVal_list = inputVal_list[k-1:] + inputVal_list[:k-1]
        result.append(inputVal_list.pop(0))
    else:
        remain = (k-1) % len(inputVal_list)
        result.append(inputVal_list.pop(remain))
        inputVal_list = inputVal_list[remain:] + inputVal_list[:remain]

print(f"<{', '.join(map(str, result))}>")

