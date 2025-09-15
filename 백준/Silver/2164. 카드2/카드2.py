import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

result = deque()

for i in range(1, n+1):
    result.append(i)

def find_last_card(n, inputVal):

    while n > 1:
        if inputVal:
            inputVal.popleft()
            inputVal.append(inputVal.popleft())
            n -= 1
    print(inputVal[0])


find_last_card(n, result)
