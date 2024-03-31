# 플로이드-와샬 알고리즘

"""
플로이드 와샬
i부터 j까지, 1~k개의 정점을 이용하여 최단거리를 구한다.
dp를 사용하는 문제다.
n번 만큼의 단계를 반복하여 '점화식에 맞게' 2차원 리스트를 갱신하는 것

1. 현재 단계를 k번째라고 할때
현재 dist에는 1~k-1번째 정점을 사용해서 나올 수 있는 최단거리가 남아있음.
1~k의 정점을 이용하여 도달가능한 최단거리를 구함.
dp이므로 과거의 값을 이용하여 다음 값을 구하는 방식

2. 점화식
두 정점 i,j에 대해 k번 정점을 지나가면서 가면 최단거리가 더 짧아지는가?
즉 기존 i->j 보다 i-> k -> j가 더 짧은 최단거리를 가지는지 확인

3. 위의 점화식을 모든 (i,j)에 적용함
조건 => if (dist[i][j] > dist[i][k] + dist[k][j])
위 if문으로 판단하면서 기존보다 빨라지면 최단거리를 갱신을 한다.

"""
import sys
INF = int(1e9)
n= int(sys.stdin.readline())
edge = int(sys.stdin.readline())
dist = [[INF for j in range(n)] for i in range(n)]

for i in range(n):
     for j in range(n):
          if i==j:
               dist[i][j] = 0

for _ in range(edge):
     u,v,w = map(int, sys.stdin.readline().split())
     if dist[u-1][v-1] !=0:
          if dist[u-1][v-1] > w:
               dist[u-1][v-1] = w
     else:
          dist[u-1][v-1] = w

def floyd(n):
     for k in range(n): # 시작부터 끝 노드까지의 경유
          for i in range(n):
               for j in range(n):
                    dist[i][j] = min(dist[i][j], (dist[i][k]+dist[k][j]))

floyd(n)
for i in range(n):
     for j in range(n):
          if dist[i][j] == INF:
               print(0, end=' ')
          else:
               print(dist[i][j])
               
