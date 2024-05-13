# 2531번

import sys
input = sys.stdin.readline

n,d,k,c = map(int, input().split())

belt = []
# 초밥의 종류와 개수 입력받기
for _ in range(n):
    num = int(input())
    belt.append(num)

maxCnt = 0
maxAns = 0
# 초밥을 처음부터 끝까지 k개만큼 연속으로 먹기
for i in range(n):
    cnt = 0
    couponeCheck = False
    visited = [False] * (d+1)
    for j in range(i, i+k):
        j = j%n # 배열의 크기를 넘어가면 다시 처음으로 돌아오게 하기위해서 나머지연산
        # print(belt[j], end=' ')
        
        # 초밥의 종류 카운트 하기
        if visited[belt[j]] == False:
            visited[belt[j]] = True
            cnt +=1
            # 쿠폰 초밥과 연속으로 먹는 초밥이 같은지 확인
            if belt[j] == c:
                couponeCheck = True
    
    maxCnt = max(cnt, maxCnt)
    # print("Count: ", cnt)

    # 초밥 종류가 다 다르고 쿠폰에 없는 초밥을 먹었으면 k+1개의 초밥을 먹음
    if cnt == k and couponeCheck == False:
        # print(k+1)
        ans = k+1
    
    # 초밥 종류가 다 다르고 쿠폰에 있는 초밥을 먹으면 k개의 초밥을 먹음
    elif cnt ==k and couponeCheck == True:
        # print(k)
        ans = k
    
    # 초밥 종류가 다 다르지 않고 쿠폰에 없는 초밥을 먹은 경우
    elif cnt != k and couponeCheck == False:
        # print(cnt+1)
        ans = cnt+1
    
    # 초밥 종류가 다 다르지 않고 쿠폰에 있는 초밥을 먹은 경우
    else:
        # print(cnt)
        ans = cnt

    maxAns = max(ans, maxAns)
    
print(maxAns)