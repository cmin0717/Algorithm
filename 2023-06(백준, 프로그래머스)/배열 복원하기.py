import sys
input = sys.stdin.readline

h, w, x, y = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h+x)]

for i in range(h):
    for j in range(w):
        # 새롭게 더할 범위에 있는 애들만 값을 재정립
        if x <= i < h+x and y <= j < w+y:
            board[i][j] -= board[i-x][j-y]
        

for i in board[:h]:
    print(*i[:w])

