# 가운데를 말해요
# 힙큐는 힙정렬 알고리즘을 사용해서 정렬시간이 O(n log n)이다
# 이진트리 기반이므로 n -> log n으로 줄어듬

import heapq
import sys

maxQ = []
minQ = []

# sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())

# 힙에서 값 꺼낼때
# ans = heapq.heappop(heap)

for i in range(1,n+1):
     num = int(sys.stdin.readline())

     if i==1:
          heapq.heappush(maxQ, (-num,num)) # 최대 힙
     elif i==2:
          heapq.heappush(minQ, (num,num))  # 최소 힙
     else:
          if i%2==0: # 짝수이면 최소 힙에 넣기
               heapq.heappush(minQ, (num,num))  # 최소 힙
          elif i%2==1: # 홀수이면 최대 힙에 넣기
               heapq.heappush(maxQ, (-num,num)) # 최대 힙

     # 수가 두 개이상이고, 최대힙값이 최소힙값보다 크면 값 스왑
     if i >=2 and maxQ[0][1] > minQ[0][1]:
          temp = heapq.heappop(maxQ)    # 최대힙의 top 반환
          heapq.heappush(maxQ, (-minQ[0][1], minQ[0][1])) # 최대힙에 최소힙값 push
          heapq.heappop(minQ)
          heapq.heappush(minQ, (temp[1], temp[1]))

     print(maxQ[0][1])
