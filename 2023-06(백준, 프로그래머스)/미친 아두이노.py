import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(input().rstrip()) for _ in range(n)]
# 움직일 방향별 추가값
dic = {'1': [1,-1], '2': [1,0], '3': [1,1], '4': [0,-1], 
       '5': [0,0], '6': [0,1], '7': [-1,-1], '8': [-1, 0], '9': [-1, 1]}

# 미친 아두이노들 좌표
aduinos = set()
# 종수 좌표
jongsu = []

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            aduinos.add((i,j))
        elif board[i][j] == 'I':
            jongsu = [i,j]

# 주어진 방향으로 종수 이동, 가는 방향에 아두이노 있으면 False리턴으로 겜 종료
def jongsu_move(move):
    global jongsu
    x,y = dic[move]
    x,y = jongsu[0]+x, jongsu[1]+y
    if board[x][y] == 'R':
        return False
    else:
        board[x][y] = 'I'
        board[jongsu[0]][jongsu[1]] = '.'
        jongsu = [x,y]
        return True

# 미친 아두이노가 움직일 최적의 방향 구함
def check(x,y):
    i,j = jongsu
    result = [float('inf')]

    for t in range(1,10):
        a,b = dic[str(t)]
        dist = abs((x+a) - i) + abs((y+b) - j)
        if dist < result[0]:
            result = [dist, x+a, y+b]

    # 최적의 방향으로 움직일때 종수가 있으면 겜 종료
    return result[1], result[2], True if result[0] == 0 else False

# 미친 아두이노들 움직임 같은 좌표에 있는 아두이노들은 사망
def aduino_move():
    visit = set()
    die = set()

    for aduino in aduinos:
        board[aduino[0]][aduino[1]] = '.'
        i, j, done = check(aduino[0], aduino[1])

        if done:
            return False, set()
        
        if (i,j) in visit:
            die.add((i,j))
        visit.add((i,j))
    
    result = set()
    for i,j in visit:
        if (i,j) not in die:
            board[i][j] = 'R'
            result.add((i,j))

    return True, result

# 주어진 방향으로 종수 이동
turn = 0
for move in input().rstrip():
    turn += 1
    if not jongsu_move(move):
        print(f'kraj {turn}')
        break

    temp, aduinos = aduino_move()
    if not temp:
        print(f'kraj {turn}')
        break
else:
    for b in board:
        print(''.join(b))