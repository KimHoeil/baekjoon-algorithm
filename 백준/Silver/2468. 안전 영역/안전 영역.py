# 안전영역

# bfs 사용

# bfs구현
# 큐 선언
# bfs함수 생성
# q가 비어있지 않을때까지 반복
# 노드에 인접한 노드를 모두 큐에 삽입
# 비의양 = 1부터 높이n까지 모든 경우 조사

import sys
import copy
from collections import deque


# sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())
arr = []
visited = [[False for j in range(n)] for i in range(n)]
for i in range(n):
     arr.append(list(map(int, sys.stdin.readline().split())))
copyArr = copy.deepcopy(arr)

# 상하좌우 탐색
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def vaild(x,y):
     if x>=0 and x <n and y>=0 and y<n:
          return True
     return False

def bfs(r,c):
     global arr
     global dx,dy,n
     q = deque()
     q.append((r,c))

     arr[r][c] = 0
     # 큐가 비어있지 않으면 실행
     while len(q) != 0:
          curRow, curCol = q.popleft()
          
          # 현재 위치에서 상하좌우 탐색
          for i in range(4):
               nextRow = curRow + dx[i]
               nextCol = curCol + dy[i]
               # 배열의 범위가 유효하면
               if vaild(nextRow, nextCol):
                    # 침수가 안됬으면 큐에 삽입
                    if arr[nextRow][nextCol] !=0:
                         arr[nextRow][nextCol] = 0
                         q.append((nextRow,nextCol))

     # for i in arr:
     #      print(*i)
     # print()
     return
               
maxCnt=0
# 전체 비오는 높이 확인
for t in range(101):
     safeCnt = 0
     # 비보다 높이가 낮은건물 침수시키기
     for i in range(n):
          for j in range(n):
               if arr[i][j] <= t:
                    arr[i][j] = 0
     # for i in arr:
     #      print(*i)
     
     # 안전영역 개수 구하기
     for i in range(n):
          for j in range(n):
               # 침수되지 않은 영역은 안전영역으로 카운트
               if arr[i][j] != 0:                   
                    safeCnt +=1 
                    bfs(i,j) # 안전영역 테두리 확인하고 확인한곳은 침수시킴

     maxCnt = max(safeCnt,maxCnt)
     arr = copy.deepcopy(copyArr)

print(maxCnt)