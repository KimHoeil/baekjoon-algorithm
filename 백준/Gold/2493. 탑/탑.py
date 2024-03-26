# 탑

import sys
from collections import deque

# sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline())

arr = []
arr = list(map(int, sys.stdin.readline().split()))

topArr = []
# 탑높이랑 인덱스 번호 pair로 저장하기 (탑높이, 인덱스번호)
for i in range(len(arr)):
     topArr.append((arr[i],i+1))

# print(*topArr)
     
# 스택에 저장하면서 수신하는 탑 번호 pair로 저장하기
# 스택이 비어있지 않으면 
# 스택의 topPtr과 넣으려고하는 탑을 비교해서 스택topPtr의 높이가 더 작으면, 
# 스택 pop하고 다음 topPtr (탑높이, 인덱스) 저장
# 스택 pop하고 다음 topPtr이 없으면 (탑높이, 0) 저장
# 현재 넣으려고하는 탑 스택에 push
# 스택 topPtr의 높이가 더 크면 (탑높이, topPtr인덱스) 저장하고 push
topStk = deque()
ansArr = [] # (탑높이, 수신한탑번호)

topStk.append(topArr[0]) # 맨처음 탑 넣고 시작
ansArr.append(0)

# 모든 탑 순회하기
     # peek = [-1] 로 구현가능
for i in range(1, n):
     
     # 작은탑이 다 없어질때까지
     while True: # 넣으려는 탑 높이가 더 큰 경우 스택 탑 pop
          # 넣으려는 탑이 스택탑보다 큰경우
          if topArr[i][0] >= topStk[-1][0]: 
               # print(topArr[i][0],  topStk[-1][0])
               # print('pop전', topStk)
               topStk.pop() # 스택에서 pop
               # print('pop하고 다음 stkTop: ',topStk)

               # topStk.append(topArr[i]) # 스택에 탑 push
               if len(topStk) ==0: # push했는데 길이가 1이면 탈출
                    ansArr.append(0)
                    topStk.append(topArr[i]) # 스택에 탑 push
                    break

          else: # 작은경우
               ansArr.append(topStk[-1][1])
               topStk.append(topArr[i]) # 스택에 탑 push
               break

     # print()
print(*ansArr)

                    
 