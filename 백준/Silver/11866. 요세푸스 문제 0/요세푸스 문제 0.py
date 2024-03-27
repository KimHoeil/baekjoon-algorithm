# 요세푸스 문제0

# 원순열 상황에서 k번째 사람을 제거함.
# 모든 사람이 제거되면 순서대로 출력하고 종료
# 링버퍼 활용 큐문제


import sys
from collections import deque
import copy

# sys.stdin = open('input.txt','r')
n,k = map(int, sys.stdin.readline().split())

deq = deque()
for i in range(n):
     deq.append(i+1)

ans = []
# 모든 사람이 제거될 때까지 반복
while deq:
     # k번째 원소를 뒤로 보냄
     for _ in range(k):
          deq.append(deq.popleft())
     
     # k번째 원소 제거
     ans.append(str(deq.pop()))
          

print('<'+ ', '.join(ans)+'>')



