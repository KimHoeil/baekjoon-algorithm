# 트리 순회하기

"""
               방문 순서
전위 순회 (루트)(왼쪽자식)(오른쪽자식)
중위 순회 (왼쪽자식)(루트)(오른쪽자식)
후위 순회 (왼쪽자식)(오른쪽자식)(루트)
"""

import sys

# 1. 인접행렬 구현방식
# 2. 인접리스트 구현방식
# 트리형태 구현 방식... -> 딕셔너리로 노드 클래스 값으로 저장하기

# sys.stdin = open('input.txt','r')
n = int(sys.stdin.readline())

class Node():
     def __init__(self, value, left, right) -> None:
          self.value = value
          self.left  = left
          self.right = right

# 한 줄당 한 노드를 받으면 이진트리 형태
tree = {}
nodes =[]
for i in range(n):
     nodes.append(sys.stdin.readline().split())


def preorder(node):
     """전위 순회 (루트)(왼쪽자식)(오른쪽자식)"""
     print(node.value, end='') # 자기 자신 먼저 출력
     if node.left != '.':      # 왼쪽 자식이 있다면 재귀 호출로 순회
          preorder(tree[node.left])
     if node.right != '.':
          preorder(tree[node.right]) # 오른쪽 자식이 있다면 순회
     

def inorder(node):
     """중위 순회 (왼쪽자식)(루트)(오른쪽자식)"""
     if node.left != '.':
          inorder(tree[node.left])
     print(node.value, end='')
     if node.right != '.':
          inorder(tree[node.right])
     
def postorder(node):
     """후위 순회 (왼쪽자식)(오른쪽자식)(루트)"""
     if node.left != '.':
          postorder(tree[node.left])
     if node.right != '.':
          postorder(tree[node.right])
     print(node.value, end='')

for value,left,right in nodes:
     # 트리의 키값에 노드 정보를 저장
     tree[value] = Node(value,left,right) 

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])