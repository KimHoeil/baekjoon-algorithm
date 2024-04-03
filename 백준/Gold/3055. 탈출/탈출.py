# 탈출

import sys
from collections import deque

MAX = 52

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def valid(x,y):
     if 0<=x <r and 0<= y <c: return True
     return False

check = False
r,c = map(int, sys.stdin.readline().split())

# 티떱숲 지도 초기화
arr = []
waterq = deque()
copyWaterq = deque()
sq = deque()
copySq = deque()

for i in range(r):  
     arr.append(list(input()))

     for j in range(c):
          if arr[i][j] == '*':
               waterq.append((i,j))
          elif arr[i][j] == 'S':
               sq.append((i,j))

cnt =1
dis = [[0 for j in range(MAX)] for i in range(MAX)]

while True:
     # 고슴도치가 비버굴에 도착하는 경로
     while sq:
          x,y = sq.popleft()

          if arr[x][y] == '*':
               continue
          else:
               for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if valid(nx,ny) and arr[nx][ny] == '.':
                         arr[nx][ny] ='S'
                         dis[nx][ny] =dis[x][y] +1
                         copySq.append((nx,ny))
                    elif valid(nx,ny) and arr[nx][ny] == 'D':
                         check = True
                         dis[nx][ny] = dis[x][y]+1
                         sq = deque()
                         copySq = deque()
                         break
          
     sq, copySq = copySq, sq

     # 물이 상하좌우로 퍼지는 마법
     while waterq:
          x,y = waterq.popleft()

          for i in range(4):
               nx = x + dx[i]
               ny = y + dy[i]

               # 상하좌우에 물 범람하기
               if valid(nx,ny) and arr[nx][ny] == '.':
                    arr[nx][ny] = '*'
                    copyWaterq.append((nx,ny))
               elif valid(nx,ny) and arr[nx][ny] == 'S':
                    arr[nx][ny] = '*'
                    copyWaterq.append((nx,ny))
     
     waterq, copyWaterq = copyWaterq, waterq
     cnt +=1
     if len(sq) ==0: break

if check == False: print('KAKTUS')
else:
     for i in range(r):
          for j in range(c):
               if arr[i][j] == 'D':
                    print(dis[i][j])


