# 신입사원

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for testCase in range(t):
     n = int(input())
     applyer = []
     for _ in range(n):
          document, interview = map(int, input().split())
          applyer.append((document,interview))

     applyer.sort()
     # print(applyer)

     q = deque()

     q.append(applyer[0])
     last = 0

     for i in range(1,n):
          # 합격한 사람의 면접 순위보다 다음 사람의 면접 순위가 높으면 선발
          if applyer[last][1] > applyer[i][1]:
               q.append(applyer[i])
               last = i
               
     print(len(q))
     # print(q)
