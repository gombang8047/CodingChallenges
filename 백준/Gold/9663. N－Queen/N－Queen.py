def nqueen(row, cols, diag_minus, diag_plus):

    global count

    if row == N:
        count += 1
        return
    
    for i in range(N):
        if cols[i] == True and diag_minus[row + i] == True and diag_plus[row - i + (N-1)] == True:
            cols[i] = False
            diag_minus[row + i] = False
            diag_plus[row - i + (N-1)] = False
            nqueen(row + 1, cols, diag_minus, diag_plus)
            cols[i] = True
            diag_minus[row + i] = True
            diag_plus[row - i + (N-1)] = True




N = int(input())

count = 0
cols = [True] * N
diag_minus = [True] * (2*N-1)
diag_plus = [True] * (2*N-1)

nqueen(0, cols, diag_minus, diag_plus)

print(count)