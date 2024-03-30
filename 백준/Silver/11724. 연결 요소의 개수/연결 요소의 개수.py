# 연결요소의 개수

import sys
from collections import defaultdict
from collections import deque


n,m = map(int, sys.stdin.readline().split())

adjMatrix = [[] for _ in range(n)]
visited= [False]*n

# print(adjMatrix)

for i in range(m):
     u,v = map(int, sys.stdin.readline().split())
     adjMatrix[u-1].append(v-1)
     adjMatrix[v-1].append(u-1)

# print(adjMatrix)

def bfs(vertex):
     q = deque()
     q.append(vertex)
     visited[vertex] = True

     while q:
          front = q.popleft()

          for v in adjMatrix[front]:
               if visited[v] == False:
                    visited[v] = True
                    q.append(v)
                    
cnt =0
for i in range(n):
     if visited[i] == False:
          bfs(i)
          cnt +=1
          
print(cnt)