import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

apple_coordinate = [[False] * n for _ in range(n)]
move_change = deque()
snake_location = deque()
snake_location_array = [[False] * n for _ in range(n)]
time = 1
snake_x, snake_y = 0, 0
move_change_direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
move_change_num = 0

for _  in range(k):
    a, b = map(int, input().split())
    apple_coordinate[b-1][a-1] = True

l = int(input())

for _ in range(l):
    a, b = list(input().split())
    move_change.append([a, b])

snake_location.append([0, 0]) #처음 뱀의 위치를 넣어둔다.
snake_location_array[0][0] = True

while True:
    if move_change:
        if int(move_change[0][0]) == time - 1: #방향전환의 시간이 됐을때 바꿔준다.
            if move_change[0][1] == "D": #D가 들어왔을때 방향을 오른쪽으로 바꿔준다 만약 4가 넘어가면 나머지만 남겨준다
                move_change_num = (move_change_num + 1) % 4
            elif move_change[0][1] == "L": #L이 들어왔을때 방향을 왼쪽으로 바꿔준다.
                if move_change_num == 0:
                    move_change_num = 4
                move_change_num = move_change_num - 1
            move_change.popleft() #쓰고난뒤 없애준다

    snake_x += move_change_direct[move_change_num][0]
    snake_y += move_change_direct[move_change_num][1] #뱀의 방향대로 더해준다.

    if snake_x < 0 or snake_y < 0 or snake_x >= n or snake_y >= n: #뱀의 머리가 맵의 밖으로 나갔을때 break해준다.
        break
    
    if snake_location_array[snake_x][snake_y] == True:
        break

    snake_location.appendleft([snake_x, snake_y]) #뱀머리의 위치를 옮기고 위치값을 저장해준다.
    snake_location_array[snake_x][snake_y] = True
    if apple_coordinate[snake_x][snake_y] == False: #꼬리의 위치를 빼고 False로 만든다.
        tail_index_location = snake_location.pop()
        snake_location_array[tail_index_location[0]][tail_index_location[1]] = False
    else: #애플의 위치에 도달했을때 
        apple_coordinate[snake_x][snake_y] = False
    
    time += 1 #모든것이 끝났을때 time을 1씩 증가시킨다.

print(time) #마지막 타임 출력
    
