


import sys
input = sys.stdin.readline


while True:
     # 입력: 사탕의 종류 n, 가지고 있는 돈 m
     n, m = map(float, input().split())
     m = int(m * 100 + 0.5)  # 소수점을 정수로 변환

     if n == 0.0 and m == 0:
          break

     # 사탕 정보 입력 받기 (칼로리와 가격)
     candies = []
     for _ in range(int(n)):
          c, p = map(float, input().split())
          calories = int(c)
          price = int(p * 100 + 0.5)  # 소수점을 정수로 변환
          candies.append((calories, price))

     # DP 테이블 초기화
     dp = [0] * (m+1)

     # DP를 이용한 최대 칼로리 계산
     for calories, price in candies:
          for j in range(price, m+1):
               dp[j] = max(dp[j], dp[j-price] + calories)

     # 결과 출력
     print(dp[m])
