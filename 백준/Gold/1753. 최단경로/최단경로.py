# 최단경로

import sys
from collections import defaultdict, deque
import heapq

n,m = map(int, (sys.stdin.readline().split()))
INF = sys.maxsize

start = int(sys.stdin.readline())
# adj = defaultdict(list) # 그래프 모델링 {시작정점:[(도착정점,가중치)]}
adj = [[] for _ in range(n)]
minq = []
dist = [INF]*n

for i in range(m):
     u,v,w = map(int, sys.stdin.readline().split())
     adj[u-1].append((v-1, w))
     

# for i in range(n):
#      print(adj[i])

def dijkstra(s):
     dist[s] = 0 # 시작정점의 최단거리는 0부터 시작
     heapq.heappush(minq, (dist[s],s)) # (최소힙에 노드와 노드의 최단거리 삽입)

     while minq:
          minCost, nowVertex = heapq.heappop(minq)

          for nowEndV, adjCost in adj[nowVertex]:
               # 인접 노드의 최단거리 값 비교하기
               
               if minCost+adjCost < dist[nowEndV]: # 현재 정점의 최단거리+인접정점의 비용이 해당 정점의 최단거리보다 작다면 최단거리 갱신
                    dist[nowEndV] = minCost+adjCost
                    heapq.heappush(minq, (dist[nowEndV], nowEndV)) # 다음 방문 후보 도시로 큐에 삽입
     

dijkstra(start-1)

for i in dist:
     if i == INF:
          print('INF')
     else:
          print(i)
          