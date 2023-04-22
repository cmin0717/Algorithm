def solution(m, n, board):

    board = [list(i) for i in board]
    
    # 해당 위치에서 2*2상자가 만들어진다면 XY에 저장
    def check(i,j):
        puzz = board[i][j]
        
        if board[i+1][j] == puzz and board[i][j+1] == puzz and board[i+1][j+1] == puzz:
            xy.append([i,j])
            xy.append([i+1,j])
            xy.append([i,j+1])
            xy.append([i+1,j+1])
    
    result = 0
    while True:
        xy = []
        
        # board를 돌면서 변환가능한 상자를 찾는다.
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != '.':
                    check(i,j)
        
        # 없다면 종료
        if len(xy) == 0:
            return result
        
        # 있다면 해당위치들 변환
        for x,y in xy:
            if board[x][y] != '.':
                board[x][y] = '.'
                result += 1
        
        # 변환후 board 재정비
        for j in range(n):
            for i in range(m-1,-1,-1):
                if board[i][j] == '.':
                    for z in range(i-1,-1,-1):
                        if board[z][j] != '.':
                            board[i][j],board[z][j] = board[z][j],board[i][j]
                            break