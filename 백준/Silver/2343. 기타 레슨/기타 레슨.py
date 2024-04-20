import sys

input = sys.stdin.readline

n, m = map(int, input().split())
courses = list(map(int, input().split()))

start, end = max(courses), sum(courses)

def is_possible(mid):
    count, total = 0, 0
    for course in courses:
        if total + course > mid:
            count += 1
            total = 0
        total += course
    return count < m

answer = end
while start <= end:
    # mid = 블루레이에 할당할 수 있는 최대 강의 시간
    mid = (start + end) // 2 
    if is_possible(mid): # mid값으로 모든 강의를 m개의 블루레이에 분배할 수 있는지 판단
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)
