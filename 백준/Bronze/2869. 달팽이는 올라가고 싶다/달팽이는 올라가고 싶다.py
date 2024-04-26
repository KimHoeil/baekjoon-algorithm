# 2869번

import sys
import math

input = sys.stdin.readline

a,b,v = map(int, input().split())

goal = v-a
goUpDay = a-b

if goal == 0:
     print(1)
     exit()

semiGoal = math.ceil(goal / goUpDay)

if semiGoal == 0:
     print(1)

else:
     print(semiGoal+1)