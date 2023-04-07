n = int(input())

dp = [0,1,2] + [0] * (n-2) 

for i in range(3,n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 모듈러 연산을 이용해서 미리 나머지를 넣어준다. 안해주면 메모리 초과 뜬다.

print(dp[n])
