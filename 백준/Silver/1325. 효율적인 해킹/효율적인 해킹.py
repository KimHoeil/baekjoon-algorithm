# https://www.acmicpc.net/problem/1325

import sys
from collections import deque

input = sys.stdin.readline  

n,m = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    adj[v].append(u)

def bfs(vertex):
    q = deque()
    q.append(vertex)
    visited = [False] * (n+1)
    visited[vertex] = True
    count = 1
    while q:
        v = q.popleft()
        for nowEndV in adj[v]:
            if not visited[nowEndV]:
                visited[nowEndV] = True
                q.append(nowEndV)
                count += 1
    return count

cntList = []
for i in range(1,n+1):
    cntList.append(bfs(i))
    
print(*[i for i in range(1,n+1) if cntList[i-1] == max(cntList)])