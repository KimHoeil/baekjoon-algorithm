# 계단오르기
import sys

input = sys.stdin.readline

n = int(input())
score = [0] + [int(input()) for _ in range(n)]
dp = [[0]*3 for _ in range(n+1)]

dp[1][1] = score[1]

for i in range(2, n+1):
    # 바로 전계단을 밟지 않고 올라온 경우
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + score[i]
    # 바로 전계단을 밟고 올라온 경우
    dp[i][2] = dp[i-1][1] + score[i]

print(max(dp[n][1], dp[n][2]))
