# dfs와 bfs 실버2 그래프 탐색
# 그렇군...여전히 알고리즘에 대한 내 이해도가 부족했던 탓이였어...
# 정점만 탐색하면 되는것이 목적인데 depth를 꼭 써야한다고 생각햇던 내 불찰이군..


import sys
import copy

n,m,v = map(int, sys.stdin.readline().split())
adj = [[] for i in range(n)]
visited = [False] * n
copy_visited = copy.deepcopy(visited)
resultArr = [0] * n
vertexCheckArr = [False] * n


def DFS(vertex:int):
    global n
    visited[vertex] = True

    print(vertex+1, end=' ')
    
    for i in adj[vertex]:
        if visited[i] ==False:
            visited[i] =True
            DFS(i)

def BFS(vertex:int):
    global n

    q = []
    q.append(vertex)
    
    depth = [0] * n
    visited[vertex] = True

    while len(q) !=0:
        front = q.pop(0)
        print(front+1, end=' ')

        # adj[front].sort()
        for nowEndV in adj[front]:
            if visited[nowEndV] ==False:
                q.append(nowEndV)
                visited[nowEndV] = True
    
for i in range(m):
    s,e = map(int, sys.stdin.readline().split())
    adj[s-1].append(e-1)
    adj[e-1].append(s-1)

    # 사용하는 정점 체크
    vertexCheckArr[s-1] = True
    vertexCheckArr[e-1] = True

dfsCnt = 0
# 방문할 정점을 작은 순서대로 정렬하기
for i in range(n):
    adj[i].sort()
    if vertexCheckArr[i] ==True:
        dfsCnt +=1

# for i in adj:
#     print(i)

DFS(v-1)
print()
visited = copy.deepcopy(copy_visited)
BFS(v-1)