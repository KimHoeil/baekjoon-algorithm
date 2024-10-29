import sys

input = sys.stdin.readline
m,n = map(int, input().split())
board = [input() for _ in range(m)]

def count_paint(x,y, start_color):
    count = 0
    for i in range(8):
        for j in range(8):
            expectedc_color = 'W' if (i+j) %2 ==0 else 'B'
            if start_color == 'B':
                expectedc_color = 'B' if (i+j)%2 ==0 else 'W'
            if board[x+i][y+j] != expectedc_color:
                count +=1
    return count

min_paint = float('inf')
for i in range(m-7):
    for j in range(n-7):
        paint_count_white_start = count_paint(i,j,'W')
        paint_count_black_start = count_paint(i,j,'B')  
        min_paint = min(min_paint, paint_count_white_start, paint_count_black_start)

print(min_paint)