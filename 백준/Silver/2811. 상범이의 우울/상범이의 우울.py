# 2811번

import sys
input = sys.stdin.readline

n = int(input())
inputList = list(map(int, input().split()))
inputList.append(0)


i = 0
maxIdx = 0
maxPeriod = 0
while i < n:
    if inputList[i]  < 0:
        index = i
        period = 1
        for j in range(i+1, n):
            if inputList[j] < 0:
                period +=1
                i = j
            else:
                break
        
        # 기간이 가장 긴 경우
        if maxPeriod < period:
            maxIdx = index
            maxPeriod = period

        # 기간이 같으면 인덱스가 더 큰 경우로 갱신
        elif maxPeriod == period:
            if maxIdx < index:
                maxIdx = index
    
    i+=1

# print(maxPeriod, maxIdx)

t = 0 # 우울기간
ans = 0
count = 0
flowerCheck = [False] * n
for i in range(n):
    if inputList[i] < 0:
        t +=1
        index = i-t+1 # 우울한 기간 첫날
        if inputList[i+1] >=0:
            # 2t만큼 줄수있는 경우
            if index - (2*t) >= 0:
                for j in range(index - (2*t), index):
                    if flowerCheck[j] == False:
                        flowerCheck[j] = True
                        count +=1
                # print(ans, "here")

            # 2t만큼 줄수없는 경우
            elif index - (2*t) < 0:
                for j in range(index):
                    if flowerCheck[j] == False:
                        flowerCheck[j] = True
                        count +=1
                # print(ans)
            t = 0
ans = count
# print(count)

count = 0
maxCount = 0
# 가장 긴 우울 기간인 경우 최대값 찾기
for i in range(n):
    # 최장 우울 기간인 경우만 추가로 확인
    if inputList[i] < 0:
        t +=1
        # print("why?", t, i)
        index = i-t+1 # 우울한 기간 첫날
        if inputList[i+1] >=0:
            if t == maxPeriod:  
                # print("?")
                # 3t만큼 줄수있는 경우
                # print("index;:", index, i)
                if index - (3*maxPeriod) >=0:
                    for j in range(index - (3*maxPeriod), index):
                            if flowerCheck[j] == False:
                                count +=1
                    # print(ans, " amx")

                # 3t만큼 줄수없는 경우
                else:
                    # print("no")
                    for j in range(index):
                            if flowerCheck[j] == False:
                                count +=1

                maxCount = max(count, maxCount)
                count = 0
            t = 0

# print(flowerCheck)

# print(maxCount)
ans += maxCount

print(ans)