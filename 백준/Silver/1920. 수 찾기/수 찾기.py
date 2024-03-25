# 수찾기 실버 4

import sys
import copy

n = int(sys.stdin.readline())
arr  =[]
arr = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
arrB = list(map(int, sys.stdin.readline().split()))

arr.sort()
ans = []
while len(arrB)!=0:
    num = arrB.pop(0)

    start = 0
    end = n
    
    # print(num, start, end)
    while start <= end:
        mid = int((start+end)/2)
        if mid >= n:
            # print(0)
            ans.append(0)
            break
        else:
            if num > arr[mid]:
                start = mid+1
            elif num < arr[mid]:
                end = mid-1
            elif num == arr[mid]:
                # print(1)
                ans.append(1)
                break
        
            if end < start:
                # print(0)
                ans.append(0)
                break
        
for i in ans:
    print(i)
# print(ans)
    