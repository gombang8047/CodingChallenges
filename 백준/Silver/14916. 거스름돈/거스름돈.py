import sys
input = sys.stdin.readline

n = int(input())

def calculate(n):

    count = 0

    for i in range(n//5, -1, -1):
        tmp = n - 5*i
        if tmp % 2 == 0:
            j = tmp // 2
            count = i + j
            break
    
    if count != 0:
        print(count)
    else:
        print(-1)

calculate(n)