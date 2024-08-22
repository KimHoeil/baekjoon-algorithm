# https://www.acmicpc.net/problem/1379

import sys
from collections import deque
import heapq

input = sys.stdin.readline

n = int(input())
endq = []
startq = []
for i in range(n):
    num, start, end = map(int, input().split())
    heapq.heappush(endq, (end,start,num))
    heapq.heappush(startq, (start, end, num))

visited = [[False,0] for i in range(n+1)]# 배정여부 체크, 배정 강의실 번호 저장
readyq = []
roomNum = 1
k = n

while startq:
    endCorse = endq[0] # 최상단값만 보기 = peek
    startCorse = startq[0]

    # print("end,stat", endCorse[0],endCorse[1], startCorse[0],startCorse[1])

    # 이미 배정된 경우
    if visited[endCorse[2]][0] == True:
        # print("what the fuck?", endCorse[0], startCorse[0])
        # print(visited)
        heapq.heappop(endq)
        continue

    # 같은 강의인 경우
    if endCorse[2] == startCorse[2]:
        heapq.heappop(startq)
        visited[startCorse[2]][1] = roomNum
        roomNum+=1
        # print("what?", endCorse[0], startCorse[0])
        print()
        continue
    
    # 이미 배정된 강의실이 있는 경우 먼저 확인
    if readyq:
        readyCorse = readyq[0]
        if readyCorse[0] <= startCorse[0]:
            visited[startCorse[2]][1] = visited[readyCorse[2]][1]
            heapq.heappop(startq)
            heapq.heappop(readyq)
            visited[readyCorse[2]][0] = True
            k -=1
            # print("reservation ready")
            # print("startCosrse", startCorse[0], startCorse[1], startCorse[2])
            # print("readyCorse", readyCorse[0], readyCorse[1], readyCorse[2])
            # print()
            continue

    
    # 시작시간이 빠른(작은) 경우 = 배정못하는 경우
    if endCorse[0] > startCorse[0]:
        heapq.heappop(startq)
        visited[startCorse[2]][1] = roomNum
        # print("reservation solo")
        # print("startCosrse", startCorse[0], startCorse[1], startCorse[2],roomNum)
        # print("endCosrse", endCorse[0], endCorse[1], endCorse[2])
        # print()
        roomNum +=1
    
    # 시작시간이 느린(큰) 경우 = 배정할 수 있는 경우
    elif endCorse[0] <= startCorse[0]:
        startCorse = heapq.heappop(startq)
        endCorse = heapq.heappop(endq)
        visited[endCorse[2]][0] = True

        # print("reservation duo")
        # print("startCosrse", startCorse[0], startCorse[1], startCorse[2], roomNum, visited[endCorse[2]][1])
        # print("endCosrse", endCorse[0], endCorse[1], endCorse[2])
        # print()

        if visited[endCorse[2]][1] != 0: # 배정방이 있다면 그걸 사용
            visited[startCorse[2]][1] = visited[endCorse[2]][1]
        else:
            visited[endCorse[2]][1] = roomNum
            visited[startCorse[2]][1] = roomNum
            roomNum +=1
        k -=1
        heapq.heappush(readyq, (startCorse[1], startCorse[0], startCorse[2])) # (종료,시작,번호)
        
        
print(k)
for i in range(1, n+1):
    print(visited[i][1])