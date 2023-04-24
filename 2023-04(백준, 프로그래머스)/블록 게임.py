def solution(board):
    max_block = max([max(i) for i in board])
    block = [[] for _ in range(max_block+1)] # 현재 블록들을 각 블록 구성끼리 저장
    fill = [[] for _ in range(max_block+1)] # 블록마다 채워야하는 칸을 저장
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:
                block[board[i][j]].append([i,j])
    
    for i in range(1,len(block)):
        check,standard = 0,0 
        block_x = [bx[0] for bx in block[i]] # 블록의 x좌표 모음
        
        # 블록의 x좌표에서 가장 많은 x좌표를 기준으로 저장
        for x in block_x:
            b_c = block_x.count(x)
            if b_c > check:
                standard,check = x,b_c
        
        # 만약 기준 x좌표보다 아래로 블록이 더 있다면 이 블록은 절대 채울수없다 위가 막혀있기에
        if standard+1 in block_x:
            continue
        
        # 기준 x좌표의 y값들을 모두 저장
        block_y = []
        for x,y in block[i]:
            if x == standard:
                block_y.append(y)

        # 구한 기준 x좌표의 y값들을 이용하여 채워야하는 좌표를 구해서 fill에 채운다.
        cnt = 1
        while True:
            fill_b = [[standard-cnt,y] for y in block_y]
            temp = False
            for f in fill_b:
                if f in block[i]:
                    temp = True
                    break
            if temp:
                for f in fill_b:
                    if f not in block[i]:
                        fill[i].append(f)
                cnt += 1
            else:
                break
    
    # 해당 좌표에 검은 블록을 놓을수 있는지 체크 함수
    def dot(idx):
        for x,y in fill[idx]:
            for i in range(x,-1,-1):
                if board[i][y] != 0:
                    return False
        return True
    
    # fill에서 채워야하는 좌표를 가져와서 더이상 채울수 없을때까지 체크
    result = 0
    visit = []
    while True:
        for i in range(1,len(fill)):
            if fill[i] and dot(i) and i not in visit:
                for x,y in block[i]:
                    board[x][y] = 0
                visit.append(i)
                result += 1
                break
        else:
            return result
    
solution([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0], [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5], [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]])