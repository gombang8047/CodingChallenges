import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print_inputVal = deque(map(int, input().split()))

    time = 0
    while True:

        if print_inputVal[0] < max(print_inputVal): #프린트의 최대 중요도보다 낮으면 뒤로 보낸다.
            print_inputVal.append(print_inputVal.popleft())
        
        else:

            print_inputVal.popleft() #프린트의 최대중요도를 팝한다.
            time += 1

            if m == 0:
                print(time) #이때 m이 0이면 시간을 출력한다.
                break

        if m > 0:
            m -= 1
        else:
            m = len(print_inputVal) - 1
