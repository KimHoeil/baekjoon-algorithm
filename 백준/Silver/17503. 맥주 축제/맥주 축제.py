# 17503번

############################
# 그리디 풀이법
# 1. 도수레벨이 낮은 순으로 정렬 (우선순위1)
# 2. 선호도가 높은 순으로 정렬 (우선순위2)
# 3. 정렬된 맥주를 n개만큼 최소힙에 삽입
# 4. 선호도의 합이 m이상인지 확인
# 5. 선호도의 합이 m미만이면 pop하고 다음 맥주를 삽입하고 확인
# 6. 선호도의 합이 m이상이 될때까지 반복

from collections import deque
import sys, heapq
input = sys.stdin.readline

n,m,k = map(int, input().split())

beerList = []
for _ in range(k):
    v,d = map(int, input().split()) # 선호도, 도수레벨
    beerList.append((v,d)) 

beerList.sort(key=lambda x:(x[1], -x[0])) # 도수 오름차순, 선호도 내림차순 정렬
beerq = deque(beerList)

minq = []
prefSum  = 0

while beerq:
    pref, dosu = beerq.popleft()
    prefSum += pref
    heapq.heappush(minq, (pref,dosu))

    if len(minq) == n:
        if prefSum >= m:
            print(dosu)
            exit()
        else:
            prevBeer = heapq.heappop(minq)
            prefSum -= prevBeer[0]

print(-1)

