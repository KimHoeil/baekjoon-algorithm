# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

n = int(input())
board=[]
for _ in range(n):
    board.append(list(map(int, input().split())))


whiteCnt = 0
blueCnt = 0
def paper_cut(r,c,n):
    global whiteCnt
    global blueCnt
    tmpCnt =0
    for i in range(r, r+n):
        for j in range(c, c+n):
            if board[i][j]:
                tmpCnt +=1
    
    if not tmpCnt: # 하얀색 종이이면
        whiteCnt +=1
    elif tmpCnt == n**2: # 파란색 종이이면
        blueCnt +=1
    else: # 최소 단위가 나올때까지 분할정복
        half = n // 2
        paper_cut(r,c,half)
        paper_cut(r, c+half, half)
        paper_cut(r+half, c, half)
        paper_cut(r+half, c+half, half)
    


paper_cut(0,0,n)
print(whiteCnt)
print(blueCnt)
    