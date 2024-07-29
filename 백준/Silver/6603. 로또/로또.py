# 로또 실버2 순열

import sys
import copy
resultArr = [0] * 6
visited = [False] * 6

def dfs(start:int, k:int, depth:int, testCase):
    global resultArr

    if depth==6:
        for i in resultArr:
            if i !=0:
                print(i, end=' ')
        print()
        return
    
    for i in range(start,k):
        resultArr[depth] = testCase[i]
        dfs(i+1, k, depth+1, testCase)

    

while True:
    testCase = list(map(int, sys.stdin.readline().split()))

    if testCase[0]==0:
        break
    else:
        k = testCase.pop(0)

    dfs(0,k,0,testCase)
    print()

    

