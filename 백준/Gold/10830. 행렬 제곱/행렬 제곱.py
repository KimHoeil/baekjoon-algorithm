# https://www.acmicpc.net/problem/10830

import sys
import copy
input = sys.stdin.readline

n,b = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def matrix_pow(b):
    if b == 1:
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
        return matrix
    else:
        result = matrix_pow(b//2) 

        ans = [[0 for j in range(n)] for i in range(n)]

        if b % 2 == 0:
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        ans[i][j] +=(result[i][k] * result[k][j])%1000
                        ans[i][j] = ans[i][j] % 1000
            return ans
        
        else:
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        ans[i][j] +=(result[i][k] * result[k][j])%1000
                        ans[i][j] = ans[i][j] % 1000

            ans2 = [[0 for j in range(n)] for i in range(n)]

            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        ans2[i][j] +=(ans[i][k] * matrix[k][j])%1000
                        ans2[i][j] = ans2[i][j] % 1000

            return ans2

ans_matrix = matrix_pow(b)
for row in ans_matrix:
    print(*row)