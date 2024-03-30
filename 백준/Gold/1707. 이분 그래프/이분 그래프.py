# 이분 그래프

import sys
from collections import deque
sys.setrecursionlimit(10**9)

testCase = int(sys.stdin.readline())

def dfs(start):

     for next in adjMatrix[start]:
          if visited[next] == False:
               if visited[start] == 1:
                    visited[next] = 2

               elif visited[start] == 2:
                    visited[next] = 1
               dfs(next)

def isBinaryGragph():
     for i in range(vertex):
          for next in adjMatrix[i]:
               if visited[i] == visited[next]:
                    return 0
     
     return 1

for tc in range(testCase):

     vertex,edge = map(int, sys.stdin.readline().split()) 

     adjMatrix =[[] for _ in range(vertex)]
     visited = [False]*vertex

     for i in range(edge):
          u,v = map(int, sys.stdin.readline().split())
          adjMatrix[u-1].append(v-1)
          adjMatrix[v-1].append(u-1)

     # print(adjMatrix)
     for i in range(vertex):
          if visited[i] == False:
               visited[i] = 1
               dfs(i)

     # print(visited)
     if isBinaryGragph():
          print('YES')
     else:
          print('NO')

     

