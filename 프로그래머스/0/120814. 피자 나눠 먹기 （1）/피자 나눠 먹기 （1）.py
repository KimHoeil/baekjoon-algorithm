def solution(n):
    answer = 0
    
    answer = n/7
    if answer == 0 or answer != int(answer):
        answer = int(answer) + 1
    
    return answer