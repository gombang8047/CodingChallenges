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
    min_distance_list = [float('inf')] * (city_count+1)
    min_distance_list[start_city] = 0
    heap_list = [(0, start_city)]

    while heap_list:
        current_cost, current_city = heapq.heappop(heap_list)
        if current_cost > min_distance_list[current_city]:
            continue
        for cost, neighbor in tree_list[current_city]:
            new_cost = min_distance_list[current_city] + cost
            if new_cost < min_distance_list[neighbor]:
                min_distance_list[neighbor] = new_cost
                heapq.heappush(heap_list, (new_cost, neighbor))

    print(min_distance_list[end_city])

dijkstra(start_city, end_city)