def solution(grid):
    n,m = len(grid), len(grid[0])
    # 방향성 상,우,하,좌
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    # 각 격자별로 4방향성을 가진 배열을 만들어준다.
    visit = [[[False]*4 for _ in range(m)] for _ in range(n)]

    result = []
    for i in range(n):
        for j in range(m):
            for z in range(4):
                # 이미 갔다온 사이클이라면 패쓰
                if visit[i][j][z]:
                    continue                

                cnt = 0
                x,y = i,j
                # 한번이라도 갔던곳이 나올때까지 반복
                while not visit[x][y][z]:
                    visit[x][y][z] = True
                    cnt += 1
                    
                    if grid[x][y] == 'L':
                        z = (z+1) % 4
                    elif grid[x][y] == 'R':
                        z = (z-1) % 4
                    
                    x = (x+dx[z]) % n
                    y = (y+dy[z]) % m
                    
                result.append(cnt)
                
    return sorted(result)