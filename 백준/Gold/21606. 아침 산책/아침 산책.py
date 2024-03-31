# 아침산책 솔루션

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

place = sys.stdin.readline()
visited = [False]*n 
outdoor = [False]*n
cnt = 0

for p in range(len(place)):
     if place[p] == '0': # 0이면 실외
          outdoor[p] = True


adj = [[] for _ in range(n)]
for i in range(n-1):
     u,v = map(int, sys.stdin.readline().split())
     adj[u-1].append(v-1)
     adj[v-1].append(u-1)

     # 두 정점 모두 실내이면 경로의 수 2 증가
     if outdoor[u-1] ==False and outdoor[v-1] ==False:
          cnt +=2


def dfs(start):
     visited[start] = True
     insideCnt = 0

     for nowEndV in adj[start]:
          if outdoor[nowEndV] == False: # 인접한 노드가 실내라면
               insideCnt +=1

          elif not visited[nowEndV] and outdoor[nowEndV] == True: # 인접한 노드가 실외라면
               insideCnt += dfs(nowEndV)
     return insideCnt

for i in range(n):
     if outdoor[i] == True and not visited[i]: # 시작이 실외일 때만 탐색
          result = dfs(i) # dfs로 인접한 실내 노드 개수를 계산
          cnt += (result)*(result-1) # 경로의 개수 추가


print(cnt)
