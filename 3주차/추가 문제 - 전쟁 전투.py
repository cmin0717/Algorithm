import sys
input = sys.stdin.readline

n, m = map(int,input().split())

war = [input().rstrip() for _ in range(n)]
check = [[0] * m for _ in range(n)] # 방문 체크용

w = 0
b = 0

def dfs(x,y,team):
    global cnt
    check[x][y] = 1
    for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if 0 <= a < n and 0 <= b < m and war[a][b] == team and check[a][b] == 0: # 조건 체크
            cnt += 1
            dfs(a,b,team)

for i in range(n):
    for j in range(m):
        cnt = 1
        if war[i][j] == 'W' and check[i][j] == 0:
            dfs(i,j,'W')
            w += cnt**2
            continue
        if war[i][j] == 'B' and check[i][j] == 0:
            dfs(i,j,'B')
            b += cnt**2
print(w, b)