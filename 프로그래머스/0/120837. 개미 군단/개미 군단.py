def solution(hp):
    answer = 0
    if hp == 0: return 0
    
    div1 = hp // 5
    if hp % 5 != 0:
        hp = hp % 5
        div2 = hp // 3
        rest = hp % 3
        return div1+div2+rest
    else:
        return div1
    
