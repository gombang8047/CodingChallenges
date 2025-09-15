import sys
input = sys.stdin.readline

n = int(input())

stack_list = []

for _ in range(n):
    inputVal = list(input().split())

    if inputVal[0] == 'push':
        stack_list.append(int(inputVal[1]))
    elif inputVal[0] == 'pop':
        if stack_list:
            print(stack_list.pop())
        else:
            print(-1)
    elif inputVal[0] == 'size':
        print(len(stack_list))
    elif inputVal[0] == 'empty':
        if stack_list:
            print(0)
        else:
            print(1)
    elif inputVal[0] == 'top':
        if stack_list:
            print(stack_list[-1])
        else:
            print(-1)
    