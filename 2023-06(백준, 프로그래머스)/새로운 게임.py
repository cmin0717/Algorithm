import sys
input = sys.stdin.readline

n,k = map(int, input().split())

# 땅의 정보
board = [list(map(int, input().split())) for _ in range(n)]

# 해당 땅에 무슨 말이 있는지에 대한 정보
horses = [[[] for _ in range(n)] for _ in range(n)]

# 각 말의 위치정보
position = [[] for _ in range(k)]

# 방향전환을 위해
dx, dy = [0,0,-1,1], [1,-1,0,0]

# 파란 땅을 만났을경우 방향전환을 위해
dic = {0:1, 1:0, 2:3, 3:2}

for i in range(k):
    x,y,d = map(int, input().split())
    position[i] = [x-1, y-1, d-1]
    horses[x-1][y-1] = [i]

# 각 턴 종료시 종료 조건을 만족하는지 체크
def done():
    for i in range(n):
        for j in range(n):
            if len(horses[i][j]) >= 4:
                return True
    return False

# 해당 말이 주체적으로 움직일수있는 조건인지 체크(한 곳에서 제일 밑에 위치한 말만 움직일수 있다.)
def can_move(idx):
    x,y,d = position[idx]
    return True if horses[x][y][0] == idx else False

# 하얀 땅과 붉은 땅일경우
def white_red(x,y,nx,ny):
    c = board[nx][ny]
    if c == 0:
        for horse in horses[x][y]:
            horses[nx][ny].append(horse)
            position[horse] = [nx, ny, position[horse][2]]
    elif c == 1:
        for horse in horses[x][y][::-1]:
            horses[nx][ny].append(horse)
            position[horse] = [nx, ny, position[horse][2]]
    horses[x][y] = []

# 각 말의 조건에 따라 말을 이동
def horse_move(idx):
    x,y,d = position[idx]
    nx, ny = x+dx[d], y+dy[d]

    # 움직인 말이 범위안에 있고 파란땅이 아닐경우
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
        white_red(x,y,nx,ny)
    
    # 움직인 말이 범위 밖에 있거나 파란땅일 경우
    elif nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 2:
        # 방향전환
        d = dic[d]
        position[idx][2] = d
        nx, ny = x+dx[d], y+dy[d]
        
        # 방향전환후 다시 조건 체크
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
            white_red(x,y,nx,ny)

        

turn = 0
while turn <= 1000:
    turn += 1

    # 각 말이 움직일수있다면 이동
    for i in range(k):
        if can_move(i):
            horse_move(i)

    # 조건을 만족하면 현재 턴을 출력 후 종료
    if (done()):
        print(turn)
        break
else:
    # 1000턴 동안 끝나지 않았다면 조건을 만족하지 못했기에 -1 출력
    print(-1)