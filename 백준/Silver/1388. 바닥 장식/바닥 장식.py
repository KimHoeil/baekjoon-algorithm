import sys
input = sys.stdin.readline


n,m = map(int, input().split())
board = [list(map(str, input().rstrip())) for i in range(n)]
# print(board)

cnt =0
def dfs(x,y,shape, dx, dy):
    board[x][y] = '0'
    
    nx = x + dx
    ny = y + dy
    if 0<=nx<n and 0<=ny<m:
        if board[nx][ny] == shape:
            board[nx][ny] = '0'
            dfs(nx,ny,shape, dx, dy)
                

for i in range(n):
    for j in range(m):
        if board[i][j] == '-':
            dfs(i,j, '-', 0,1)
            cnt+=1
        elif board[i][j] == '|':
            dfs(i,j, '|', 1,0)
            cnt+=1

                
print(cnt)