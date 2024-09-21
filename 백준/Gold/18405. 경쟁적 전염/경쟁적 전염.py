import sys
from collections import deque
import heapq
input = sys.stdin.readline

n,k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s,x,y = map(int, input().split())
virus = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
           virus.append((board[i][j],i,j))

virus.sort()
q = deque(virus)

def bfs(q):    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    time = 0
    virus = []
    while q:
        num,row,col = q.popleft()

        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny] == 0:
                    board[nx][ny] = num
                    virus.append((num,nx,ny))

    return virus

for time in range(s):
    q = deque(bfs(q))

print(board[x-1][y-1])

