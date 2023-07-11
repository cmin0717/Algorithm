import sys
input = sys.stdin.readline

n = int(input())
board = [[float('inf')] * (n+1) for _ in range(n+1)]
for i in range(1,n+1):
    board[i][i] = 0

while True:
    s,e = map(int,input().split())

    if s == -1 and e == -1:
        break
    board[s][e] = 1
    board[e][s] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            board[i][j] = min(board[i][j], board[i][k] + board[k][j])

score = min([max(board[i][1:]) for i in range(1,n+1)])
student = [i for i in range(1,n+1) if score == max(board[i][1:])]
print(score, len(student))
print(*sorted(student))