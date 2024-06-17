# https://www.acmicpc.net/problem/1012

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())


def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0, -1,1]

    q = deque([(x,y)])
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < m and 0<= ny < n:
                if arr[nx][ny] == 1 and visited[nx][ny] is False:
                    visited[nx][ny] = True
                    q.append((nx,ny))

        
for _ in range(t):
    m,n,k = map(int, input().split())
    cnt = 0

    arr = [[0 for j in range(n)] for i in range(m)]
    cabbageq = deque([])
    for i in range(k):
        x,y = map(int, input().split())
        arr[x][y] = 1
        cabbageq.append((x,y))
    
    visited = [[False for j in range(n)] for i in range(m)] 

    # for a in arr:
    #     print(a)

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1 and visited[i][j] is False:
                bfs(i,j)
                cnt +=1

    print(cnt)
