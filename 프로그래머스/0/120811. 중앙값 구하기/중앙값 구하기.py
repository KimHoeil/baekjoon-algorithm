def solution(array):
    answer = 0
    array.sort()
    median = len(array) // 2
    return array[median]