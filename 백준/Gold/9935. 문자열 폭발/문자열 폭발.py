import sys
input = sys.stdin.readline

string_inputVal = list(input().strip())
explosion_string = list(input().strip())
stack_list = []

length_explosion_string = len(explosion_string)

for i in range(len(string_inputVal)):
    stack_list.append(string_inputVal[i])

    if stack_list[(len(stack_list) - length_explosion_string):] == explosion_string:
        for _ in range(length_explosion_string):
            stack_list.pop()

if stack_list:
    print("".join(stack_list))
else:
    print("FRULA")