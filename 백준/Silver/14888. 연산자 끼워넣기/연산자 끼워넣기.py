n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 최댓값과 최솟값을 초기화합니다.
max_value = -1e10
min_value = 1e10

# DFS 함수를 정의합니다.
def dfs(i, res):
    global max_value, min_value, add, sub, mul, div
    # 모든 수를 다 사용했다면, 최댓값과 최솟값을 갱신합니다.
    if i == n:
        max_value = max(max_value, res)
        min_value = min(min_value, res)
        return
    # 각 연산자에 대해 재귀적으로 DFS를 수행합니다.
    if add > 0:
        add -= 1
        dfs(i + 1, res + numbers[i])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(i + 1, res - numbers[i])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(i + 1, res * numbers[i])
        mul += 1
    if div > 0:
        div -= 1
        # 나눗셈은 음수일 때 C++14 표준을 따릅니다.
        if res < 0:
            dfs(i + 1, -(-res // numbers[i]))
        else:
            dfs(i + 1, res // numbers[i])
        div += 1

# DFS를 시작합니다.
dfs(1, numbers[0])

# 최댓값과 최솟값을 출력합니다.
print(max_value)
print(min_value)
