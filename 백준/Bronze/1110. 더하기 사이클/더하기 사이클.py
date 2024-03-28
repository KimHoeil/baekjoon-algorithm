n = input()
if len(n) == 1:  # n이 한자릿수 라면 앞에 0을 붙인다
    n = '0' + n

cnt = 0 # 횟수를 세는 변수
num = n
while True:
    num = num[1] + str(int(num[0]) + int(num[1]))[-1]  # 새로운 수 제작
    cnt += 1  # 제작할 때마다 카운트 + 1

    if num == n:  # n과 같아지면 break
        break

print(cnt)