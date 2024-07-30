# https://www.acmicpc.net/problem/10974

import sys
input = sys.stdin.readline

n = int(input())    
arr = [i for i in range(1, n+1)]    
result = [0] * n
visited = [False] * (n+1)

def dfs(depth):
    if depth == n:
        print(*result)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result[depth] = arr[i-1]
            dfs(depth+1)
            visited[i] = False
dfs(0)