import sys
input = sys.stdin.readline

n = int(input())
inputVal_list = []

for _ in range(n):
    inputVal_list.append(list(map(int, input().split())))

def confetti(n, inputVal_list, start_x, end_x, start_y, end_y):

    global count_blue
    global count_white

    if n == 0:
        return
    
    check_num = False
    check_white = 0
    check_blue = 0
    
    for i in range(start_x, end_x):
        for j in range(start_y, end_y):
            if check_blue != 0 and check_white != 0:
                break
            if inputVal_list[i][j] == 0:
                check_white += 1
                check_num = True
            else:
                check_blue += 1
        else:
            continue
        break

    if check_white == n*n:
        count_white += 1
        return   
    if check_num == False:
        count_blue += 1
        return
    else:
        confetti(n//2, inputVal_list, start_x, (start_x + end_x)//2, start_y, (start_y + end_y)//2)
        confetti(n//2, inputVal_list, (start_x + end_x)//2, end_x, start_y, (start_y + end_y)//2)
        confetti(n//2, inputVal_list, start_x, (start_x + end_x)//2, (start_y + end_y)//2, end_y)
        confetti(n//2, inputVal_list, (start_x + end_x)//2, end_x, (start_y + end_y)//2, end_y)

count_blue = 0
count_white = 0

confetti(n, inputVal_list, 0, len(inputVal_list), 0, len(inputVal_list))

print(count_white)
print(count_blue)