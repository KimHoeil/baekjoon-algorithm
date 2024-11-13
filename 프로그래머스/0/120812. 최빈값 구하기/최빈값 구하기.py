from collections import Counter
def solution(array):
    answer = -1
    counter = Counter(array)
    
    # 가장 빈도가 높은 숫자들을 찾음
    max_count = max(counter.values())
    most_common = [num for num, freq in counter.items() if freq == max_count]
    
    # 최빈값이 하나면 그 값을 반환, 여러 개면 -1을 반환
    return most_common[0] if len(most_common) == 1 else answer