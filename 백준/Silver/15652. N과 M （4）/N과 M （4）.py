def select(lst, last, n):
    
    if n >= M:
        print(*last)
        return
    
    for i in range(N):
        if not last:
            last.append(lst[i])
            select(lst, last, n+1)
            last.pop(-1)
        elif lst[i] >= last[-1]:
            last.append(lst[i])
            select(lst, last, n+1)
            last.pop(-1)
        
N, M = map(int, input().split())

lst = []
last = []
for i in range(1, N+1):
    lst.append(i)

select(lst, last, 0)