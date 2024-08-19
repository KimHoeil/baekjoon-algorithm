# https://www.acmicpc.net/problem/25187

import sys
input = sys.stdin.readline


n,m,q = map(int, input().split())
waterType = list(map(int, input().split()))
waterSum = [0] * n
parent = [0] * n

for i in range(n):
    if waterType[i] == 0:
        waterSum[i] -= 1
    else:
        waterSum[i] += 1

# 루트를 찾는 함수. path compression 적용
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u,v):
    x = find(u)
    y = find(v)

    if x == y: return
    parent[y] = x

    waterSum[x] += waterSum[y]

def make_set(u):
    parent[u] = u

for i in range(n):
    make_set(i)

for _ in range(m):
    u,v = map(int, input().split())
    union(u-1, v-1)

for i in range(q):
    num = int(input())
    p = find(num-1)

    if waterSum[p] > 0:
        print(1)
    else:
        print(0)

