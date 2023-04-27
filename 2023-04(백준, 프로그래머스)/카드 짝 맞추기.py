from heapq import *
from itertools import permutations

def solution(board, r, c):
    def find(board,x,y,f):
        h = [[0,x,y,f"{x}-{y}"]]
        
        while h:
            cnt,x,y,visit = heappop(h)
            
            if board[x][y] == f:
                return [cnt,x,y]
            
            # 일단 상하좌우 갈수있다면 보낸다.
            for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
                if f"{i}-{j}" != visit and 0 <= i < 4 and 0 <= j < 4:
                    heappush(h,[cnt+1,i,j,visit])
            
            # 하 ctrl키로 움직임
            for i in range(x-1,-1,-1):
                if f"{i}-{y}" != visit and board[i][y] != 0:
                    heappush(h,[cnt+1,i,y,visit])
                    break
            else:
                if f"{0}-{y}" != visit:
                    heappush(h,[cnt+1,0,y,visit])
            
            # 상 컨트롤 키
            for i in range(x+1,4):
                if f"{i}-{y}" != visit and board[i][y] != 0:
                    heappush(h,[cnt+1,i,y,visit])
                    break
            else:
                if f"{3}-{y}" != visit:
                    heappush(h,[cnt+1,3,y,visit])

            # 좌측 컨트롤 키 
            for j in range(y-1,-1,-1):
                if f"{x}-{j}" != visit and board[x][j] != 0:
                    heappush(h,[cnt+1,x,j,visit])
                    break
            else:
                if f"{x}-{0}" != visit:
                    heappush(h,[cnt+1,x,0,visit])
            
            # 우측 컨트롤 키
            for j in range(y+1,4):
                if f"{x}-{j}" != visit and board[x][j] != 0:
                    heappush(h,[cnt+1,x,j,visit])
                    break
            else:
                if f"{x}-{3}" != visit:
                    heappush(h,[cnt+1,x,3,visit])

    # 총 몇개의 그림판이 남았나 체크        
    check = set()
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                check.add(board[i][j])

    # 각 찾을수 있는 경우의수대로 다 찾아보고 제일 작은값 출력       
    result = float('inf')
    origin_r,origin_c = r,c
    for turn in permutations(list(check),len(check)):
        check = 0
        new_board = [[board[i][j] for j in range(4)] for i in range(4)]
        for t in turn:
            cnt,x,y = find(new_board,r,c,t)  # 현재위치에서 찾아야할 위치까지의 정보
            new_board[x][y] = 10
            cnt1,x1,y1 = find(new_board,x,y,t) # 두 카드의 거리정보
            check += cnt+cnt1+2 
            new_board[x][y] = 0
            new_board[x1][y1] = 0
            r,c = x1,y1
        result = min(result,check)
        r,c = origin_r,origin_c
    return result


# 테스트케이스 하나가 삑나는데 도저히 못찾겠다... 사람들 마다 풀이도 달라서 어떻게 찾아야할지....
# 중복되는걸 해결하라는데 중복이 있을수있나??? 이해가 가지 않는다.
# 요즘 왜케 알고리즘이 깔끔하게 안풀리는지 스트레스 개받네 시발ㅇ나러낭러님라ㅣ
# 나는 멍청한가봐............