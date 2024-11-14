def solution(slice, n):
    answer = 0
    result = n / slice

    if result == int(result):
        answer = result
    else: answer = int(result) + 1
    return answer