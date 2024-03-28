import sys

# 바킹독 형님 답안
# def POW(a, b, m):
#     if b==1: return a % m
#     val = POW(a, int(b/2), m)
#     # 지수가 짝수승이면 바로 결과값 반환
#     if b%2 == 0: return val
#     # 지수가 홀수승이면 a를 한번더 곱해서 리턴
#     return val * a % m

input = sys.stdin.readline
a,b,c = map(int, input().split()) # 20억 이하의 자연수

# C의 n승 계산 O(logN) 의 시간복잡도를 가진다.
def fpow(a, n, c):
	if n == 1:
		return (a%c)
	else:
		x = fpow(a, n//2,c)
		if n % 2 == 0:
			return (x * x)%c
		else:
			return (x * x * a)%c

print(fpow(a,b,c))
