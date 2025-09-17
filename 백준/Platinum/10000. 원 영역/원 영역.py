import sys
input = sys.stdin.readline

n = int(input())
circle_list = []
for _ in range(n):
    a, b = map(int, input().split())
    circle_list.append([a-b, a+b])

circle_list.sort(key=lambda x : (x[1], x[1] - x[0]))
stack_list = []
area_count = 1

for i in range(len(circle_list)):
    if not stack_list:
        stack_list.append(circle_list[i])
        area_count += 1
        continue

    new_line = circle_list[i]
    area_count += 2 if stack_list[-1][0] <= new_line[0] and stack_list[-1][1] >= new_line[1] else 1
    
    while stack_list:
        p = stack_list.pop()
        if p[1] < new_line[0]:
            stack_list.append(p)
            break
        if p[0] <= new_line[0] <= p[1]:
            new_line = [p[0], new_line[1]]

    stack_list.append(new_line)

print(area_count)