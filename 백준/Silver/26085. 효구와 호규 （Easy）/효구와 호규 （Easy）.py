# 26085번

import sys

input = sys.stdin.readline

n,m = map(int, input().split())

arr = []
for _ in range(n):
     arr.append(list(map(int, input().split())))




# n x m 이 홀수인경우 
size = n*m
if size%2 == 1:
     print(-1)
     exit()

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt0 = 0
cnt1 = 0
# n x m 이 짝수인 경우
for i in range(n):
     for j in range(m):
          if arr[i][j] == 0: cnt0+=1
          if arr[i][j] == 1: cnt1+=1
          
# 0또는 1의 개수가 홀수 인 경우          
if cnt0 %2 ==1 or cnt1 %2 ==1:
     print(-1)
     exit()


for i in range(n):
     for j in range(m):
          for k in range(4):
               nx = i + dx[k]
               ny = j + dy[k]

               if 0<= nx < n and 0<= ny < m:
                    if arr[nx][ny] == arr[i][j]:
                         print(1)
                         exit()

print(-1)
