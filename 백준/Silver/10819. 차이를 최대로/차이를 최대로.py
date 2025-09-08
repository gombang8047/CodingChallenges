N = int(input())

lst = list(map(int, input().split()))

used = [False] * N

path = []

fin = []

num = 0

def max_num(n, lst, path, used):

    global num

    if len(path) == N:
        for i in range(N):
            if i+1 < N:
                num += abs(path[i] - path[i+1])
        fin.append(num)
        num = 0
        return
    
    if n >= N:
        return
    
    for i in range(len(lst)):
        if used[i] == False:
            path.append(lst[i])
            used[i] = True
            max_num(n+1, lst, path, used)
            path.pop(-1)
            used[i] = False
    
max_num(0, lst, path, used)

print(max(fin))