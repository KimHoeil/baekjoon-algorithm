# 부분 수열의 합_실버2_백트래킹

import sys
import copy

n, s = map(int, sys.stdin.readline().split())
arr = []
visited = [False] * n

num = list(map(int, sys.stdin.readline().split()))
arr = copy.deepcopy(num)
cnt = 0
arr.sort()
isFirst = False

def dfs(sum:int, depth:int)->int:

    global cnt
    global s
    global isFirst
    
    if sum == s and isFirst==True:
        cnt +=1
        
    if depth == n:
        return
    
    isFirst = True
    for i in range(depth,n):
        sum += arr[i]
        dfs(sum, i+1)
        sum -= arr[i]

dfs(0,0)
print(cnt)