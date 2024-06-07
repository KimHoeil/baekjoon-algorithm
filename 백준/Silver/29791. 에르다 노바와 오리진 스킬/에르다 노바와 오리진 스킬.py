# https://www.acmicpc.net/problem/29791

import sys
from collections import deque
input = sys.stdin.readline

nova, origin = map(int, input().split())


novaList = list(map(int, input().split()))
originList = list(map(int, input().split()))

novaList.sort()
originList.sort()

novaq= deque(novaList)
originq = deque(originList)

ccCount = 0
accCount = 0
novaCooltime = 0
originCooltime = 0

while True:
    if novaq:
        nova = novaq.popleft()
    if originq:
        origin = originq.popleft()
    

    # print("nova:", nova)
    # print("origin: ", origin)

    if nova >= novaCooltime:
        ccCount +=1
        novaCooltime = 100+nova

    
    if origin >= originCooltime:
        accCount +=1
        originCooltime = 360+origin

    

    if len(novaq) == 0 and len(originq) == 0:
        break

print(ccCount, accCount)
    
    
