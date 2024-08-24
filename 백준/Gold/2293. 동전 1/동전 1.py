# https://www.acmicpc.net/problem/2293

import sys
input = sys.stdin.readline

n,k= map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] *(k+1)
dp[0] = 1
for i in range(n):
    for j in range(k+1):
        if j - coins[i] < 0: # 동전이 음수가 되는 경우 체크
            continue
        dp[j] = dp[j] + dp[j - coins[i]]
        
print(dp[k])