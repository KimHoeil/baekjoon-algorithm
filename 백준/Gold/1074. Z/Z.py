# https://www.acmicpc.net/problem/1074

import sys
input = sys.stdin.readline

def Z(r,c,n):
    if n==0: return 0

    half = n//2

    if r<half and c<half:
        return Z(r,c,half)
    if r<half and c>=half:
        return half * half + Z(r, c-half, half)
    if r>=half and c<half:
        return 2*half*half + Z(r-half, c, half)
    return 3*half*half + Z(r-half, c-half, half)

n,r,c = map(int, input().split())
print(Z(r,c,2**n))
