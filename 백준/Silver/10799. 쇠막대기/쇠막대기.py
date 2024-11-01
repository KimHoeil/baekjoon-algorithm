import sys
input = sys.stdin.readline

def count_pieces(arrangement):
    stack = []
    count = 0   
    for i in range(len(arrangement)):
        if arrangement[i] =='(':
            stack.append('(')
        else: # ')'
            stack.pop()
            if arrangement[i-1] == '(': # 레이져이면
                count += len(stack)
            else: # 쇠막대기의 끝이면
                count +=1
    return count

arrangement = input().strip()
print(count_pieces(arrangement))
