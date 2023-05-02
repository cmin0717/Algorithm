from collections import deque

def solution(rows, columns, queries):
    # 해당 row,col에 맞게 보드 생성
    board = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    result = []

    for x1,y1,x2,y2 in queries:
        
        # 주어진 x,y좌표를 통해 위쪽 면, 아래 면, 양쪽 면을 구함
        up = deque(board[x1-1][y1-1:y2-1])
        left = deque([board[i][y1-1] for i in range(x1,x2)])
        right = deque([board[i][y2-1] for i in range(x1-1,x2-1)])
        down = deque(board[x2-1][y1:y2])
        
        # 큐를 사용하여 시계방향으로 이동
        right.appendleft(up.pop())
        down.append(right.pop())
        left.append(down.popleft())
        up.appendleft(left.popleft())
        
        # 그중에 제일 작은값 result에 저장
        result.append(min(up+left+right+down))

        # 해당 값을 실제 보드에 적용
        board[x1-1][y1-1:y2] = up + deque([right[0]])
        board[x2-1][y1-1:y2] = deque([left[-1]]) + down
        for i in range(len(left)-1):
            board[x1+i][y1-1] = left[i]
        for i in range(1,len(right)):
            board[x1-1+i][y2-1] = right[i]
            
    return result