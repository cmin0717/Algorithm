import sys
input = sys.stdin.readline

# 각 물건 마다 dp리스트를 만들어서 해결

n,k = map(int,input().split())
items = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * (k+1) for _ in range(n+1)] # 중복 계산을 막기 위해 각 물건마다 memo생성

for i in range(1,n+1):
    for j in range(1,k+1):
        if j - items[i-1][0] >= 0: # 다른 물건과 같이 담을수있는 조건이 되면
            dp[i][j] = max(dp[i-1][j - items[i-1][0]] + items[i-1][1], dp[i-1][j]) 
        else:
            dp[i][j] = dp[i-1][j] # 뭐가 없으면 전에 dp값을 가져온다.

print(max(dp[n]))

# ---------------------------------------------------------------------------------------------------------

# dp리스트를 하나만 사용하여 갱신해가며 해결하는 방법 (메모리,시간을 봤을때 훨씬 좋다. )

n,k = map(int,input().split())

dp = [0] * (k+1) # 리스트를 하나만 사용하여 갱신해간다

for _ in range(n):
    item_w,item_v = map(int,input().split())

    if item_w > k:continue

    for i in range(k,0,-1): # 중복값을 없애기 위해 뒤에서 부터 값을 채워간다.
        if i + item_w <= k and dp[i] != 0: # 해당 무게에 값이 있고 같이 가방에 담을수 있다면
            dp[i + item_w] = max(dp[i + item_w], dp[i] + item_v)
    dp[item_w] = max(dp[item_w], item_v) # 주어진 물건의 해당하는 무게에 가치를 넣어준다. 원래 값과 비교해서 큰값으로

print(max(dp))