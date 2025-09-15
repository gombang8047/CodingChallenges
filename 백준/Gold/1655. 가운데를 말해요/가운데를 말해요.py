import sys
import heapq
input = sys.stdin.readline

n = int(input())

max_heap_list = []
min_heap_list = []

for _ in range(n):
    inputVal = int(input())

    if not max_heap_list or inputVal <= -max_heap_list[0]:
        heapq.heappush(max_heap_list, -inputVal)
    else:
        heapq.heappush(min_heap_list, inputVal)

    if len(max_heap_list) > len(min_heap_list) + 1:
        heapq.heappush(min_heap_list, -heapq.heappop(max_heap_list))
    elif len(min_heap_list) > len(max_heap_list):
        heapq.heappush(max_heap_list, -heapq.heappop(min_heap_list))

    print(-max_heap_list[0])