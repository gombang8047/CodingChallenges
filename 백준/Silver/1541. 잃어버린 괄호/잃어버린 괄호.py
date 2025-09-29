import sys
import re
input = sys.stdin.readline

inputVal = re.split('([-+])', input())
result = []

i = 0
while i < len(inputVal):

    if inputVal[i] == '+':
        k = result.pop()
        result.append(int(k) + int(inputVal[i+1]))
        i+=1
    elif inputVal[i] == '-':
        result.append(inputVal[i])
    else:
        result.append(int(inputVal[i]))
    i += 1

s = ''.join(str (i) for i in result)

print(eval(s))
