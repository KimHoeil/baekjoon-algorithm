# 외판원 순회2

# 그래프를 만들어서 도시 맵 정의
# 2차원 배열?
# adj[1][1] = 0
# adj[1][2] = 10
# 인접리스트로 그래프 정의해보자.....dmmm으하하아가아아강
# 백트래킹 구현하면 무조건 풀린다!

import sys
import math

# sys.stdin = open("input.txt", "r")
n = int(sys.stdin.readline())

# visited = [[True for j in range(n)] for i in range(n)]
visited = [False] * n
costArr = []

# 도시 이동비용 초기화
for i in range(n):
    costArr.append(list(map(int, sys.stdin.readline().split())))

adjList = []

for i in range(n):
    adjList.append([])
    for j in range(n):
        # 갈 수 있는 도시이면 도시간 인접리스트에 추가
        if costArr[i][j] != 0:
            adjList[i].append(j)

# for i in adjList:
#     print(i)

minCost = sys.maxsize
# print(minCost)


# 외판원 순회 함수
def dfs(start, vertex, depth, cost):
    global adjList
    global visited
    global costArr
    global n
    global minCost

    if depth == n:
        if costArr[vertex][start] != 0:
            cost = cost + costArr[vertex][start]
            # print("cost=", cost)
            if minCost > cost:
                minCost = cost
            #     return
            # else:
            #     if minCost > cost:
            #         minCost = cost
        return

    for v in adjList[vertex]:
        # 인접 도시를 방문하지 않았다면 방문
        if visited[v] == False:
            visited[v] = True
            cost = cost + costArr[vertex][v]
            dfs(start, v, depth + 1, cost)
            visited[v] = False
            cost = cost - costArr[vertex][v]

    #     print(v, end=" ")
    # print(":", vertex + 1, "번째 도시와 인접한 도시 목록 출력")
    # print(minCost)
    # print()


for i in range(n):
    visited[i] = True
    dfs(i, i, 1, 0)
    visited[i] = False

print(minCost)
