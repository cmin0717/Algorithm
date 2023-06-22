import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 치즈의 좌표 저장
cheeses = set()
# 확장 해야 할 좌표
check_arr = []

for i in range(n):
    for j in range(m):
        # 치즈 추가
        if board[i][j] == 1:
            cheeses.add((i,j))
        # 가장 자리를 제외한 부분중 치즈가 아닌 부분은 2로 변경
        elif 0 < i < n-1 and 0 < j < m-1 and board[i][j] == 0:
            board[i][j] = 2
        # 나머지는 확장 해야할 좌표에 저장
        else:
            check_arr.append([i,j])

# 치즈 외부 공간 표시 작업
def change(x,y):
    q = deque([[x,y]])

    while q:
        i,j = q.popleft()

        for a,b in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
            if 0 <= a < n and 0 <= b < m and (board[a][b] == 2 or board[a][b] == 0):
                board[a][b] = 3
                q.append([a,b])

# 확장해야할 좌표를 이용하여 치즈 외부 공간 표시
def out(arr):
    for i,j in arr:
        if board[i][j] == 0:
            board[i][j] = 3
            change(i,j)

# 녹아 버릴 치즈 삭제
def del_cheese():
    remove = []
    for i,j in cheeses:
        c = 0
        for a,b in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
            if 0 <= a < n and 0 <= b < m and board[a][b] == 3:
                c += 1
        if c >= 2:
            remove.append([i,j])
    return remove

turn = 0
while cheeses:

    # 치즈 외부 공간 표시
    out(check_arr)

    # 치즈 삭제
    check_arr = []
    for i,j in del_cheese():
        cheeses.remove((i,j))
        check_arr.append([i,j])
        board[i][j] = 0

    turn += 1
print(turn)