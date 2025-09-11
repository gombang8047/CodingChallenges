def num(T, count):

    if T < 0:
        return 0
    if T == 0:
        count += 1
        lst.append(count)
        return 0

    num(T-1, count)
    num(T-2, count)
    num(T-3, count)

T = int(input())

for _ in range(T):

    n = int(input())

    lst = []

    num(n, 0)
    print(sum(lst))
    lst = []