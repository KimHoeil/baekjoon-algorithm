# https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lanList = []
for _ in range(k):
    lanList.append(int(input()))

start = 1
end = max(lanList)
mid = 0

def check(mid):
    cnt = 0
    for lan in lanList:
        cnt += lan // mid
    return cnt >= n


while start <= end:
    mid = (start+end) // 2

    # n보다 크거나 같으면
    if check(mid):
        ans = mid
        start = mid + 1
    # n보다 작으면 
    else:
        end = mid-1

print(ans)