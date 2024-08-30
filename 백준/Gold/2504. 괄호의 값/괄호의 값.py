# https://www.acmicpc.net/problem/2504

import sys
from collections import deque

input = sys.stdin.readline

string = list(map(str, input().rstrip()))
stack = deque([])

def bracketCheck():

    for s in string:
        if s == '(' or  s == '[':
            stack.append(s)
        
        else:

            if s == ')':
                temp = 0
                flag = False
                while stack:
                    top = stack.pop()
                    
                    if top == '(':
                        stack.append(2 if temp == 0 else 2 * temp)
                        flag = True
                        break
                    elif top == '[':
                        print(0)
                        return
                    else: # 중첩된 값이 있는 경우 (숫자가 스택에 있는 경우)
                        temp += top
                if flag is False:
                    print(0)
                    return

            elif s == ']':
                temp = 0
                flag = False
                while stack:
                    top = stack.pop()

                    if top == '[':
                        stack.append(3 if temp == 0 else 3 * temp)
                        flag = True
                        break
                    elif top == '(':
                        print(0)
                        return
                    else: # 중첩된 값이 있는 경우 (숫자가 스택에 있는 경우)
                        temp += top

                if flag is False:
                    print(0)
                    return

    print(sum(stack) if all(isinstance(x, int) for x in stack) else 0) 
bracketCheck()
