# https://www.acmicpc.net/problem/28250

# https://www.acmicpc.net/problem/28250

import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())

A = list(map(int, input().split()))
counter = Counter(A)

sum_mex = 0
sum_mex += counter[0] * (n-counter[0]-counter[1])   # 조합 (0, 1이상인경우) = mex값은 1
sum_mex += counter[0] * counter[1] *2               # 조합 (0,1) 인 경우 = mex값은2이므로 2를 곱해준다.
sum_mex += counter[0] * (counter[0]-1) // 2         # 조합 (0,0) 인 경우 = mex값은 1
print(sum_mex)

