# 뱀

import sys
from collections import deque

# sys.stdin = open('input.txt','r')

# L은 왼쪽으로 90도 회전
# D는 오른쪽으로 90도 회전
# 북동남서
direct = [(-1,0),(0,1),(1,0),(0,-1)]

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
     
board = [[0 for j in range(n)] for i in range(n)]
for i in range(k):
     r,c = map(int, sys.stdin.readline().split())
     
     board[r-1][c-1] = 1 # 사과가 있다는 표시

l = int(sys.stdin.readline())

info = []
for i in range(l):
     info.append(sys.stdin.readline().split()) # 게임정보 배열에 문자열로 저장

# print(board)
# print(info)

# 문제에서 주어진 시간은 1000초 이하로 해결
info.append((10001, ''))

# 뱀의 방향 전환
def turn_snake(direction):
     global turnIdx
     # 왼쪽으로 회전
     if direction == 'L':
          if turnIdx !=0:
               turnIdx -=1
          else:
               turnIdx = 3
     # 오른쪽으로 회전
     else:
          if turnIdx !=3:
               turnIdx +=1
          else:
               turnIdx = 0
     return

# 뱀 시작위치 초기화
snake = deque()
snake.append((0,0))

# 뱀의 기본 방향 설정          
turnIdx = 1
cnt = 0 # 게임 진행 시간
start = 1 # 방향을 바꿀 때 출발 시간
breaker = False # 반복문 탈출 명령
x,y = 0,0 # 뱀의 머리 위치

# 시물레이션
for i in range(len(info)):
     # time = int(info[0]) # 방향전환 시간
     # c = info[1]      # 방향전환 정보
     start = cnt+1
     for _ in range(start, int(info[i][0]) +1):
          # 이동할 좌표 설정
          nx = x + direct[turnIdx][0]      
          ny = y + direct[turnIdx][1]
          # 이동할 좌표가 벽 또는 자기자신의 몸과 부딪친다면 반복문 종료
          if nx<0 or nx>=n or ny<0 or ny>=n or (nx,ny) in snake:
               cnt+=1
               breaker = True
               break
          # 뱀이 이동할 다음 위치에 사과가 있다면
          if board[nx][ny] ==1:
               # 사과 먹기
               board[nx][ny] =0
               x,y = nx, ny
               # 뱀의 위치 표시
               snake.append((x,y))
          # 다음 위치에 사과가 없다면
          else:
               x,y = nx, ny
               # 뱀의 위치 표시
               snake.popleft()
               snake.append((x,y))
               # 게임 1초씩 증가
          cnt +=1

     if breaker == True:
          break
     # 뱀 이동후 방향 전환
     turn_snake(info[i][1])

print(cnt)
