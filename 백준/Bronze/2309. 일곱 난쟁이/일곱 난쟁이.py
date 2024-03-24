# 일곱 난쟁이

import sys
import copy

arr = []
resultArr = [0] * 9
visited = [False] * 9
result = []

for i in range(9):
    inp = int(input())
    arr.append(inp)

def dfs(start:int, depth:int):
    global result

    if depth == 7:
        if sum(resultArr) == 100:
            result = copy.deepcopy(resultArr)
        return
    
    for i in range(start,9):
        resultArr[depth] = arr[i]
        dfs(i+1, depth+1)
        resultArr[depth] = 0
    
dfs(0,0)
result.sort()

for i in result:
    if i !=0:
        print(i)