T = int(input())

for i in range(T):

    a = int(input())
    lst = list(map(int, input().split()))
    result = 0
    maxNum = -1

    for j in range(len(lst)-1, -1, -1):
        if maxNum <= lst[j]:
            maxNum = lst[j]
        else:
            result = result + maxNum - lst[j]

    print(f"#{i+1} {result}")