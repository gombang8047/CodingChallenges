def calculate(n, lst, team):

    if n >= N//2:
        if len(process) == N//2:
            team1.append(tuple(sorted(process)))
            return

    for i in range(N):
        if used[i] == False:
            if not process:
                process.append(team[i])
                used[i] = True
                calculate(n+1, lst, team)
                process.pop()
                used[i] = False
            elif team[i] > process[-1]:
                process.append(team[i])
                used[i] = True
                calculate(n+1, lst, team)
                process.pop()
                used[i] = False

N = int(input())
result = []
process = []
lst = []
for i in range(N):
    lst.append(list(map(int, input().split())))
team = [i for i in range(N)]
used = [False] * N
used_team = [False] * N

team1 = []

calculate(0, lst, team)

fin = []

team1 = list(set(team1))
for k in range(len(team1)):
    team2 = tuple(set([i for i in range(N)]) - set(team1[k]))
    synergy1 = sum(lst[team1[k][i]][team1[k][j]] + lst[team1[k][j]][team1[k][i]] for i in range(len(team1[k])) for j in range(i+1, len(team1[k])))
    synergy2 = sum(lst[team2[i]][team2[j]] + lst[team2[j]][team2[i]] for i in range(len(team2)) for j in range(i+1, len(team2)))
    fin.append(abs(synergy1-synergy2))

print(min(fin))
