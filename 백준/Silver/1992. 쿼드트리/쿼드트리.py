import sys
input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().rstrip())))

def quard_tree(row, col, row_end, col_end, n):
    if n == 1:  # 1x1 크기일 때
        return str(board[row][col])
    
    half = n // 2
    # 사분면 나누어 재귀적으로 호출하여 결과 문자열 반환
    top_left = quard_tree(row, col, row + half, col + half, half)
    top_right = quard_tree(row, col + half, row + half, col_end, half)
    bottom_left = quard_tree(row + half, col, row_end, col + half, half)
    bottom_right = quard_tree(row + half, col + half, row_end, col_end, half)
    
    # 사분면의 결과가 모두 같으면 하나로 압축, 다르면 괄호로 묶어서 결합
    if top_left == top_right == bottom_left == bottom_right and len(top_left) == 1:
        return top_left  # 모두 같다면 하나로 압축
    else:
        return f"({top_left}{top_right}{bottom_left}{bottom_right})"

# 결과 출력
print(quard_tree(0, 0, n, n, n))
