n = int(input())

dp = [0,1] + [0]*(n-1) # 0,1은 미리 넣어준다. 이따 i-1, i-2를 하기 위해서

for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])