N = int(input())

W = []

for _ in range(N):
    W.append(list(map(int, input().split())))

path = []

used = [[True for _ in range(N)] for _ in range(N)] 

for i in range(N):
    used[i][i] = False

city = [True] * N

fin = []

def min_cost(n, W, path, used, city):

    if len(path) == N and n == 0:
        fin.append(sum(path))
        return

    if n >= N:
        return
    
    if city[n] == False:
        return
    
    for i in range(N):
        if used[n][i] == True and W[n][i] != 0:
            path.append(W[n][i])
            used[n][i] = False
            city[n] = False
            min_cost(i, W, path, used, city)
            path.pop(-1)
            used[n][i] = True
            city[n] = True
            
min_cost(0, W, path, used, city)

print(min(fin))