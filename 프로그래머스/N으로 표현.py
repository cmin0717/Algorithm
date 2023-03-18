def check(arr,idx,dp):
    for i in range(1,(idx+1)//2+1):
        for x in arr[idx-i]:
            for y in arr[i]:
                if x - y > 0: dp.add(x-y)
                dp.add(x+y)
                dp.add(x*y)
                if x // y != 0 : dp.add(x//y)
    return dp

def solution(n, num):
    dp = [set()] * (9)
    dp[1].add(n)
    if num in dp[1]: return 1

    for i in range(2,9):
        dp[i] = check(dp, i, set())
        dp[i].add(int(str(n)*i))
        if num in dp[i]:
            return i
    else:
        return -1