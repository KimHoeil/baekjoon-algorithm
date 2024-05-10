# 16165번

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
groupDict = {}
memberDict = {}

# n개의 걸그룹 입력받기
for _ in range(n):
    group = input().rstrip()
    groupCnt = int(input())

    memberList = []
    for _ in range(groupCnt):
        member = input().rstrip()   # 공백제거
        memberList.append(member)  # 멤버 리스트 추가
        memberList.sort()           # 멤버 이름 오름차순 정렬
        groupDict[group] = memberList # 그룹 딕셔너리 추가
        memberDict[member] = group # 멤버 딕셔너리 추가

# m개의 퀴즈 입력받기
for _ in range(m):
    quiz = input().rstrip()
    type = int(input())

    if type == 1: # 멤버이름으로 그룹 출력하기
        print(memberDict[quiz])
    
    else: # 그룹 이름으로 멤버 출력하기
        for member in groupDict[quiz]:
            print(member)
