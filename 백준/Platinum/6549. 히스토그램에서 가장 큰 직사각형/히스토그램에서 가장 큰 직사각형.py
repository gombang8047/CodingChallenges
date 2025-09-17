import sys
input = sys.stdin.readline

while True:
    inputVal = list(map(int, input().split()))
    if inputVal[0] == 0:
        break
    
    inputVal = inputVal[1:]
    inputVal.append(0)
    stack_inputVal = []
    max_extent_result = []

#스택에 인덱스 값으로 넣어서 비교하기

    for i in range(0, len(inputVal)):
        if not stack_inputVal: #stack이 비었을때 그냥 넣는다.
            stack_inputVal.append(i)
        elif inputVal[stack_inputVal[-1]] < inputVal[i]: #input값이 stack의 마지막 값보다 클때 그냥 넣는다.
            stack_inputVal.append(i)
        else: #input값이 stack의 마지막 값보다 작을때
            max_stack_point = stack_inputVal[-1]
            while True: #input값보다 stack의 마지막 값이 작을때까지 pop한다. 
                if not stack_inputVal: #만약 stack 비워지면 break
                    break
                elif inputVal[stack_inputVal[-1]] >= inputVal[i]:
                    move_point = len(stack_inputVal) - 1 #스택 뒤부터 앞으로 움직이기 위한 포인터
                    while True:
                        if stack_inputVal:#pop될 기둥의 높이 pop되기전에 최대 값이 될 수 있는 넓이를 구한다. #pop을 할때 그 기둥을 사용하는 최대 넓이를 구한다.
                            piller_height = inputVal[stack_inputVal[-1]]
                        if move_point < 0: #더 작은 수가 없을때 처음과 오른쪽 경계선의 거리를 곱한다.
                            max_extent_result.append(piller_height * i)
                            stack_inputVal.pop()
                            break
                        elif piller_height > inputVal[stack_inputVal[move_point]]:
                            max_extent_result.append(piller_height * (max_stack_point - stack_inputVal[move_point]))
                            stack_inputVal.pop()# 오른쪽 경계선은 max_width이 고정이고 왼쪽 경계선은 작아질때 그 값을 빼지고 곱하면 된다.
                            break
                        move_point -= 1
                else:
                    break
            stack_inputVal.append(i) #마지막에 input값을 넣어준다.

    print(max(max_extent_result))
        
    