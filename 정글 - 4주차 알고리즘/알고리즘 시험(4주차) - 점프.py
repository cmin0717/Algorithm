n = int(input())

pan = [list(map(int,input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if dp[i][j] != 0:
            for x,y in [i+pan[i][j], j],[i, j+pan[i][j]]:
                if 0 <= x < n and 0 <= y < n:
                    dp[x][y] += max(dp[i][j], 1)

print(dp[n-1][n-1])