# https://www.acmicpc.net/problem/5427

import sys
from collections import deque
import copy
# input = sys.stdin.readline

t = int(input())


def goal(x, y):
    global w,h

    if 0<=x<h and 0<= y< w:
        return False
    return True


def bfs(x, y):
    dx = [-1,1,0,0] #상하좌우
    dy = [0,0, -1,1]
    global w,h
    global building
    global fireq
    
    dis = [[0 for j in range(w)] for i in range(h)]

    # for d in dis:
    #     print(d)

    escapeq = deque([])
    escapeq.append((x,y))
    fireCopyq = deque([])
    escapeCopyq= deque([])

    while escapeq or fireq:
        fireCopyq = deque([])
        escapeCopyq= deque([])

        while fireq:
            firex, firey = fireq.popleft()
            for i in range(4):
                # 불이 먼저 번짐
                    firenx = firex + dx[i]
                    fireny = firey + dy[i] 

                    if 0<= firenx < h and 0<= fireny < w:
                        if building[firenx][fireny] == '.':
                            # print("firenx:", firenx, "fireny:",fireny)
                            building[firenx][fireny] = '*'
                            fireCopyq.append((firenx,fireny))
                    
                        if building[firenx][fireny] == '@':
                            building[firenx][fireny] = '*'
                            fireCopyq.append((firenx,fireny))


        while escapeq:
            x, y = escapeq.popleft()
            for j in range(4):
                # 상근이가 이동함
                nx = x + dx[j]
                ny = y + dy[j]

                if goal(nx,ny):
                    # print("escape sucess!!")
                    print(dis[x][y]+1)
                    # for i in building:
                    #     print(i)
                    return
                
                if building[nx][ny] == '.':
                    building[nx][ny] = '@'
                    dis[nx][ny] = dis[x][y] + 1
                    escapeCopyq.append((nx,ny))

        escapeq = copy.deepcopy(escapeCopyq)
        fireq = copy.deepcopy(fireCopyq)
        # if fireFlag == True and moveFlag == False:
        #     print("IMPOSSIBLE")
        #     return
            
    print("IMPOSSIBLE")

for _ in range(t):
    w, h = map(int, input().split())
    
    building = []
    for _ in range(h):
        building.append(list(map(str, input())))

    # for i in building:
    #     print(i)
    

    fireq = deque([])
    visited = [[False for j in range(w)] for i in range(h)]
    sx = 0
    sy = 0
    for i in range(h):
        for j in range(w):
            if building[i][j] == '@':
                # print("im sangun")
                sx = i 
                sy = j 
            if building[i][j] == '*':
                # print("im fire")
                fireq.append((i,j))
                visited[i][j] = True
                
    bfs(sx,sy)