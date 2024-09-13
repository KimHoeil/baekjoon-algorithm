import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    goal = int(input())
    dp = [0] * (goal+1)
    dp[0] = 1

    for i in coins:
        for j in range(1, goal+1):
            if j-i < 0: continue
            dp[j] = dp[j] + dp[j-i]
    
    print(dp[goal])
                