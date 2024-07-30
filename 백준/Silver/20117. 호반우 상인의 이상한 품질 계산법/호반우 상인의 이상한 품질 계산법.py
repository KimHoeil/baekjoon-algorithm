# https://www.acmicpc.net/problem/20117

import sys
input = sys.stdin.readline

n = int(input())
merchandise = list(map(int, input().split()))

start = 0
end = n-1

merchandise.sort()
price = 0
if n % 2 == 0:
    while start < end:
        price += merchandise[end] * 2
        start += 1
        end -= 1
else:
    while start <= end:
        if start == end:
            price += merchandise[start]
            break
        price += merchandise[end] * 2
        start += 1
        end -= 1
        
print(price)
