import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(n)]

dp = [[-1]*m for _ in range(n)]

def check(x,y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0

    for a,b in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
        if 0 <= a < n and 0 <= b < m:
            if maps[x][y] > maps[a][b]:
                dp[x][y] += check(a,b)
    return dp[x][y]

check(0,0)
print(dp[0][0])