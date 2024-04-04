# 단지번호 붙이기 실버 1 bfs
# 시작시간 38분 start
# 아이고....이렇게 멍청했다니..ㅠㅠ
# 왜 처음부터 끝까지 보는 방법을 떠올리지 못햇을가...

import sys
import copy

n = int(input())
arr = [[] for i in range(n)]
d= [(-1,0),(1,0),(0,-1),(0,1)] # 상,하,좌,우 (x,y)
visited = [[False for j in range(n)] for i in range(n)]
ans = []

def vaild(x:int,y:int)->bool:
    if x>=0 and x <n and y>=0 and y<n: return True
    return False

def bfs(x:int, y:int):
    global dis,arr
    visited[x][y] = True
    start = (x,y)
    cnt = 1
    
    q=[]
    q.append(start)

    while len(q) != 0:
        front = q.pop(0)

        for i in range(4):
            nx = front[0] + d[i][0]
            ny = front[1] + d[i][1]

            if vaild(nx,ny) and visited[nx][ny]==False and arr[nx][ny]==1:
                arr[nx][ny] = 0
                cnt +=1
                visited[nx][ny] = True
                q.append((nx,ny))
                                
    return cnt

for i in range(n):
    ipt = list(input())
    ipt = list(map(int, ipt))
    arr[i] = ipt

dis = copy.deepcopy(arr)

dangiCnt = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] ==1:
            dangiCnt +=1
            ans.append(bfs(i,j))
print(dangiCnt)
ans.sort()
for i in ans:
    print(i)