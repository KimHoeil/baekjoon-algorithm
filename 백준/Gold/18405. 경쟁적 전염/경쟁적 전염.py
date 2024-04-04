# 경쟁적 전염

import sys
import copy
from collections import deque

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def valid(x,y):
     if 0<= x <n and 0<=y<n: return True
     return False


def bfs():
    q = deque()
    q.append((0,0))


    if testTube[0][0] !=0:
          virusList[testTube[0][0]-1].append((0,0)) # 바이러스 번호와 좌표값 저장
          visited[0][0] = True
    else:
          visited[0][0] = True
     

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 배열의 유효 범위이고, 방문하지 않았고, 바이러스가 존재하면 바이러스큐에 삽입
            if valid(nx,ny) and visited[nx][ny] is False and testTube[nx][ny] !=0:
                 visited[nx][ny] = True
                 q.append((nx,ny))
                 virusList[testTube[nx][ny]-1].append((nx,ny))

            # 바이러스가 존재하지 않는다면 계속 탐색
            elif valid(nx,ny) and visited[nx][ny] is False and testTube[nx][ny] ==0:
                 visited[nx][ny] = True
                 q.append((nx,ny))
     

n,k = map(int, sys.stdin.readline().split())
testTube = []
virusList = [[] for _ in range(k)]
newvirusList = [[] for _ in range(k)]


visited = [[False for j in range(n)] for i in range(n)]

for i in range(n):
     v = list(map(int, sys.stdin.readline().split()))
     testTube.append(v)


# S초, X행, Y열
S,X,Y = map(int, sys.stdin.readline().split())

bfs()

for i in range(S):
     for j in range(k):
          if len(virusList[j]) != 0: # 바이러스 공간이 비어있지 않다면
               for virus in virusList[j]: 

                    vx = virus[0]
                    vy = virus[1]

                    for i in range(4):
                         dvx = vx + dx[i]
                         dvy = vy + dy[i]

                         if valid(dvx,dvy) and testTube[dvx][dvy] ==0:
                              # 바이러스가 필드에 전염될때는 인덱스번호+1로 처리해줘야한다..(코드 리뷰어가 디버깅해줌)
                              testTube[dvx][dvy] = j+1 
                              newvirusList[j].append((dvx,dvy))

     # 새로 생성한 바이러스 리스트와 기존 바이러스 리스트 swap
     virusList, newvirusList = newvirusList, virusList
     newvirusList = [[] for _ in range(k)] # 임시 바이러스 리스트는 초기화
     

# print(testTube)

if testTube[X-1][Y-1] != 0:                    
     print(testTube[X-1][Y-1])
else: print(0)
