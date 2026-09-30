def solution(board):
    
    n = len(board)
    m = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if i + di >= 0 and i + di < n and j + dj >= 0  and j + dj < n:
                            m[i+di][j+dj] = 1
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if m[i][j] == 0:
                answer += 1
    
    return answer