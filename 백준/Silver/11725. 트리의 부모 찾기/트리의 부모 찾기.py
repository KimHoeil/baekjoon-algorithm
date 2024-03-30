# 트리의 부모 찾기

import sys
from collections import deque
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())

adjMatrix =[[] for _ in range(n)]
visited = [False]*n
ans = [0]*n

for i in range(n-1):
     u,v = map(int, sys.stdin.readline().split())

     adjMatrix[u-1].append(v-1)
     adjMatrix[v-1].append(u-1)

# print(adjMatrix)

def dfs(startVertex):

     visited[startVertex] = True
     for i in adjMatrix[startVertex]:
          if visited[i] == False:
               ans[i] = startVertex+1
               visited[i] = True
               dfs(i)
               visited[i] = False
dfs(0)
for i in range(1, len(ans)):
     print(ans[i])