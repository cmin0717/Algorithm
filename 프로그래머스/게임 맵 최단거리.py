from heapq import *

def solution(maps):
    n,m = len(maps), len(maps[0])
    # 애당초 도착지가 벽으로 막혀있을 경우 바로 -1 리턴
    if maps[n-1][m-1] == 0 and maps[n-2][m-1] == 0:
        return -1
    
    h = [[1,0,0]]
    maps[0][0] = 0
    
    while h:
        cnt,x,y = heappop(h)
        
        if x == n-1 and y == m-1:
            return cnt
        
        for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
            if 0 <= i < n and 0 <= j < m and maps[i][j] == 1:
                maps[i][j] = 0
                heappush(h,[cnt+1,i,j])
    else:
        return -1 

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))