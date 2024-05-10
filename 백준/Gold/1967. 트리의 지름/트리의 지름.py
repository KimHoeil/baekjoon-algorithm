# 1967번

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 노드개수 n
# 간선개수 n-1
# 1. u 부모노드번호 2. v 자식노드번호 3. w 간선의 가중치
# 트리의 지름 = 임의의 노드에서 가장 먼 (가중치가 가장 큰) 노드에서
# 가장 먼 노드 (가중치가 가장 큰) 찾기. 
# 두 노드 사이의 거리가 트리의 지름이다.


n = int(input())
visited = [False]* (n+1)
tree = [[] for i in range(n+1)] # [노드 [(연결노드,가중치)]]

for _ in range(n-1):
    u,v,w = map(int, input().split())
    tree[u].append((v,w)) # 연결노드, 가중치
    tree[v].append((u,w))


depth = [0] * (n+1)
dist = [0] * (n+1)
            
def dfs(vertex):
    visited[vertex] = True

    # 트리 깊이 우선 탐색
    for nowEndV, cost in tree[vertex]:
        if visited[nowEndV] is False:
            visited[nowEndV] = True
            
            # 트리의 지름 구하기
            dist[nowEndV] = dist[vertex] + cost
            dfs(nowEndV)


dfs(1)

maxDis = max(dist)
startNode = dist.index(maxDis)

visited = [False] * (n+1)
dist = [0] * (n+1)
dfs(startNode)

print(max(dist))