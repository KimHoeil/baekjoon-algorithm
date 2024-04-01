# 줄세우기, 위상정렬

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
inDegree = [0] *n # 정점에 들어오는 간선 ex. 1->3 에서 -> inDegree
adj = [[] for i in range(n)]

def topologySort(n):
     q = deque()

     # 위상정렬 시작
     # 큐에 in-degree가 0인 정점을 먼저 넣는다
     for i in range(n):
          if inDegree[i] == 0:
               q.append(i) # 넣을때는 해당 정점의 인덱스를 넣어야한다.

     # 완전한 전체 순회를 위해 n개 노드 반복
     for i in range(n):
          # n개까지 전체 방문하기 전 큐가 비었다면
          # 사이클이 발생하였다는 뜻
          if len(q) == 0:
               return
          
          front = q.popleft()
          # 문제는 1부터 시작하므로 +1을 해준 번호를 출력
          print(front+1, end=' ')

          # 방문한 정점에서 나가는 간선(out-degree)들에 대해 계산
          # 해당 간선들이 들어오는 정점, 즉 도착점에서는 들어오는 간선(in-degree)이 줄어드는 것이기 때문에
          # 간선 수만큼 in-degree를 줄여줘야한다.
          for edge in adj[front]:
               nowEndV = edge

               inDegree[nowEndV] -=1 # 도착점의 indegree를 1빼준다

               # 만약 indegree가 0이라면
               # 다음 위상정렬 계산을 위해 해당 정점을 큐에 삽입한다.
               if inDegree[nowEndV] == 0:
                    q.append(nowEndV)

for i in range(m):
     a,b = map(int, sys.stdin.readline().split())

     # 학생 두명의 키를 비교하는 것을 그래프로 정렬하기
     # a학생이 b학생을 가리키고 있다는것은 b학생보다 a학생이 크다는 뜻
     adj[a-1].append(b-1)
     inDegree[b-1] +=1 # b학생의 들어오는 간선 추가해주기

topologySort(n)
