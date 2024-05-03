# 1026번
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
q = deque(a)
ans = 0
for bi in b:
     ai = q.popleft()
     
     mult = ai * bi
     ans += mult
print(ans)
          
