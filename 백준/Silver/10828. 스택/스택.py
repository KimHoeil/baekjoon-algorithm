# 스택

"""
push
pop
size
empty
top

"""
import sys

n = int(sys.stdin.readline())

stk = [None]*n
ptr = 0

# n번의 명령 반복
for i in range(n):
     command = sys.stdin.readline().split()

     if command[0] == 'push':
          if len(stk)-1 == ptr: # 스택이 가득차면
               continue
          else:
               stk[ptr] = int(command[1])
               ptr +=1
          
     if command[0] == 'top':
          if ptr == 0: # 포인터가 바닥에 있으면
               print(-1)
          else:
               print(stk[ptr-1])

     if command[0] == 'size':
          print(ptr)
          
     if command[0] == 'empty':
          if ptr ==0: # 스택이 비어있으면
               print(1)
          else:
               print(0)

     if command[0] == 'pop':
          if ptr ==0: # 스택이 비어있으면
               print(-1)
          else:
               print(stk[ptr-1])
               ptr -=1
