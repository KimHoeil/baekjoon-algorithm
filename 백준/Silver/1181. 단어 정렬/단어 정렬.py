# 단어 정렬

import sys

# sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline())
arr = []
s1 = set() # 집합 사용으로 중복제거

for i in range(n):
     s1.add(sys.stdin.readline().rstrip())

arr = list(s1) 
# 먼저 사전순으로 정렬
arr.sort()

# 다음 길이순으로 정렬
arr.sort(key=len)

for i in arr:
     print(i)
