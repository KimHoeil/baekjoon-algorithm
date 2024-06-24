# https://www.acmicpc.net/problem/15789


import sys  
input = sys.stdin.readline


# 루트 노드를 찾는 연산
def find(x):
    if parent[x] < 0 :
        return x
    
    parent[x] = find(parent[x])
    return parent[x]


n,m = map(int, input().split())

parent = [-1]* (n+1)
parent[0] = 0    

for _ in range(m):
    u,v = map(int, input().split())

    ru = find(u)
    rv = find(v)
    
    # print("ru",ru, "rv", rv)

    if ru == rv: continue

    if parent[ru] < parent[rv]:
        parent[ru] += parent[rv]
        parent[rv] = ru
    else:
        parent[rv] += parent[ru]
        parent[ru] = rv

    # print(parent)


c,h,k = map(int, input().split())

# print()
# print("p:", parent)
# print()

neutral = []
for i in range(1, n+1):
    if parent[i] < 0:
        if parent[h] != i and i != h:
            if parent[c] != i and i != c:
                neutral.append(parent[i])

neutral.sort()
# print(neutral)

ans = parent[c]
if ans > 0:
    ans = parent[ans]

# print(ans)
for i in range(k):
    ans += neutral[i]

print(abs(ans))



