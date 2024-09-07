# https://www.acmicpc.net/problem/1110

import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
def add_cycle(num):
    global cnt 

    if num < 10:
        add_num = num
    else:
        left = str(num)[0]
        right = str(num)[1]
        add_num = int(left) + int(right)
    
    new_num = str(num)[-1] + str(add_num)[-1]

    if int(new_num) == int(n):
        return
    else:
        add_cycle(int(new_num))
        cnt = cnt+1

add_cycle(n)
print(cnt)
