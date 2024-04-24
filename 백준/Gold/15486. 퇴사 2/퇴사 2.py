import sys

input = sys.stdin.readline


N = int(input())  # 전체 상담 개수
T = []  # 각 상담을 완료하는데 걸리는 기간
P = []  # 각 상담을 했을 때 받을 수 있는 금액
dp = [0] * (N + 1)  # DP를 위한 배열, 초기값은 0으로 설정

# 상담 기간과 금액 정보 입력 받기
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# Bottom-Up 방식으로 DP 배열 갱신
for i in range(1, N + 1):
    if i + T[i - 1] <= N + 1:  # 상담이 퇴사일을 넘지 않을 경우
        dp[i + T[i - 1] - 1] = max(dp[i + T[i - 1] - 1], dp[i - 1] + P[i - 1])
    dp[i] = max(dp[i], dp[i - 1])  # 상담을 하지 않는 경우

# 최대 수익 출력
print(dp[N])
