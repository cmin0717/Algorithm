def solution(line):
    
    cross_dot = set()
    min_x, min_y = float('inf'), float('inf')
    max_x, max_y = -float('inf'), -float('inf')
    
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            
            # 두 선이 평행이라면 패쓰
            n = (a*d) - (b*c)
            if n == 0:
                continue
            
            # 교점이 정수가 아니라면 패쓰
            new_y = (b*f - e*d) / n
            new_x = (e*c - a*f) / n
            if new_x % 1 != 0 or new_y % 1 != 0:
                continue

            # 교점을 저장하고 교점들의 최대, 최소 x,y값을 저장
            new_x, new_y = int(new_x), int(new_y)
            min_x = min(min_x, new_x)
            max_x = max(max_x, new_x)
            min_y = min(min_y, new_y)
            max_y = max(max_y, new_y)
            cross_dot.add((new_x, new_y))
    
    # 해당 교점들의 최소 크기의 판 생성
    board = [['.'] * (abs(max_y - min_y)+1) for _ in range(abs(max_x - min_x)+1)]
    
    # 좌표를 수정해주고 교점에 해당하는 좌표에 *삽입
    add_x, add_y = -min_x, -min_y
    for x,y in cross_dot:
        x += add_x
        y += add_y
        board[x][y] = '*'
    board = board
    return [''.join(i) for i in board][::-1]
            