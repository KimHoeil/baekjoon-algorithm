# Z 실버 1 재귀

import sys
import copy

n,targetR,targetC = map(int, sys.stdin.readline().split())
ans = 0
# arr = [[0 for j in range(2**n)] for i in range(2**n)]
cnt =0

def dfs(N:int, r:int, c:int):
    global cnt
    global ans
    length = 2**N

    # Z형태로 방문하는 재귀식
    # cnt를 매개변수로 입력해서 방문 횟수를 카운트할 수 있다.
    if N == 1:
        # print("r=",r, "c=",c)
        for i in range(r, r+2):
            for j in range(c, c+2):
                # arr[i][j] = cnt
                cnt +=1
                if targetR==i and targetC==j:
                    return
                # for k in arr:
                #     print(k)
                # print()
        return
    
    # 1사분면
    if targetR-r < length/2 and targetC-c < length/2:
        dfs(N-1, r,c)
        return
    else:
        cnt += (2**(N-1)) * (2**(N-1))
        # print("1", cnt)

    # 2사분면
    if targetR-r < length/2 and targetC-c >= length/2:
        dfs(N-1, r, int((2*c + (2**(N)))/2))
        return
    else:
        cnt += (2**(N-1)) * (2**(N-1))
        # print("2", cnt)

    # 3사분면
    if length/2 <= targetR-r and targetC-c < length/2:
        dfs(N-1, int((2*r + (2**(N)))/2), c)
        return
    else:
        cnt += (2**(N-1)) * (2**(N-1))
        # print("3", cnt)

    # 4사분면
    if length/2 <= targetR-r and length/2 <= targetC-c:
        dfs(N-1, int((2*r + (2**(N)))/2), int((2*c + (2**(N)))/2))
        return
    else:
        cnt += (2**(N-1)) * (2**(N-1))
        # print("4", cnt)
        
dfs(n,0,0)
print(cnt-1)
# print(arr[r][c])       

# for i in arr:
#     print(i)

