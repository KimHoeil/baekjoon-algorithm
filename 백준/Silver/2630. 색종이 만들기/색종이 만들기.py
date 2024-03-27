# 색종이 만들기

import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline
n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]

wCnt, bCnt = 0,0

def div_conq(x,y,N):
     global wCnt, bCnt
     tmpCnt = 0
     for i in range(x, x+N):
          for j in range(y, y+N):
               if B[i][j]:
                    tmpCnt +=1

     if not tmpCnt: # 하얀색 종이가 있으면 카운트 증가
          wCnt +=1
     elif tmpCnt == N**2: # 파란색 종이가 있으면 카운트 증가
          bCnt+=1

     else: # 분할정복해서 최소단위가 나올때까지 탐색
          div_conq(x,y, N//2)
          div_conq(x+N//2, y, N//2)
          div_conq(x,y+N//2, N//2)
          div_conq(x+N//2, y+N//2, N//2)
     return

div_conq(0,0,n)
print(wCnt)
print(bCnt)