# 10655번
import sys
input = sys.stdin.readline

n = int(input())

distance = [0]
checkPoint = []
for _ in range(n):
     x,y = map(int, input().split())
     checkPoint.append((x,y))

for i in range(n-1):
     dist = abs(checkPoint[i][0] - checkPoint[i+1][0]) + abs(checkPoint[i][1] - checkPoint[i+1][1])
     distance.append(dist)

totalDist = sum(distance)

minDist = 1e9
for i in range(1, n-1):
     # {(전체거리 - i를 끼고 달린거리) + (i-1에서 i+1까지 달린 거리)} 
     skipDist = totalDist - (distance[i]+distance[i+1]) + \
     abs(checkPoint[i-1][0] - checkPoint[i+1][0]) + abs(checkPoint[i-1][1] - checkPoint[i+1][1])
     
     minDist = min(minDist, skipDist)

print(minDist)
