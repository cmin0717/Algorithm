from heapq import *

def solution(board):
    # 출발지점에서는 아래랑 오른쪽만 갈수있다. 만일 가는곳이 벽이라면 출발점에 추가하지 않는다.
    h = [i for i in [[100,'d',1,0,['0:0','1:0']],[100,'r',0,1,['0:0','0:1']]] if board[i[2]][i[3]] == 0] 
    n = len(board)
    # heap으로 돌릴건데 만일 같은 위치 같은방향인데 cost가 더 높은상황에서는 더 볼필요가 없다.그걸 체크하기위한 작업업
    check = [[[float('inf') for _ in range(4)] for _ in range(n)] for _ in range(n)]
    dic = {'d':0,'u':1,'l':2,'r':3}
    
    while h:
        c,way,x,y,v = heappop(h)
        
        # 현재 같은 위치 같은 방향인곳에서 나보다 작은값이 왔다갔다면 나는 더 할 필요가 없다.
        if check[x][y][dic[way]] < c:
            continue
        else:
            check[x][y][dic[way]] = c
        
        # 도착지점에 왔다면 현재 cost를 리턴 / 항상 작은값으로 왔기에 첫 도착한 사람이 젤 작다.
        if x == n-1 and y == n-1:
            return c
        
        # 방문체크 및 여러 조건 판단후 heap에 넣어준다.
        for a,b,w in [x+1,y,'d'],[x-1,y,'u'],[x,y-1,'l'],[x,y+1,'r']:
            ab = f'{a}:{b}'
            if 0 <= a < n and 0 <= b < n and ab not in v and board[a][b] != 1:
                if w == way:
                    heappush(h,[c+100,w,a,b,v+[ab]])
                else:
                    heappush(h,[c+600,w,a,b,v+[ab]])

solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]])