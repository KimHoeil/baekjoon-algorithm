# 토마토 3차원 격자 골드 5 bfs
# 아아... 토마토가 있는 곳의 좌표를 큐에 삽입했어야 하는구남..
# dequq vs list q 시간복잡도 차이... 구조에 대해서 알아봐야할듯. O(1) vs O(N) 차이나네..

import sys
import copy
from collections import deque


m,n,h = map(int, sys.stdin.readline().split())
tomatoArr = []
d = [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)] # 위,아래,왼쪽,오른쪽,앞,뒤 (h,x,y)
visited = [[[False for k in range(m)] for j in range(n)] for i in range(h)]
# dis = [[[0 for k in range(m)] for j in range(n)] for i in range(h)]
q = deque()

def vaild(H:int, x:int, y:int)->bool:
    global m,n,h
    if x>=0 and x<n and y >=0 and y<m and H>=0 and H<h: return True
    return False

def BFS():
    global visited
    global tomatoArr
    global d,q
    global dis

    # 익은 토마토 정보 초기화
    for info in q:
        visited[info[0]][info[1]][info[2]] = True
        dis[info[0]][info[1]][info[2]] = 1

    while len(q) != 0:
        front = q.popleft()

        cur_h = front[0]
        cur_r = front[1]
        cur_c = front[2]

        # 위,아래,왼쪽,오른쪽,앞,뒤 (h,x,y)
        for i in range(6):
            nh = cur_h + d[i][0]
            nx = cur_r + d[i][1]
            ny = cur_c + d[i][2]

            # 토마토가 존재하고 익지 않았으면 익히기
            if vaild(nh,nx,ny) and visited[nh][nx][ny] == False and tomatoArr[nh][nx][ny] == 0:
                visited[nh][nx][ny] = True
                tomatoArr[nh][nx][ny] = 1
                dis[nh][nx][ny] = dis[cur_h][cur_r][cur_c] +1
                q.append((nh,nx,ny))
                

# arr = [[0 for _ in range(m)] for _ in range(n)]
# copy_arr = copy.deepcopy(arr)
# 3차원 배열로 모델링
for i in range(h):
    arr = []
    for j in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
        for k in range(len(arr[j])):
            if arr[j][k]==1:
                q.append((i,j,k))
    tomatoArr.append(arr)
    # arr = copy.deepcopy(copy_arr)

dis = copy.deepcopy(tomatoArr)
BFS()
# t==0이면 토마토가 익지 못하는 상황이므로 -1 출력하고 종료
# t==0이 아니면 토마토가 모두 익는데 걸리는 날짜를 출력
cnt = 0
for tomatoH in dis:
    for tomatoN in tomatoH:
        # print(tomatoN)
        for tomatoM in tomatoN:
            if tomatoM ==0:
                print(-1)
                exit()
            if cnt < tomatoM:
                cnt = tomatoM
            # cnt = max(cnt,tomatoM)
print(cnt-1)


# c++식 코딩 버전... 
# cnt = 0
# for H in range(len(tomatoArr)):
#     for N in range(len(tomatoArr[H])):
#         print(dis[H][N])
#         for M in range(len(tomatoArr[H][N])):
#             if tomatoArr[H][N][M] ==0:
#                 print(-1)
#                 exit()
#             cnt = max(cnt,dis[H][N][M])
# print(cnt-1)

        

