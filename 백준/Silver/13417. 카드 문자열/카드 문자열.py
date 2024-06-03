# 13417번

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    string = list(map(str, input().split()))
    # print(string)
    q = deque(string)
    
    result = deque([])
    while q:
        char = q.popleft()
        # print(char)
        if len(result) == 0:
            result.append(char)
        elif result[0] >= char:
            result.appendleft(char)
        else:
            result.append(char)

    ans = list(result)
    ans = "".join(ans)
    print(ans)

