# 이진 검색 트리

"""
트리를 전위 순회한 결과가 주어졌을때
후위 순회한 결과를 출력하라.

"""
import sys
sys.setrecursionlimit(10**9)

preResult = []
while True:
     try:
          preResult.append(int(sys.stdin.readline().rstrip()))
     except:
          break

def postorder(rootIdx, endIdx):
     if rootIdx > endIdx:
          return
     global preResult

     # root보다 큰 값 없는 경우 전부 왼쪽 서브트리로 취급
     rightStart = endIdx +1
     for i in range(rootIdx+1, endIdx +1):
          if preResult[rootIdx] < preResult[i]:
               rightStart = i
               break

     postorder(rootIdx+1, rightStart-1) # 왼쪽탐색
     postorder(rightStart, endIdx)      # 오른쪽 탐색
     print(preResult[rootIdx]) # root 출력

postorder(0, len(preResult)-1)



