import sys
import copy

n = int(sys.stdin.readline())

arr = [[0 for j in range(n)] for i in range(n)]
visited = [[False for j in range(n)] for i in range(n)]

def vaild(x,y)->bool:
    if x>=0 and x < n and y>=0 and y <n: return True
    return False

def attackRangeSet(r, c):
    
    # 아래 탐색 불가 설정하기
    for i in range(r,n):
        if vaild(i,c):
            visited[i][c] = True
            # 퀸에 번호를 매겨서 범위 설정하기
            if arr[i][c] == 0:
                arr[i][c] = c+1

    leftDownColumn = copy.deepcopy(c)

    # 좌하 탐색 불가 설정하기
    for i in range(r,n):
        if vaild(i,leftDownColumn):
            visited[i][leftDownColumn] = True
            # 퀸에 번호를 매겨서 범위 설정하기
            if arr[i][leftDownColumn] == 0:
                arr[i][leftDownColumn] = c+1
            leftDownColumn -= 1

    rightDownColumn = copy.deepcopy(c)

    # 우하 탐색 불가 설정하기
    for i in range(r,n):
        if vaild(i,rightDownColumn):
            visited[i][rightDownColumn] = True
            # 퀸에 번호를 매겨서 범위 설정하기
            if arr[i][rightDownColumn] == 0:
                arr[i][rightDownColumn] = c+1            
            rightDownColumn +=1

def attackClear(r, c):

    # 아래 탐색 불가 해제하기
    for i in range(r,n):
        if vaild(i,c):
            # 퀸에 번호를 매겨서 범위 해제하기
            if arr[i][c] == c+1:
                arr[i][c] = 0
                visited[i][c] = False

    leftDownColumn = copy.deepcopy(c)

    # 좌하 탐색 불가 해제하기
    for i in range(r,n):
        if vaild(i,leftDownColumn):
            # 퀸에 번호를 매겨서 범위 해제하기
            if arr[i][leftDownColumn] == c+1:
                arr[i][leftDownColumn] = 0
                visited[i][leftDownColumn] = False
            leftDownColumn -= 1

    rightDownColumn = copy.deepcopy(c)

    # 우하 탐색 불가 해제하기
    for i in range(r,n):
        if vaild(i,rightDownColumn):
            # 퀸에 번호를 매겨서 범위 해제하기
            if arr[i][rightDownColumn] == c+1:
                arr[i][rightDownColumn] = 0
                visited[i][rightDownColumn] = False
            rightDownColumn +=1


def dfs(r, depth:int)->int:

    count =0

    if depth == n:
        return 1
    
    # 이미 탐색하고 지나온곳은 스킵
    for i in range(r, n):
        for j in range(n):

            # 퀸을 못놓는 조건문 자리
            if visited[i][j] == False:
                arr[i][j] = j+1
                visited[i][j] = True
                attackRangeSet(i,j)

                # for k in arr:
                #     print(k)
                # print()

                # for k in visited:
                #     print(k)
                # print()

                count += dfs(i+1, depth+1)

                arr[i][j] = 0
                visited[i][j] = False
                attackClear(i,j)

        break # 한 줄 다 탐색했으면 다음 열 탐색 (첫째줄 기준 탐색이므로)
                
    return count

print(dfs(0,0))
                

