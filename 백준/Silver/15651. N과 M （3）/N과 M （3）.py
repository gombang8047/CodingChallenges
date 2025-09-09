def select(list, last, n):
    
    if n >= M:
        print(*last)
        return
    
    for i in range(N):
        last.append(list[i])
        select(list, last, n+1)
        last.pop(-1)
    

N, M = map(int, input().split())

list = []
last = []
for i in range(1, N+1):
    list.append(i)

select(list, last, 0)