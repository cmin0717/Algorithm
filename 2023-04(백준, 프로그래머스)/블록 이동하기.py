from heapq import *

def solution(board):
    
    h,n = [],len(board)
    done = set('0.0.0.1')
    heappush(h,[0,0,0,0,1,0])
    
    while h:
        
        cnt,x1,y1,x2,y2,stay = heappop(h)
        
        if x2 == n-1 and y2 == n-1:
            return cnt
        
        r_c = {0:[[x2,y2,x2,y2+1],[x1,y1-1,x1,y1],[x1+1,y1,x2+1,y2],[x1-1,y1,x2-1,y2]],
               1:[[x1,y1+1,x2,y2+1],[x1,y1-1,x2,y2-1],[x2,y2,x2+1,y2],[x1-1,y1,x1,y1]]}
        
        for a1,b1,a2,b2 in r_c[stay]:
            check = f"{a1}.{b1}.{a2}.{b2}"
            if check not in done and 0 <= a1 < n and 0 <= b1 < n and 0 <= a2 < n and 0 <= b2 < n:
                if board[a1][b1] != 1 and board[a2][b2] != 1:
                    done.add(check)
                    heappush(h,[cnt+1,a1,b1,a2,b2,stay])
        
        cro = {0:[[x1-1,y1,x1,y1,x2+1,y2],[x2-1,y2,x2,y2,x1-1,y1],[x1,y1,x1+1,y1,x2+1,y2],[x2,y2,x2+1,y2,x1+1,y1]],
               1:[[x1,y1-1,x1,y1,x2,y2-1],[x1,y1,x1,y1+1,x2,y2+1],[x2,y2-1,x2,y2,x1,y1-1],[x2,y2,x2,y2+1,x1,y1+1]]}
        
        for a1,b1,a2,b2,c1,c2 in cro[stay]:
            check = f"{a1}.{b1}.{a2}.{b2}"
            if check not in done and 0 <= a1 < n and 0 <= b1 < n and 0 <= a2 < n and 0 <= b2 < n and 0 <= c1 < n and 0 <= c2 < n:
                if board[a1][b1] != 1 and board[a2][b2] != 1 and board[c1][c2] != 1:
                    done.add(check)
                    heappush(h,[cnt+1,a1,b1,a2,b2,abs(stay-1)])


# 도대체 시팔 뭐가 틀린지 모르겠다.... 테케 하나 틀렸는데 뭔지 감도 안온다 시발 화나서 말도 안나오네....
# 몰라 시벌,....