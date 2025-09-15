import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

lst = deque()

for _ in range(N):

    a = input().split()

    if a[0] == 'push':
        lst.append(int(a[1]))
    
    elif a[0] == 'pop':
        if lst:
            sys.stdout.write(str(lst.popleft()) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')
    
    elif a[0] == 'size':
        sys.stdout.write(str(len(lst)) + '\n')
    
    elif a[0] == 'empty':
        if lst:
            sys.stdout.write(str(0) + '\n')
        else:
            sys.stdout.write(str(1) + '\n')
    
    elif a[0] == 'front':
        if lst:
            sys.stdout.write(str(lst[0]) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')
    
    elif a[0] == 'back':
        if lst:
            sys.stdout.write(str(lst[-1]) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')
    