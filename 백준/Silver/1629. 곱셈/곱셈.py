import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def multiplication(a, b):

    global num

    if b == 0:
        return
    
    if b % 2 == 1:
        num *= (a % c)
        multiplication(a % c, b - 1)
    else:
        multiplication(a * a, b // 2)

num = 1
multiplication(a, b)
print(num % c)