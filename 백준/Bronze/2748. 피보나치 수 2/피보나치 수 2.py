# 피보나치 수 by dp

import sys


n = int(sys.stdin.readline())
F = [0]*(n+1)

# top-down (재귀 방식)
def fibo(n):
     if n <= 1:
          F[n] = n
          return n
     
     if F[n] !=0: # 값이 쓰여있으면 재사용함
          return F[n]
     else:
          # 메모이제이션
          F[n] = fibo(n-1)+fibo(n-2)
          return F[n]

# bottom-up
# def fibo(n):
#      if n == 0:
#           return 0
#      elif n ==1:
#           return 1
     
#      F[1] = 1

#      for i in range(2, n+1):
#           F[i] = F[i-1] + F[i-2]
     

fibo(n)
print(F[n])