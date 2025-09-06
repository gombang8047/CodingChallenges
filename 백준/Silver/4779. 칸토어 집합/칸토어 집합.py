import sys

input = sys.stdin.readline

def canto(arr, start, end):
    
    length = end - start 

    if length <= 1:
        return

    start += length // 3
    end -= length // 3

    arr[start:end] = ' ' * (length // 3)
    
    canto(arr, start - (length // 3), start)
    canto(arr, end, end + (length // 3))


while True:
    N = input()

    if not N:
        break

    N = int(N)

    arr = list('-' * (3 ** N))

    canto(arr, 0, len(arr))

    print("".join(arr))

