# https://www.acmicpc.net/problem/2579

import sys
input= sys.stdin.readline

n = int(input())

score = [0] * (n+1)
for i in range(1, n+1):
    score[i] = int(input())

if n == 1:
    print(score[1])
    exit()

dp = [0] * (n+1)
dp[1] = score[1]
dp[2] = score[1] + score[2]

for i in range(3, n+1):
    score1 = dp[i-2] + score[i]
    score2 = dp[i-3] + score[i-1] + score[i]
    dp[i] = max(score1, score2)
    
print(dp[n])




