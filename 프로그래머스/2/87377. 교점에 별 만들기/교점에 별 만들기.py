def solution(line):
    answer = []
    n = len(line)
    pos = list()
    
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    
    # 1. 직선의 교점 구하기
    for i in range(n):
        a,b,e = line[i]
        for j in range(i+1, n):
            c,d,f = line[j]
            if a*d == b*c: continue
            x = (b*f-e*d) / (a*d-b*c)
            y = (e*c-a*f) / (a*d-b*c)
            
            # 2. 정수 교점만 변수로 저장하기
            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x,y])
                # 3. 최대/최소 사각형 구하기
                if x_min > x: x_min = x
                if y_min > y: y_min = y
                if x_max < x: x_max = x
                if y_max < y: y_max = y

    # 4. 2차원 배열에 *찍기
    x_len = x_max - x_min + 1
    y_len = y_max - y_min + 1
    coord = [['.'] * x_len for _ in range(y_len)]
    
    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        coord[ny][nx] = '*'
    
    # 5. 배열 역순으로 출력하기
    for result in coord: answer.append(''.join(result))
            
    return answer[::-1]