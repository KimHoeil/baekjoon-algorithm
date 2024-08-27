# https://www.acmicpc.net/problem/8983

import sys
from collections import deque

input = sys.stdin.readline

m,n,l = map(int, input().split())
M = list(map(int, input().split()))
M.sort()
animals = []
for _ in range(n):
    x,y = map(int, input().split())
    animals.append((x,y))

q = deque(animals)

cnt = 0
while q:
    x,y =q.popleft()

    if y > l:
        continue

    start = 0
    end = len(M)-1
    ans = 0
    while start <= end:
        mid = (start+end) // 2
        saro = M[mid]

        if x >= saro:
            ans =  mid
            start = mid+1
        else:
            end = mid-1

    # print("ans=",ans,M[ans], "x,y=",x,y)
    # 이분탐색으로 찾은 사로의 바로 왼쪽 사로도 같이확인
    # 이분탐색의 조건이 크거나 같은 경우이기때문에 더 작은 경우가 x좌표가 더가까울수도 있기 때문
    if len(M) == 1:
        dis = abs(M[ans]-x) + y
        if dis <= l:
            cnt +=1


    elif ans != 0:
        left = ans -1
        
        dis1 = abs(M[ans]-x) + y
        dis2 = abs(M[left]-x) + y
        
        if dis1 <= l:
            cnt +=1
        elif dis2 <= l:
            cnt +=1
            
    else:
        right = ans +1
        dis1 = abs(M[ans]-x) + y
        dis2 = abs(M[right]-x) + y
        if dis1 <= l: # 사정거리안에 들어오면
            cnt +=1
        elif dis2 <= l:
            cnt +=1

print(cnt)