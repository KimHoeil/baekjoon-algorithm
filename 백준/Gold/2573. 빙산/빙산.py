# 빙산 골드4

import sys
import copy
from collections import deque

n,m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

def vaild(x:int, y:int):
    global n,m
    if x>=0 and x <n and y>=0 and y<m: return True
    return False

def BFS(arr):
    d = [(0,1),(0,-1),(1,0),(-1,0)] # 동서남북 (x,y)

    check_arr = copy.deepcopy(arr)
    # copyQ = deque()

    q = deque()
    # 빙산의 좌표 위치 큐에 삽입
    for i in range(n):
        for j in range(m):
            if arr[i][j] !=0:
                q.append((i,j))

    while len(q) !=0:
        front = q.popleft()
        x = front[0]
        y = front[1]

        # 빙산의 동서남북 방향 체크
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            # 바닷물이 인접해있으면 빙산이 1씩 녹아내림
            if vaild(nx,ny) and check_arr[nx][ny] ==0:
                if arr[x][y] != 0:
                    arr[x][y] -=1
        
        # 빙산이 다 녹지 않았으면 다시 큐에 삽입해줌
        # if arr[x][y] !=0:
        #     copyQ.append((x,y))
    
    # q = copy.deepcopy(copyQ)

def BFS_check(r:int, c:int, visited,arr):
    d = [(0,1),(0,-1),(1,0),(-1,0)] # 동서남북 (x,y)

    checkQ = deque()
    checkQ.append((r,c))

    visited[r][c] = True

    while len(checkQ) !=0:
        front = checkQ.popleft()
        x = front[0]
        y = front[1]

        # 빙산의 동서남북 방향 체크
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]

            # 빙산의 덩어리 체크
            if vaild(nx,ny) and arr[nx][ny] !=0 and visited[nx][ny]==False:
                visited[nx][ny] =True
                checkQ.append((nx,ny))


yearCnt = 0
while True:
    visited = [[False]*m for _ in range(n)]
    yearCnt +=1
    BFS(arr)

    # 빙산이 녹는 경우 체크
    icebergCnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and visited[i][j]==False:
                icebergCnt +=1
                BFS_check(i,j,visited,arr)

    # print("iceberg=", icebergCnt)
    # 빙산이 2덩어리 이상이면 종료
    if icebergCnt >= 2:
        print(yearCnt)
        break
    if icebergCnt ==0:
        print(0)
        break
    
