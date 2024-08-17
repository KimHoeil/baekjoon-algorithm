# https://www.acmicpc.net/problem/17071

import sys
from collections import deque

visited = [[1e9] * 500001 for _ in range(2)] # [짝수, 홀수] 0,1일때 짝수인지 홀수인지 구분해서 방문처리

def bfs(start, time):
    q= deque([])
    q.append((start,time))
    visited[0][start] = 0

    while q:
        x,time = q.popleft()        
        for nx in [x-1, x+1, x*2]:
            if 0 <= nx < 500001: # 유효한 공간이면
                if visited[(time+1)%2][nx] > time+1: # 중복을 허용하지만 더 빠른 경우만 방문하도록
                    q.append((nx,time+1))
                    visited[(time+1)%2][nx] = time+1

input = sys.stdin.readline
subin, bro = map(int, input().split())

if subin == bro:
    print(0)
    exit()

bfs(subin,0)

def solution(bro):
    for i in range(1, 500001):
        bro = bro + i

        if bro > 500000:
            print(-1)
            return
        # 작거나 같은 이유는 수빈이 먼저 도착하면 동생이 올때까지 와리가리 타면서 기다렸다가 잡을수있기 때문
        if 0<= bro < 500001 and visited[i%2][bro] <= i:
            print(i)
            return
    print(-1)

solution(bro)


