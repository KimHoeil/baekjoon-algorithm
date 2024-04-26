# 1913번

import sys

input = sys.stdin.readline

n = int(input())
location = int(input())

snail = [[0 for i in range(n)] for j in range(n)]

def vaild(x, y):
     if 0<=x < n and 0<= y < n:
          return True
     return False


def simulation(x, y):
     ansX, ansY = 0,0
     # 하우상좌
     dx = [1,0,-1,0]
     dy = [0,1,0,-1]

     snail[x][y] = n*n

     direction = 0
     nx = x+dx[direction]
     ny = y+dy[direction]

     # 찾고자하는 위치 좌표 저장
     if location == snail[x][x]:
          ansX, ansY = 1,1

     # 달팽이 숫자를 역순으로 출력하기
     while True:
          # 배열 범위가 유효하고 달팽이 몸통이 아니면 출력
          if vaild(nx,ny) and snail[nx][ny] == 0:
               snail[nx][ny] = snail[x][y] -1

               # 찾고자하는 위치 좌표 저장
               if location == snail[nx][ny]:
                    ansX, ansY = nx+1, ny+1

               x, y = nx, ny
               nx = x+dx[direction]
               ny = y+dy[direction]


          # 벽을 만나거나 달팽이 몸통을 만나면 방향 전환
          else:
               direction +=1
               direction = direction % 4 # 4방향을 계속 사용하기 위해서 모듈러 연산 사용
               nx = x + dx[direction]
               ny = y + dy[direction]

               if snail[nx][ny] != 0: # 방향을 바꿨는데도 달팽이 몸통이면 더이상 이동할 곳이 없으므로 종료
                    break

     for i in snail:
          print(*i)
     
     print(ansX, ansY)


simulation(0, 0)



     