import sys
input = sys.stdin.readline

n = int(input())

time_list = []

for _ in range(n):
    time_list.append(list(map(int, input().split())))

time_list.sort(key=lambda x : (x[1], x[0]))

last_value = 0
result = []

for start, end in time_list:

    if last_value <= start:
        result.append([start, end])
        last_value = end

print(len(result))