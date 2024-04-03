# 빙산

import sys
import copy
from collections import deque

n,m = map(int, sys.stdin.readline().split())
arr = []

for i in range(n):
     arr.append(list(map(int, sys.stdin.readline().split())))


def vaild(x,y):
     if 0 <= x < n and 0 <= y < m:
          return True
     return False

def bfs(arr):
     # 상하좌우
     dx = [-1,1,0,0]
     dy = [0,0,-1,1]

     checkArr = copy.deepcopy(arr)

     q = deque()

     # 빙산의 좌표 위치 큐에 삽입
     for i in range(n):
          for j in range(m):
               if arr[i][j] != 0:
                    q.append((i,j))
     
     while q:
          front = q.popleft()
          x = front[0]
          y = front[1]
          
          # 빙산의 상하좌우 방향 체크
          for i in range(4):
               nx = x + dx[i]
               ny = y + dy[i]

               # 바닷물이 인접해있으면 빙산이 1씩 녹아내림
               if vaild(nx,ny) and checkArr[nx][ny] == 0:
                    if arr[x][y] != 0:
                         arr[x][y] -=1

def bfs_check(r,c, visited, arr):
     # 상하좌우
     dx = [-1,1,0,0]
     dy = [0,0,-1,1]

     checkQ = deque()
     checkQ.append((r,c))

     visited[r][c] = True

     while checkQ:
          front = checkQ.popleft()
          x= front[0]
          y= front[1]

          # 빙산의 상하좌우 방향 체크
          for i in range(4):
               nx = x + dx[i]
               ny = y + dy[i]

               # 빙산의 덩어리 체크
               if vaild(nx,ny) and arr[nx][ny] != 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    checkQ.append((nx,ny))


yearCnt = 0
while True:
     visited = [[False]*m for _ in range(n)]
     yearCnt +=1
     bfs(arr)

     # 빙산이 녹는 경우 체크
     icebergCnt = 0
     for i in range(n):
          for j in range(m):
               if arr[i][j] != 0 and visited[i][j]==False:
                    icebergCnt +=1
                    bfs_check(i,j,visited,arr)
     
     if icebergCnt >= 2:
          print(yearCnt)
          break
     if icebergCnt == 0:
          print(0)
          break