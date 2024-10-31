import sys

input = sys.stdin.readline

def is_valid_tictactoe(board):
    # 보드를 2D 리스트로 변환
    board = [list(board[i:i+3]) for i in range(0,9,3)]
    
    # X,O,빈공간 개수 세기
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    space_count = sum(row.count('.') for row in board)
    
    # X와 O의 개수 차이가 0또는 1이 아니면 무효
    if x_count < o_count or x_count > o_count + 1:
        return False
        
    # 승리 조건 확인 함수
    def check_win(player):
        # 가로, 세로, 대각선 확인
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
                all(board[j][i] == player for j in range(3)):
                return True
        if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2-i] == player for i in range(3)):
            return True
        return False

    # X가 이겼는데 O의 개수가 X와 같으면 무효
    # O가 이겼는데 X의 개수가 O보다 많으면 무효
    if check_win('X') and x_count <= o_count:
        return False
    if check_win('O') and  x_count > o_count:
        return False

    # 빈칸이 있거나 승리하지 못한경우 무효
    # X와 O의 개수 차이가 없고 빈공간이 남아있으면 무효
    if space_count > 0 and check_win('X') == False and check_win('O') == False:
        return False


    return True

while True:
    board = input().strip()
    if board == 'end':
        break
    print("valid" if is_valid_tictactoe(board) else "invalid")
    