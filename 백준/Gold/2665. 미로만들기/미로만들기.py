# 미로만들기

import sys
n = int(sys.stdin.readline().rstrip())
graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().rstrip())))
INF = int(1e9)
distance = [[INF] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque
def BFS():
  q = deque()
  q.append((0, 0, 0))
  distance[0][0] = 0
  while q:
    # dist = 검은방을 몇 개 부셔야 지나가는지 체크
    dist, x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < n and 0 <= ny < n:
        # 유효한 범위이면 지나가는데 필요한 검은방 개수 갱신
        cost = dist
        # 검은방 이라면 지나가기위해 부수고, 카운트를 올려줌
        if graph[nx][ny] == 0:
          cost += 1
        # 내가 검은방을 부수고 지나온 루트가 다음땅의 부수고온 개수보다 작다면 현재 값으로 갱신해줌  
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          # 검은방을 부순개수와 다음 탐색할 곳을 큐에 삽입함.
          q.append((cost, nx, ny))

BFS()
print(distance[n-1][n-1])