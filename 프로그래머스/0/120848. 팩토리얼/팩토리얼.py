def solution(n):
    
    A = 1
    B = 2
    count = 0
    
    while A <= n:
        
        A = A * B
        B += 1
        count += 1
    
    answer = count
    
    return answer