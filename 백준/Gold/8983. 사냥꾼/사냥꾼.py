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
    pos = 0
    while start <= end:
        mid = (start+end) // 2
        saro = M[mid]

        if x >= saro: # 사로위치가 작은경우
            pos =  mid
            start = mid+1

        else: # 사로위치가 큰경우
            end = mid-1

    # print("pos=",pos,M[pos], "x,y=",x,y)

    if pos < len(M):
        dis = abs(M[pos]-x) + y
        if dis <= l:
            cnt +=1
            continue
    
    if pos > 0:
        dis = abs(M[pos-1]-x) + y
        if dis <= l:
            cnt+=1
            continue
    
    if pos +1 < len(M):
        dis = abs(M[pos+1]-x)+y
        if dis <= l:
            cnt+=1
            continue





print(cnt)