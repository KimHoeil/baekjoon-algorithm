# https://www.acmicpc.net/problem/25189

import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
rf,cf,rh,ch = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# visited 3차원배열로 선언하기
visited = [[[1e9,1e9] for j in range(m)] for i in range(n)] # [일반점프횟수, 슈퍼점프횟수]
visited_row = [False]* 1000
visited_col = [False]* 1000

def bfs(rf,cf,rh,ch):

    if rf == rh and cf == ch:
        print(0)
        return

    q = deque([])
    q.append((rf,cf,0,0))
    visited[rf][cf][0] = 0
    
    while q:
        x, y, jumpCnt, isSuperJump = q.popleft() # isSuperJump => 0이면 그냥점프, 1이면 슈퍼점프

        if x==rh and y==ch:
            print(jumpCnt)
            return

        # 상하좌우
        dx = [-board[x][y], board[x][y], 0, 0]
        dy = [0, 0, -board[x][y] ,board[x][y]]

        # 슈퍼점프를 '쓸'경우
        if isSuperJump == 0:
            # 슈퍼점프를 '쓸'경우 y축 점프
            if visited_row[x] is False:
                visited_row[x] = True
                for j in range(m):                
                    if visited[x][j][1] > jumpCnt+1:
                        visited[x][j][1] = jumpCnt+1
                        q.append((x,j,jumpCnt+1,1))
                        
            # 슈퍼점프를 '쓸'경우 x축 점프
            if visited_col[y] is False:
                visited_col[y] = True
                for k in range(n):
                    if visited[k][y][1] > jumpCnt+1:
                        visited[k][y][1] = jumpCnt+1
                        q.append((k,y,jumpCnt+1,1))


        # 일반점프를 "쓸"경우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= n or 0 > ny or ny >= m: # 유효한 공간이 아니면
                continue
            
            if visited[nx][ny][isSuperJump] > jumpCnt+1:
                q.append((nx,ny,jumpCnt+1,isSuperJump))
                visited[nx][ny][isSuperJump] = jumpCnt+1

   
    print(-1)    

bfs(rf-1,cf-1,rh-1,ch-1)