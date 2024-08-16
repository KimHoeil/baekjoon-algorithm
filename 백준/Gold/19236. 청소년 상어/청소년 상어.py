# https://www.acmicpc.net/problem/19236

import sys
import heapq
import copy

input = sys.stdin.readline

board = [[] for _ in range(4)]

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1] # 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

# 배열에 3차원 배열로 물고기 [번호, 방향] 입력받기
for i in range(4):
    inputList = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([inputList[j*2], inputList[j*2+1]])
    board[i] = fish 

shark = []
max_score = 0

def shark_move(board, score, x, y):
    global max_score

    # 상어턴 => 물고기 먹고 방향습득
    fish = board[x][y]
    if fish[1] != 0 and fish[1] != -1:
        shark = [x,y, fish[1]]
        score += fish[0] # 물고기 번호 증가
        board[x][y] = [-1,-1] # 상어있다는 표시
    else:
        return
    
    copy_board = copy.deepcopy(board)
    max_score = max(score, max_score)

    # 물고기턴 => fish_move()
    fish_move(copy_board)

    # 물고기 이동하고 원래 보드 업데이트해놓음!!
    board = copy.deepcopy(copy_board)

    # 상어턴 => 3군데중 한군데 조건에 맞으면 이동
    for i in range(3): # 상어는 최대 3곳으로 이동가능

        # 방향에 따라 증감값이 다른것을 처리해줌
        if dx[shark[2]] == -1: nx = shark[0] + dx[shark[2]] - i
        if dx[shark[2]] == 1: nx = shark[0] + dx[shark[2]] + i
        if dy[shark[2]] == -1: ny = shark[1] + dy[shark[2]] - i
        if dy[shark[2]] == 1: ny = shark[1] + dy[shark[2]] + i
        if dx[shark[2]] == 0: nx = shark[0]
        if dy[shark[2]] == 0: ny = shark[1]

        if 0 <= nx < 4 and 0 <= ny < 4: # 유효한 공간이면
            if copy_board[nx][ny] != [0,0]:        # 빈공간이 아니면
                copy_board[x][y] = [0,0]           # 상어가 이동하면서 빈공간처리
                shark_move(copy_board, score, nx, ny)
                # dfs 탐색 끝나고, 이전 상태의 보드에서 다시 탐색 시작
                copy_board = copy.deepcopy(board) 

def fish_move(board):

    for l in range(1,17):
        flag = False
        flag2 = False
        for i in range(7):
            for j in range(4):
                for k in range(4):
                    if board[j][k][0] == l:
                        nx = j + dx[board[j][k][1]]
                        ny = k + dy[board[j][k][1]]

                        if 0<= nx < 4 and 0<= ny < 4 and board[nx][ny] != [-1,-1]:
                            if board[nx][ny] == [0,0]: # 빈공간이면
                                board[nx][ny] = [board[j][k][0], board[j][k][1]]
                                board[j][k] = [0,0]
                                flag = True
                                break
                            else: # 물고기가 있으면 swap
                                board[nx][ny], board[j][k] = [board[j][k][0], board[j][k][1]], board[nx][ny]
                                flag = True
                                break

                        else: # 상어, 바깥이라 못움직이면 방향 change
                            if board[j][k][1] >= 8:
                                board[j][k][1] = 1
                            else: 
                                board[j][k][1] += 1
                if flag == True:
                    flag2 = True
                    break

            if flag2 == True:
                break
    
shark_move(board, 0, 0, 0)
print(max_score)