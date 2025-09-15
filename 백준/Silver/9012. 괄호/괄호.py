import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    a = input()

    lst = []
    count = 0

    for i in a:
        if i == '(':
            lst.append(i)
        elif i == ')':
            if lst != []:
                lst.pop(-1)
            else:
                count += 1
    if lst == [] and count == 0:
        print('YES')
    else:
        print('NO')
