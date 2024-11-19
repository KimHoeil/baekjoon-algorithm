def solution(num_list, n):
    list_len = len(num_list) // n
    answer = [[]*n for i in range(list_len)]
    
    cnt = 1
    idx = 0
    for num in num_list:
        answer[idx].append(num)
        if cnt % n == 0: idx +=1
        cnt +=1
    ####### 리스트 슬라이싱 풀이 #############
    result = []
    for i in range(0, len(num_list), n):
        result.append(num_list[i:i+n])
    
    
    return result