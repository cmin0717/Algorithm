function solution(n, money) {
    
    let dp = [...Array(n+1).keys()].map(_ => 0)
    dp[0] = 1
    
    for (let m of money){
        for (let i = m; i <= n; i++){
            dp[i] += dp[i-m]%1000000007
        }
    }
    
    return dp[n]%1000000007
}