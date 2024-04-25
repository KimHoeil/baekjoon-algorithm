# 30012번

import sys

# sys.stdin = open('input.txt','r')
input = sys.stdin.readline


s,n = map(int, input().split())
E = list(map(int, input().split()))
k,l = map(int, input().split())


# print(E)

minJumpDis = k*2

distance = []
# 주호와 다른 개구리의 거리 계산
for i in E:
     dis = abs(s-i)
     distance.append(dis)
# print(distance)

costList = []
for dis in distance:
     if dis < 2*k: # 개구리간의 거리가 2k 미만인 경우
          jumpCost = 2*k - dis
          costList.append(jumpCost)

     else: # 개구리간의 거리가 2K이상이거나 2K인 경우
          walkCost = l * (dis-2*k)
          costList.append(walkCost)

minCost = min(costList)
index = costList.index(minCost) +1 
print(minCost, index)


