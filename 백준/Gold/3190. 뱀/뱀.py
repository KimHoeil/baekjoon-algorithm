import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [[0 for j in range(n)] for i in range(n)]
k = int(input())
for _ in range(k):
    x,y = map(int, input().split())
    board[x-1][y-1] = 1
l = int(input())
info = []
for _ in range(l):
    info.append(input().split())
info.append((10001, ''))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
turnIndex = 1
cnt = 0
x,y = 0,0
snake = deque()
snake.append((0,0))
breaker = False

def turn_snake(direct):
    global turnIndex

    if direct == 'L':
        if turnIndex !=0:
            turnIndex -=1
        else:
            turnIndex = 3    

    if direct == 'D':
        if turnIndex !=3:
            turnIndex +=1
        else:
            turnIndex = 0



for i in range(len(info)):
    
    start = cnt+1
    for _ in range(start, int(info[i][0]) + 1):
        nx = x + dx[turnIndex]
        ny = y + dy[turnIndex]
        
        if 0<=nx<n and 0<=ny<n and (nx,ny) not in snake:
            x,y = nx, ny
            # 사과가 아니면
            if board[nx][ny] != 1:
                snake.append((nx,ny))
                snake.popleft()
            # 사과이면    
            else:
                snake.append((nx,ny))
                board[nx][ny] = 0
        else:
            cnt+=1
            breaker = True
            break
        cnt +=1
    
    if breaker == True:
        break
    turn_snake(info[i][1])

print(cnt)
