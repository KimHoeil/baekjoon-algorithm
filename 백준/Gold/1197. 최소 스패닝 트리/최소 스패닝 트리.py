# 최소 신장 트리
# 프림 알고리즘

from collections import defaultdict
import heapq

import sys

def prim_mst(V,E):

#     mst_graph = [[0] * V for _ in range(V)]
    mst_nodes = [-1 for _ in range(V)]
    visited = [False for _ in range(V)]
#     print(mst_graph)
#     print(mst_nodes)
#     print(visited)

    pq = [(0, 1, 1)] # 시작 정점 초기화
    while pq:
        cost, node, prev = heapq.heappop(pq)
        if visited[node - 1] == True: # 방문한 정점이면 탐색 x
               continue
        
        visited[node - 1] = True
        # mst 연결 정점에 체크
     #    mst_graph[node - 1][prev - 1] = 1
     #    mst_graph[prev - 1][node - 1] = 1
        mst_nodes[node - 1] = cost

        # 연결된 정점의 간선중 가장 cost가 작은 순으로 pq(최소힙)에 정렬됨.
        for v, weight in graph[node]: 
            if visited[v - 1] == False: # 다음 정점을 방문하지 않았으면
                heapq.heappush(pq, (weight, v, node)) # 최소힙에 push

    print(sum(mst_nodes))
#     mst_graph[0][0] = 1
#     for row in mst_graph:
#         print(*row)
 

graph = defaultdict(list) # 그래프 {정점: [연결 정점,가중치]} 형식으로 입력받기

v, e = map(int, sys.stdin.readline().split())
for i in range(e):
     a,b,c = map(int, sys.stdin.readline().split())

     graph[a].append((b, c))
     graph[b].append((a, c))

# print(graph)
prim_mst(v,e)

# test = defaultdict(list)
# print(test)
# test2 = {}
# print(test2)

# test[1].append((2,6))
# test[1].append((3,3))
# test[2].append((4,5))
# test[2] = (4,5)
# print(test[1][0])