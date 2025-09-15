import sys
from collections import deque
input = sys.stdin.readline

zero_list = deque()

k = int(input())
for _ in range(k):
    inputVal = int(input())

    if inputVal == 0:
        zero_list.pop()

    else:
        zero_list.append(inputVal)

print(sum(zero_list))