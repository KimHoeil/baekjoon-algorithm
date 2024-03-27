# 최대 힙

import sys
import heapq
from typing import MutableSequence

# sys.stdin = open('input.txt','r')
n = int(sys.stdin.readline())

heap = []
# heapq는 최소힙 형태로 저장된다.
# 하지만 튜플을 사용하면 최대힙을 만들 수 있다.
for i in range(n):
     x = int(sys.stdin.readline())

     if x>=1: # x가 자연수이면 배열에 집어 넣기
          heapq.heappush(heap,(-x,x))
     else: # x가 0이면 배열에서 가장 큰 값을 출력하고 그 값을 제거
          if len(heap)!=0:
               ans = heapq.heappop(heap)
               print(ans[1])
          else:
               print(0)
