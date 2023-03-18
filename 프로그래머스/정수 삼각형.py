def solution(n):
    dp = [[0]*(i+1) for i in range(len(n))]
    dp[0] = n[0][0]
    dp[1][0], dp[1][1] = dp[0] + n[1][0], dp[0] + n[1][1]

    for i in range(2, len(n)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][0] + n[i][0]
            elif j == i:
                dp[i][j] = dp[i-1][-1] + n[i][-1]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + n[i][j]
                
    return max(dp[len(n)-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))