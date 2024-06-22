# https://www.acmicpc.net/problem/9375


import sys
input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(input())

    clothesDick = {}
    clothes = []
    for i in range(n):
        clothes.append(list(map(str, input().split())))
        clothesDick[clothes[i][1]] = 1
        

    for cloth in clothes:
        kind = cloth[1]
        clothesDick[kind] +=1
    
    # print(clothesDick)
    # print()

    for cloth in clothes:
        kind = cloth[1]
        # print(clothesDick[kind])

    kindList =[]
    for i in list(clothesDick.keys()):
        kindList.append(i)

    resultList =[]
    for kind in kindList:
        # print(kind)
        resultList.append(clothesDick[kind])
    
    # print(resultList)

    ans = 1
    for result in resultList:
        ans *= result
    
    print(ans-1)