import sys
input = sys.stdin.readline

n = int(input())
step = [0] + [int(input()) for _ in range(n)] # 0번째 인덱스 쓰기위해
dp = [0]

for i in range(1,n+1):
    if i < 3: # 1,2,는 다 더하는게 젤 높을수 밖에 없다
        dp.append(step[i]+sum(dp))
        continue
    # 현재값 + 전값 + 전전전dp값을 더하는 방법과 현재값 + 전전dp값을 더하는 방법 두가지 방법만 존재
    dp.append(max(step[i]+step[i-1]+dp[i-3], step[i]+dp[i-2])) # 둘중 큰걸 dp에 넣어주고 진행행

print(dp[-1])