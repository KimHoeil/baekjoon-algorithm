def solution(rsp):
    answer = ''
    # 가위 = 2
    # 바위 = 0
    # 보 = 5
    for hand in rsp:
        if hand == "2": answer += '0'
        elif hand == "0": answer += '5'
        else: answer += '2'

    return answer