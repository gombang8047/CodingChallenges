import sys
import heapq
input = sys.stdin.readline

heap_list = []  

n = int(input())
for _ in range(n):
    inputVal = int(input())

    if inputVal == 0:
        if not heap_list:
            print(0)
        else:
            print(-heapq.heappop(heap_list))

    else:
        heapq.heappush(heap_list, -inputVal)