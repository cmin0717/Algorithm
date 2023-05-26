def solution(sticker):
    n = len(sticker)
    # 스티커를 하나만 사용할수있다면 바로 최대값 리턴
    if n < 3:
        return max(sticker)
    
    # 첫번째 스트커를 사용하는 경우
    dp = [0] * n
    dp[0], dp[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, n-1):
        dp[i] = max(dp[i-1], dp[i-2] + sticker[i])
    
    # 첫번째 스티커를 사용하지 않는 경우
    dp2 = [0] * n
    dp2[0], dp2[1] = 0, sticker[1]
    for i in range(2,n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    return max(max(dp), max(dp2))