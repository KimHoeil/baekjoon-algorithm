def knapsack():
    n, k = [int(x) for x in input().split()]
    dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

    W = [0] # 물건의 무게 리스트
    V = [0] # 물건의 가치 리스트

    for _ in range(n):
        w, v = [int(x) for x in input().split()]
        W.append(w)
        V.append(v)

    for i in range(1, n+1):
        for j in range(1, k+1):
            if j >= W[i]: # 물건을 배낭에 넣을 수 있다면
                # 현재 채우려는 배낭의 무게에서 현재 넣으려는 물건을 뺀 이전 값과,
                # 현재 물건을 넣었을 때의 값을
                # 비교해서 더 가치가 큰값을 저장함.
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W[i]] + V[i])
            else:
                dp[i][j] = dp[i-1][j]

    print(dp[n][k])

knapsack()


