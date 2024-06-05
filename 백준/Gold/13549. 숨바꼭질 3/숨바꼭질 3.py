# https://www.acmicpc.net/problem/13549


from collections import deque
import sys
input = sys.stdin.readline


subin, bro = map(int, input().split())


visited = [False] * 100001
def bfs(x):
    depth = [0] * 100001

    q = deque([])
    q.append(x)
    visited[x] = True

    while q:
        cur = q.popleft()
        move = []
        move.append(cur-1)
        move.append(cur+1)
        jump = 2*cur

        if cur == bro or jump == bro:
            print(depth[cur])
            return

        
        if 0 <= jump <= 100000:
            if visited[jump] == False:
                visited[jump] = True
                q.append(jump)
                depth[jump] = depth[cur]

        for i in move:
            if 0 <= i <= 100000:
                if visited[i] == False:
                    visited[i] = True
                    q.append(i)
                    depth[i] = depth[cur] + 1


bfs(subin)