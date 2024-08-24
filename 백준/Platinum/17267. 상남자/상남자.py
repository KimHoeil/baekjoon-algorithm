
# https://www.acmicpc.net/problem/17267

import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
l,r = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().rstrip())))
visited = [[False for j in range(m)] for i in range(n)]

# print(board)

def bfs(x,y,L,R):
    cnt = 1
    q = deque([])
    q.append((x,y,L,R))
    visited[x][y] = True
    
    while q:
        cur_x, cur_y, L,R = q.popleft()
        
        # print("cur_y:", cur_y)
        # 위,아래 먼저 이동, 벽있으면 막힘
        for up_nx in range(cur_x, -1, -1):
            if 0 > up_nx or n <= up_nx:
                break
            if board[up_nx][cur_y] == 1:
                break
            
            if visited[up_nx][cur_y] is False:
                q.append((up_nx,cur_y,L,R))
                visited[up_nx][cur_y] = True
                cnt +=1
                # print("append up", up_nx,cur_y, R)
                # for i in visited:
                #     print(*i)
                # print()

        for down_nx in range(cur_x, n):
            if 0 > down_nx or n <= down_nx:
                break
            if board[down_nx][cur_y] == 1:
                break
            
            if visited[down_nx][cur_y] is False:
                q.append((down_nx,cur_y,L,R))
                visited[down_nx][cur_y] = True
                cnt +=1
        
        # 왼쪽, 오른쪽 한칸씩 이동
        if cur_y >0 and L>0 and board[cur_x][cur_y-1] == 0:
            if visited[cur_x][cur_y-1] is False:
                q.append((cur_x,cur_y-1, L-1, R))
                visited[cur_x][cur_y-1] = True
                cnt +=1

        if cur_y < m-1 and R>0 and board[cur_x][cur_y+1] == 0:
            if visited[cur_x][cur_y+1] is False:
                q.append((cur_x,cur_y+1, L, R-1))
                visited[cur_x][cur_y+1] = True
                cnt +=1

    print(cnt)
    # for i in visited:
    #     print(*i)
    

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i,j,l,r)
            break

    