import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

inputVal = list(map(int, input().split()))

plug = [deque([]) for _ in range(k+1)]
for i in range(len(inputVal)):
    plug[inputVal[i]].append(i+1)

count = 0
lst = []
for i in range(k):
    if inputVal[i] in lst:
        plug[inputVal[i]].popleft()
    elif len(lst) != n:
        lst.append(inputVal[i])
        plug[inputVal[i]].popleft()
    else:
        count += 1
        tmp = -1
        for j in range(n):
            if not plug[lst[j]]:
                tmp_idx = j
                break
            else:
                if tmp < plug[lst[j]][0]:
                    tmp = plug[lst[j]][0]
                    tmp_idx = j
        lst[tmp_idx] = inputVal[i]
        plug[inputVal[i]].popleft()
print(count)