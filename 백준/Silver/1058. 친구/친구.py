# 친구 실버2 2023 백엔드 직군 토스기출 2번
# bfs버전

import sys
import copy

n = int(sys.stdin.readline())
adj = [[] for i in range(n)]
friend_list = [] # 탐색하고자하는 사람의 2- 친구 관계 리스트
visited = [False] * n
Max = 0

def bfs(vertex:int, adj)->int:
    global Max
    global friend_list
    global visited

    q = []
    q.append(vertex)
    depth = [0] * n

    visited[vertex] = True

    while len(q) != 0:
        front = q.pop(0)
        
        # print(front, visited[front])
        # print(visited)

        if depth[front] == 2:
            continue
        
        for nowEndV in adj[front]:
            # print(nowEndV, visited[nowEndV])
            if visited[nowEndV] ==False:
                visited[nowEndV] =True
                depth[nowEndV] = depth[front] + 1
                q.append(nowEndV)
                if nowEndV not in friend_list:
                    friend_list.append(nowEndV)
        # print(friend_list)

    
    return len(friend_list)


for i in range(n):
    inp = list(input())

    for j in range(len(inp)):
        if inp[j] == 'Y':
            adj[i].append(j)

# for i in adj:
#     print(i)
# print()

# 1~n번의 사람 친구 관계 조사하기
for i in range(n):
    count = bfs(i,adj)
    Max = max(Max, count)
    # print(friend_list)
    friend_list.clear()
    for i in range(n):
        visited[i] = False
# print(bfs(0,adj))
print(Max)


