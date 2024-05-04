# 18429번

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
kit = list(map(int, input().split()))
result = [0]*n
visited = [False]*n
cnt = 0
weight = 500

def dfs(depth, n):
     global cnt
     global weight

     if depth == n:
          for i in result:
               if i < 500:
                    return
          #      print(i, end=' ')
          # print()
          cnt +=1
          return
     
     for i in range(len(kit)):
          if visited[i] == False:
               result[depth] = weight +kit[i] - k # 중량 증가량 계산
               weight = result[depth]
               visited[i] = True
               dfs(depth+1, n)
               visited[i] = False
               weight = weight-kit[i]+k
dfs(0,n)
print(cnt)