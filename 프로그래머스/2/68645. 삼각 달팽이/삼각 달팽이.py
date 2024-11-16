def snail(x,y,board,n):
    dx = [1,0,-1] # 하,우,좌상
    dy = [0,1,-1]
    direction_index = 0
    flag = False
    board[x][y] = 1
    
    while True:
        nx = x + dx[direction_index]
        ny = y + dy[direction_index]
        
        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
            board[nx][ny] = board[x][y] +1
            flag = False
            x = nx
            y = ny
        else:
            if flag == True: break
            if direction_index == 2: direction_index =0
            else: direction_index +=1 
            flag = True
        
def solution(n):
    answer = []
    
    board = [[0 for j in range(n)] for i in range(n)]
    snail(0,0,board,n)
    
    for rows in board:
        for num in rows:
            if num != 0:
                answer.append(num)
    return answer