def judgment(y, x, k):

    if not row_used[y][k] and not col_used[x][k] and not box_used[(y//3)*3 + (x//3)][k]:
        return True



def sudoku(n, find_empty, lst):

    if n >= len(find_empty):
        for i in range(len(lst)):
            print(" ".join(map(str, lst[i])))
        return True

    i = find_empty[n][0]
    j = find_empty[n][1]

    for k in range(1, 10):
        if judgment(i, j, k):
            lst[i][j] = k
            row_used[i][k] = True
            col_used[j][k] = True
            box_used[(i//3)*3 + (j//3)][k] = True
            if sudoku(n+1, find_empty, lst):
                return True
            lst[i][j] = 0
            row_used[i][k] = False
            col_used[j][k] = False
            box_used[(i//3)*3 + (j//3)][k] = False

lst = []
find_empty = []

for _ in range(9):
    lst.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if lst[i][j] == 0:
            find_empty.append([i, j])

row_used = [[False]*10 for _ in range(9)]
col_used = [[False]*10 for _ in range(9)]
box_used = [[False]*10 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if lst[i][j] != 0:  # 0이면 사용하지 않음
            row_used[i][lst[i][j]] = True
            col_used[j][lst[i][j]] = True

            if i // 3 == 0:
                if j // 3 == 0:
                    box_used[0][lst[i][j]] = True
                elif j // 3 == 1:
                    box_used[1][lst[i][j]] = True
                elif j // 3 == 2:
                    box_used[2][lst[i][j]] = True
            elif i // 3 == 1:
                if j // 3 == 0:
                    box_used[3][lst[i][j]] = True
                elif j // 3 == 1:
                    box_used[4][lst[i][j]] = True
                elif j // 3 == 2:
                    box_used[5][lst[i][j]] = True
            elif i // 3 == 2:
                if j // 3 == 0:
                    box_used[6][lst[i][j]] = True
                elif j // 3 == 1:
                    box_used[7][lst[i][j]] = True
                elif j // 3 == 2:
                    box_used[8][lst[i][j]] = True

sudoku(0, find_empty, lst)