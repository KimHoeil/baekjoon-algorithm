# https://www.acmicpc.net/problem/2422

import sys
input = sys.stdin.readline


n,m = map(int, input().split())
prohibit = [[True for j in range(201)] for i in range(201)]

for _ in range(m):
    n1,n2 = map(int, input().split())
    prohibit[n1][n2] = prohibit[n2][n1] = False

count = 0
for i in range(1,n+1):
    for j in range(i,n+1):
        for k in range(j, n+1):
            if i!=j and j!=k and k != i:
                if prohibit[i][j]and prohibit[j][k] and prohibit[k][i]:
                    # print(i,j,k)
                    count +=1
print(count)