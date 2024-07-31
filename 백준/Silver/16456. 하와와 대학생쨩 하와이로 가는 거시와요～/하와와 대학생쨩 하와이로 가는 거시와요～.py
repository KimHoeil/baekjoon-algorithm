# https://www.acmicpc.net/problem/16456

import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(1)
    sys.exit()
if n == 2:
    print(1)
    sys.exit()

dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-3]) % 1000000009

print(dp[n])