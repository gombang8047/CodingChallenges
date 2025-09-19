import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

inputVal_list = []

while True:
    line = input().strip()
    if not line:
        break
    inputVal_list.append(int(line))

def bst_postorder(start, end):
    
    if start >= end:
        return

    root = inputVal_list[start]

    idx = start + 1
    while idx < end and inputVal_list[idx] < root:
        idx += 1
    
    bst_postorder(start+1, idx)
    bst_postorder(idx, end)
    print(root)

bst_postorder(0, len(inputVal_list))