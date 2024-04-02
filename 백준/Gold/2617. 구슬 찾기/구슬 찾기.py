# 구슬찾기

import sys


n,m = map(int, sys.stdin.readline().split())

# 구슬 초기화 False는 가볍다는 뜻
# i,j가 True이면 구슬 i가 j보다 무겁다는 의미
weight = [[False for j in range(n)] for i in range(n)]

for i in range(m):
     a,b = map(int, sys.stdin.readline().split())
     weight[a-1][b-1] = True

def floyd():
     for k in range(n):
          for i in range(n):
               for j in range(n):
                    if weight[i][k] and weight[k][j]:
                         weight[i][j] = True

# for i in weight:
#      print(i)
# print()

floyd()

# for i in weight:
#      print(i)

heavierCnt = [0]*n # 각 구슬에 대해, 무거운 구슬의 개수를 세는 배열
lighterCnt = [0]*n # 각 구슬에 대해, 가벼운 구슬의 개수를 세는 배열

# 무거운 구슬과 가벼운 구슬의 수를 계산
"""
i번째 구슬이 j번째 구슬보다 무겁다면, i번째 구슬보다 무거운 구슬의 수를 나타내는
배열의 i번째 값을 증가시키고, j번째 구슬보다 가벼운 구슬의 수를 나타내는 배열의 j번째 값을
증가시킨다
"""
for i in range(n):
     for j in range(n):
          if weight[i][j] == True:
               heavierCnt[i] +=1
               lighterCnt[j] +=1

# print(heavierCnt)
# print(lighterCnt)

# 중간 무게가 될 수 없는 구슬의 수를 계산
impossible_count = 0
for i in range(n):
    if heavierCnt[i] >= (n+1)//2 or lighterCnt[i] >= (n+1)//2:
        impossible_count += 1

print(impossible_count)