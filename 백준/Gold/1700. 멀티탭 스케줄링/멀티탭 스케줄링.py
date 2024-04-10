# 멀티탭스케줄링

import sys
from collections import deque
import heapq

input = sys.stdin.readline

n,k = map(int, input().split())

sequence = list(map(int, input().split()))
# print(sequence)

sequenceq = deque()

# 사용 순서를 나타내는 큐에 인덱스 번호와 함께 저장 (인덱스번호, 물건번호)
# 인덱스번호가 사용 순서의 그리디적 속성을 부여함.
for i in range(len(sequence)):
     sequenceq.append((i+1, sequence[i]))
# print(sequenceq)

plug = [] # 플러그 선언
# print(plug)

maxq = [] # 플러그를 뽑을때 우선순위로 뽑을 물건을 저장함.
# for i in sequenceq:
#      print(i)

def findIndexInsertion(curItem):
     for idx, item in sequenceq:
          if item == curItem:
               heapq.heappush(maxq, (-idx, item)) # 맥스힙으로 사용하기위해 (-인덱스, 번호) 로 삽입
               return
          
     # 사용 목록에 없는 아이템은 뽑힐 우선순위 0순위다.
     heapq.heappush(maxq, (-1e10, curItem))
     

cnt = 0
# 물건 플러그에 뽑기 시뮬레이션 돌리기
while sequenceq:
     curIndex, curItem = sequenceq.popleft()
     
     # 플러그에 자리가있으면 꽂기
     if len(plug) < n:
          if curItem not in plug: # 물건이 플러그에 꽂혀있지 않다면 꽂기
               plug.append(curItem)
               # 다음에 나올 물건의 인덱스 번호 찾기
               findIndexInsertion(curItem)

          else: # 물건이 플러그에 꽂혀있다면
               findIndexInsertion(curItem)

          
     # 플러그에 자리가 없으면 우선순위 높은 물건 뽑기
     else:

          # 꽂아야할게 플러그에 꽂혀있다면 맥스힙만 업데이트
          if curItem in plug:
               maxq.remove((-curIndex, curItem))
               findIndexInsertion(curItem)

          else: # 우선순위가 높은(사용할 일이 제일 늦은) 물건 플러그 뽑아버리기
               
               # 플러그에 꽂혀있는데 맥스힙에 없는경우가 0순위
               candidateIdx, candidateItem = heapq.heappop(maxq)
               plug.remove(candidateItem)
               plug.append(curItem)
               cnt +=1

               # 다음에 나올 물건의 인덱스 번호 찾기
               findIndexInsertion(curItem)

print(cnt)
          
               
          
          



     

