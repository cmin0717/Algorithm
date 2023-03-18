from collections import deque

def solution(m, n, p):
    dp = [[0]*m for _ in range(n)]
    for xy in p:
        x,y = xy[0],xy[1]
        dp[y-1][x-1] = -1
        
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1 : continue
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            for x,y in [i-1,j],[i,j-1]:
                if 0 <= x and 0 <= y and dp[x][y] != -1:
                    dp[i][j] += dp[x][y] % 1000000007

    return dp[n-1][m-1] % 1000000007

solution(4,3,[[2,2],[1,3]])