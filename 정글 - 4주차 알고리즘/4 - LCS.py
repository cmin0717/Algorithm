word1 = input()
word2 = input()

dp = [0] * len(word2) 

for i in range(len(word1)):
    cnt = 0
    for j in range(len(word2)):
        if cnt < dp[j]: # 현재까지 공통수열이되는 문자가 있다면 cnt값을 갱신
            cnt = dp[j]
        elif word1[i] == word2[j]: # 공통 수열이 된다면 cnt값에 +1 해서 dp값에 넣어준다.
            dp[j] = cnt + 1
print(max(dp))

