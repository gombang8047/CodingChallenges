import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

compare_student = {}
student = [0] * (n+1)
queue_list = deque()
result = []

for _ in range(m):
    a, b = map(int, input().split())
    student[b] += 1
    if a not in compare_student:
        compare_student[a] = []
    if b not in compare_student:
        compare_student[b] = []
    compare_student[a].append(b)

for i in range(1, len(student)):
        if student[i] == 0:
            queue_list.append(i)
            student[i] = '.'

while queue_list:
    tmp = queue_list.popleft()
    result.append(tmp)

    for i in compare_student.get(tmp, []):
        student[i] -= 1
        if student[i] == 0:
            queue_list.append(i)
            student[i] = '.'
    
print(*result)