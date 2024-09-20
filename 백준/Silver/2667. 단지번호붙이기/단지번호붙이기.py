import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

board = [list(map(int, input().strip())) for _ in range(n)]
ans = []
def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    q = deque([])
    q.append((x,y))
    board[x][y] = 0
    
    cnt =1
    while q:
        curx,cury = q.popleft()
        for i in range(4):
            nx = curx + dx[i]
            ny = cury + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx,ny))
                    cnt +=1
    ans.append(cnt)

cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bfs(i,j)
            cnt+=1
ans.sort()
print(cnt)
for answer in ans:
    print(answer)
