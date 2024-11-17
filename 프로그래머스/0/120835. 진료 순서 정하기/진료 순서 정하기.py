def solution(emergency):
    answer = [0] * len(emergency)
    rank = 1
    for _ in range(len(emergency)):
        max_val = max(emergency)
        idx = emergency.index(max_val)
        emergency[idx] = 0
        answer[idx] = rank
        rank +=1

    return answer