# https://www.acmicpc.net/problem/1182

import sys
input = sys.stdin.readline

n,s = map(int, input().split())
sequence = list(map(int, input().split()))

sum = 0
cnt = 0
def dfs (depth, start):
    global sum 
    global cnt

    if depth == n:
        return
    
    for i in range(start, n):
        sum += sequence[i]
        if sum == s:
            cnt +=1
        dfs(depth+1, i+1)
        sum -= sequence[i]

dfs(0,0)
print(cnt)