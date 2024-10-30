import sys

input = sys.stdin.readline

x = int(input())

stick = [64]

def stick_check():
    stick_sum = sum(stick)
    if stick_sum > x:
        half = stick[-1] // 2
        del stick[-1]
        stick.append(half)
        stick_sum = sum(stick)
        if stick_sum == x:
            print(len(stick))
            return
        if stick_sum < x:
            stick.append(half)
        stick_check()
    else:
        print(1)

stick_check()
        
            