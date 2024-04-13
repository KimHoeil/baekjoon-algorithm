# 겹치는건 싦어

import sys
input = sys.stdin.readline

n,k = map(int, input().split())

sequence = list(map(int, input().split()))
# print(sequence)

count = [0] * 1000000

end = 0
cnt = 0
maxCnt = 0

for start in range(n):
     while  end < n and count[sequence[end]] +1 <= k:
          cnt +=1
          count[sequence[end]] +=1
          end +=1
          maxCnt = max(maxCnt, cnt)

     count[sequence[start]] -=1 
     cnt -=1

print(maxCnt)
