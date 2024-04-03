# 토마토

import sys
import copy
from collections import deque

m,n,height = map(int, sys.stdin.readline().split())
tomatoArr = []

visited = [[[False for k in range(m)] for j in range(n)] for i in range(height)]

def vaild(h,x,y):
     if 0 <= x <n and 0<= y < m and 0<=h <height: return True
     return False

q = deque()

def bfs():
     # 천장,바닥,상,하,좌,우 (h,x,y)
     dh = [-1,1,0,0,0,0] 
     dx = [0,0,-1,1,0,0]
     dy = [0,0,0,0,-1,1]


     # 익은 토마토 정보 초기화
     for h,x,y in q:
          visited[h][x][y] = True
          dis[h][x][y] = 1

     while q:
          h,x,y = q.popleft()

          # 천장,바닥,상,하,좌,우 (h,x,y)
          for i in range(6):
               nh = h + dh[i]
               nx = x + dx[i]
               ny = y + dy[i]

               # 토마토가 존재하고 익지 않았으면 익히기
               if vaild(nh,nx,ny) and visited[nh][nx][ny] is False and tomatoArr[nh][nx][ny] ==0:
                    visited[nh][nx][ny] = True
                    tomatoArr[nh][nx][ny] = 1
                    dis[nh][nx][ny] = dis[h][x][y] +1
                    q.append((nh,nx,ny))
          

# 3차원 배열로 모델링
for i in range(height):
     arr = []
     for j in range(n):
          arr.append(list(map(int, sys.stdin.readline().split())))
          for k in range(len(arr[j])):
               if arr[j][k] ==1:
                    q.append((i,j,k))
     
     tomatoArr.append(arr)

dis = copy.deepcopy(tomatoArr)
bfs()

# t==0이면 토마토가 익지 못하는 상황이므로 -1 출력하고 종료
# t==0이 아니면 토마토가 모두 익는데 걸리는 날짜를 출력
cnt = 0
for tomatoH in dis:
     for tomatoN in tomatoH:
          for tomatoM in tomatoN:
               if tomatoM ==0:
                    print(-1)
                    exit()
               if cnt < tomatoM:
                    cnt = tomatoM
print(cnt-1)