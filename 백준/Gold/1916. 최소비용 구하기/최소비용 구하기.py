import sys
import heapq
input = sys.stdin.readline

city_count = int(input())
bus_count = int(input())
tree_list = [[]for _ in range(city_count+1)]
for _ in range(bus_count):
    start, end, cost = map(int, input().split())
    tree_list[start].append((cost, end))

start_city, end_city = map(int, input().split())

def dijkstra(start_city, end_city):
    visited_city = [False] * (city_count+1)
    min_distance_list = [float('inf')] * (city_count+1)
    min_distance_list[start_city] = 0
    heap_list = [(0, start_city)]
    heapq.heapify(heap_list)

    while heap_list:
        tmp = heapq.heappop(heap_list)
        if visited_city[tmp[1]] == False:
            visited_city[tmp[1]] = True
            for i in tree_list[tmp[1]]:
                heapq.heappush(heap_list, (min_distance_list[tmp[1]] + i[0],i[1]))
                min_distance_list[i[1]] = min(min_distance_list[i[1]], min_distance_list[tmp[1]] + i[0])
    
    print(min_distance_list[end_city])

dijkstra(start_city, end_city)