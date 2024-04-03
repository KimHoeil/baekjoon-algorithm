# 게임 개발 골드3 위상정렬, 디피

import sys
import copy

n = int(sys.stdin.readline())
adj = [[] for i in range(n)]
buildingArr = [[] for i in range(n)]
inDegree = [0] * n
buildTime = [0] * n
dp = [0] * n

def Max(a:int, b:int):
    if a < b: return b
    return a

def topologiSort():

    global adj
    global inDegree
    global buildTime
    global dp
    global n

    q = [] # 리스트를 큐로 사용

    # 들어오는 간선이 없는 정점부터 순회하기
    for i in range(n):
        if inDegree[i] ==0:
            q.append(i)
    
    # 완전한 전체 순회를 위해 n번 반복
    for i in range(n):  

        if len(q) ==0:
            return

        front = q.pop()

        # 건물은 동시에 짓기도 가능하므로 먼저 지어야하는 건물중
        # 시간이 더 많이 소요되는 건물만 건설 시간에 추가해준다.
        for nowEndV in adj[front]:
            inDegree[nowEndV] -=1

            if inDegree[nowEndV] ==0:
                q.append(nowEndV)
        
        undoMaxTime = 0
        for i in buildingArr[front]:
            undoMaxTime = Max(undoMaxTime, dp[i])

        dp[front] = copy.deepcopy(buildTime[front]+ undoMaxTime)
        #print(dp[front])
        
for i in range(n):
    input = list(map(int, sys.stdin.readline().split()))
    buildTime[i] = copy.deepcopy(input[0]) # 건물 짓는 시간 입력받기
    dp[i] = copy.deepcopy(input[0])

    # 위상 정렬 그래프식으로 입력받기
    for j in range(1,len(input)-1):
        adj[input[j]-1].append(i)
        buildingArr[i].append(input[j]-1)
        inDegree[i] +=1

#print(adj)
#print(buildingArr)
#print(inDegree)
#print(buildTime)
topologiSort()

for i in range(n):
    print(dp[i])