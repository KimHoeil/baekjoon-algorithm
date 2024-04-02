# 최소비용구하기

import sys
from collections import defaultdict, deque
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = sys.maxsize

# adj = defaultdict(list) # 그래프 모델링 {시작정점:[(도착정점,가중치)]}
adj = [[] for _ in range(n)]

for i in range(m):
     u,v,w = map(int, sys.stdin.readline().split())
     adj[u-1].append((v-1, w))
     
start,end = map(int, sys.stdin.readline().split())

# for i in range(n):
#      print(adj[i])

def dijkstra(s,e,adjList):
     minq = []
     dist = [INF]*n
     visited = [False]*n

     dist[s] = 0 # 시작정점의 최단거리는 0부터 시작
     heapq.heappush(minq, (dist[s],s)) # (최소힙에 노드와 노드의 최단거리 삽입)

     while minq:
          nowCost, nowVertex = heapq.heappop(minq)
          # 이미 최단경로를 방문한 노드는 넘어감 (이전값이 갱신되었기 때문)
          if visited[nowVertex] == False:
               visited[nowVertex] = True

               # 인접 노드 비용 확인하기
               for nowEndV, nextCost in adjList[nowVertex]:
                    # 인접 노드의 최단거리 값 비교하기
                    if nowCost+nextCost < dist[nowEndV]: # 현재 정점의 최단거리+인접정점의 비용이 해당 정점의 최단거리보다 작다면 최단거리 갱신
                         dist[nowEndV] = nowCost+nextCost
                         heapq.heappush(minq, (dist[nowEndV], nowEndV)) # 다음 방문 후보 도시로 큐에 삽입
     
     print(dist[e])

dijkstra(start-1,end-1, adj)
