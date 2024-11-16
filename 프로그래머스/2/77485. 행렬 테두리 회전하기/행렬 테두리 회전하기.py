# 3. 직사각형의 테두리를 시계 방향으로 회전시킨다. (역순으로 회전시킨다.)
def rotate(x1,y1,x2,y2,matrix):
    first = matrix[x1][y1]
    min_val = first

    # 왼쪽 
    for k in range(x1, x2):
        matrix[k][y1] = matrix[k+1][y1]
        min_val = min(min_val, matrix[k+1][y1])
    # 아래
    for k in range(y1,y2):
        matrix[x2][k] = matrix[x2][k+1]
        min_val = min(min_val, matrix[x2][k+1])
    # 오른쪽
    for k in range(x2, x1, -1):
        matrix[k][y2] = matrix[k-1][y2]
        min_val = min(min_val, matrix[k-1][y2])
    # 위
    for k in range(y2,y1,-1):
        matrix[x1][k] = matrix[x1][k-1]
        min_val = min(min_val, matrix[x1][k-1])

    matrix[x1][y1+1] = first

    return min_val

def solution(rows, columns, queries):
        
    answer = []
    # 1. 1씩 증가하는 행렬 생성
    matrix = [[(i)*columns + (j+1) for j in range(columns)] for i in range(rows)]
    
    # 2. 회전할 위치 목록을 받아온다.
    for x1,y1,x2,y2 in queries:
        answer.append(rotate(x1-1,y1-1,x2-1,y2-1, matrix))
    
    return answer