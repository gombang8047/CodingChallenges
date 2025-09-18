import sys
input = sys.stdin.readline

n = int(input())
binary_tree = []
result_list_front = []
result_list_mid = []
result_list_end = []

for _ in range(n):
    binary_tree.append(list(map(str, input().split())))

binary_tree.sort(key=lambda x : x[0])

def binary_tree_search(binary_tree, i):

    result_list_front.append(binary_tree[i][0])

    if binary_tree[i][1] != ".":
        binary_tree_search(binary_tree, ord(binary_tree[i][1]) - 65)

    result_list_mid.append(binary_tree[i][0])

    if binary_tree[i][2] != ".":
        binary_tree_search(binary_tree, ord(binary_tree[i][2]) - 65)

    result_list_end.append(binary_tree[i][0])

binary_tree_search(binary_tree, 0)

print("".join(result_list_front))
print("".join(result_list_mid))
print("".join(result_list_end))