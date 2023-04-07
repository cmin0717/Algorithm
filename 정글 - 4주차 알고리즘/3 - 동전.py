test_case = int(input())

for _ in range(test_case):
    n = int(input())
    coins = list(map(int,input().split()))
    money = int(input())
    dp = [1] + [0] * money

    for coin in coins: # 중복을 막기 위해 코인을 하나씩 빼서 조합한다.
        for j in range(1,money+1):
            if j - coin >= 0: # 빼서 음수가 아니면 코인을 사용하여 새로운 조합을 만들수있다.
                dp[j] += dp[j-coin]
                
    print(dp[money])

