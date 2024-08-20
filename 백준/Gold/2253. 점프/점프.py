# https://www.acmicpc.net/problem/2253

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())

arr = [False for i in range(n+1)]
dp = [[1e9] * ((int((2*n)**0.5)+2)) for i in range(n+1)] 
for i in range(m):
    stone = int(input())
    arr[stone] = True


dp[1][0] = 0

for i in range(2, n+1):
    if arr[i] == True:
        continue
    for j in range(1,int((2*i)**0.5)+1):
        dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) +1

ans = min(dp[n])
if ans == 1e9:
    print(-1)
else:
    print(ans)