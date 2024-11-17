def solution(n):
    answer = 0
    
    for a in range(1, n+1):
        b = n / a
        if b == int(b): answer +=1
    
    return answer