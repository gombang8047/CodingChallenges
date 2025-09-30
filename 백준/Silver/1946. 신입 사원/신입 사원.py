import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    score_list = []
    for _ in range(int(input())):
        a, b = map(int, input().split())
        score_list.append([a, b])

    score_list.sort(key=lambda x : x[0])

    count = 1
    tmp = score_list[0][1]
    for i in range(1, len(score_list)):
        if tmp > score_list[i][1]:
            tmp = score_list[i][1]
            count += 1
    
    print(count)