import sys

# 행렬의 개수 N과 각 행렬의 크기를 나타내는 배열 matrix_sizes를 입력받습니다.
N = int(input())
matrix_sizes = [list(map(int, input().split())) for _ in range(N)]

# print(matrix_sizes)
# 최소 곱셈 연산 횟수를 저장할 2차원 배열 dp를 초기화합니다.
dp = [[0 if i == j else float('inf') for j in range(N)] for i in range(N)]

# dp[i][j]는 행렬 i부터 j까지 곱했을 때 필요한 최소 곱셈 연산 횟수입니다.
for chain_len in range(1, N):
    for i in range(N - chain_len):
        j = i + chain_len
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + matrix_sizes[i][0] * matrix_sizes[k][1] * matrix_sizes[j][1]
            if cost < dp[i][j]:
                dp[i][j] = cost

# 모든 행렬을 곱하는데 필요한 최소 곱셈 연산 횟수를 출력합니다.
print(dp[0][N-1])
# for d in dp:
#     print(d)