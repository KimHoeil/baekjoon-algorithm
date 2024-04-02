# 동전찾기2
# 아아....한 80% 생각해냈는데....

import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

coinWallet = []
for i in range(n):
     coin = int(sys.stdin.readline())
     coinWallet.append(coin)

# dp배열 초기화
dp = [float('inf')]* (k+1)
dp[0] = 0

def bfs():
     q = deque([0])

     while q:
          front = q.popleft()
          
          for i in range(n):
               coin = front + coinWallet[i]

               # 새로운 금액에 도달하는 데 필요한 동전의 개수가 현재까지의 최소 개수보다 작을 경우에만 갱신
               if coin <=k and dp[coin] > dp[front] +1:
                    q.append(coin)
                    dp[coin] = dp[front] + 1

               
bfs()
print(dp[k] if dp[k] != float('inf') else -1)