# 회의실 배정

import sys
from collections import deque
n = int(sys.stdin.readline())

table= [] # (종료시각, 시작시각) -> 그리디를 사용하려면 회의가 종료되는 시점이 빠른순으로 정렬해야 한다.
for _ in range(n):
     s,e = map(int, sys.stdin.readline().split())
     table.append((e,s))

table.sort()

def activity_selection(n):
     """
     그리디 속성을 이용해서 회의가 가장
     빨리 끝나는 순서로 회의 시간 배정
     """
     q = deque()

     q.append(table[0])
     last = 0

     # 현재 회의 끝나는 시간이 다음 시작 시간보다 작은 경우 q에 삽입 
     for i in range(1, n):
          # (종료, 시작)
          if table[last][0] <= table[i][1]:
               s = table[i][1]
               f = table[i][0]
               q.append((f,s))
               last = i
     
     print(len(q))
     # print(q)

activity_selection(n)