def solution(dot):
    answer = 0
    
    x,y = dot
    # 2사분면에 속하는 경우
    if x<0 and y >0: return 2
    # 1사분면에 속하는 경우
    if x>0 and y>0: return 1
    # 3사분면에 속하는 경우
    if x<0 and y <0: return 3
    # 4사분면에 속하는 경우
    if x>0 and y<0: return 4
    
    
    
    
    
    
    
    return answer