n = int(input())

dp = [0]*1001 # 미리 1000개의 이모티콘의 최소값을 다 넣어주기 위해 만듬

for i in range(2,1001):
    li = []
    for j in range(1,i//2+1): # 나누어 지는 숫자을 파악
        if i % j == 0:
            li.append(dp[j] + i//j) # 나누어 진다면 나눌수있는 수의 dp값과 몫을 더해주면 된다. 복사 붙여넣기 하면 되니깐
    dp[i] = min(li) # 나누어 지는 수중에 최소값을 넣어준다.
    for l in range(i-1,-1,-1): # 3번 조건을 맞추기위해 새로 만든 dp값에 -1씩 빼는게 더 작다면 해당 값을 갱신해준다.
        dp[l] = min(dp[l], dp[i]-l+i)

print(dp[n])

# 그래프로는 어떻게 풀지 감이 안잡힌다....