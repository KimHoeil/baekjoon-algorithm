# 임계경로

import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

indegree = [0]*n
reverseIndegree = [0]*n
adj = [[] for i in range(n)]

cnt = [[] for _ in range(n)]


from collections import deque

dist = [float('-inf')]*n # 최단 경로 체크
# route = [0]*n

def topologySort(s,e):
     q= deque()
     dist[s] = 0

     # 차수가 0인 노드 큐에 삽입
     for i in range(n):
          if indegree[i] == 0:
               q.append(i)
     
     for i in range(n):
          # 사이클 발생 확인
          if len(q) == 0:
               return
          
          nowVertex = q.popleft()

          for nowEndV, cost in adj[nowVertex]:
               # 도착점의 indegree를 1빼준다
               indegree[nowEndV] -=1

               # 도착점의 최단경로보다 현재 정점에서 이동하는게 비용이 더 크거나 같으면 값을 갱신해준다.
               if dist[nowVertex]+cost > dist[nowEndV]:
                    dist[nowEndV] = dist[nowVertex]+cost
                    cnt[nowEndV] = [nowVertex]

               elif dist[nowVertex]+cost == dist[nowEndV]:
                    cnt[nowEndV].append(nowVertex)

               # 만약 indegree가 0이라면 큐에 삽입해준다
               if indegree[nowEndV] == 0:
                    q.append(nowEndV)

     
     print(dist[e])
     # print(dist)
     # print(route)

reverseAdj = [[] for i in range(n)]   

for i in range(m):
     u,v,w = map(int, sys.stdin.readline().split())
     adj[u-1].append((v-1,w))
     reverseAdj[v-1].append(u-1)
     indegree[v-1] +=1 # 들어오는 차수 증가

start,end = map(int, sys.stdin.readline().split())

topologySort(start-1,end-1)
# reverseTopologySort(end-1, start-1)


# 도착점에서 역추적하기
q = deque([end-1])
route = set()
while q:
     now = q.popleft()
     for nextV in cnt[now]:
          if (now, nextV) not in route:
               route.add((now,nextV))
               q.append(nextV)
print(len(route))