import sys
input = sys.stdin.readline

def select_wifi(inputVal, target, low, high):

    while True:
        
        middle = (high + low) // 2

        count = 1

        last = inputVal[0]
        for x in (inputVal[1:]):
            if x - last >= middle:
                count += 1
                last = x
            
        if low > high:
            break
        elif target <= count :
            fin.append(middle)
            low = middle + 1

        elif target > count:
            high = middle - 1


inputVal = []

n, c = map(int, input().split())

for _ in range(n):
    inputVal.append(int(input()))

inputVal.sort()

fin = []

select_wifi(inputVal, c, 1, max(inputVal)-min(inputVal))

print(max(fin))

