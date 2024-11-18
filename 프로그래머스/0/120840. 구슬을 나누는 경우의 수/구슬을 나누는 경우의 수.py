
def solution(balls, share):
    answer = 0
    
    n =1
    for i in range(1, balls+1):
        n *= i
    m =1    
    for j in range(1, share+1):
        m *= j
    rest = balls-share
    nm = 1
    for k in range(1, rest+1):
        nm *= k
    answer = n // (nm*m)
    
    return answer