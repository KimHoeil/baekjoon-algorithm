# 큐2

import sys
from collections import deque

# sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())

que = deque()

for i in range(n):
     command = sys.stdin.readline().split()
     
     if command[0] == 'push':
          que.append(command[1])

     if command[0] == 'pop':
          if len(que)!=0:
               print(que.popleft())
          else:
               print(-1)
     
     if command[0] == 'size':
          print(len(que))

     if command[0] == 'empty':
          if len(que) ==0:
               print(1)
          else:
               print(0)

     if command[0] == 'front':
          if len(que) !=0:
               print(que[0])
          else:
               print(-1)

     if command[0] == 'back':
          if len(que) !=0:
               print(que[-1])
          else:
               print(-1)