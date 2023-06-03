function solution(sequence) {
    let n = sequence.length
    let dp = [[],[]]

    for (let i in sequence){
        dp[0].push(sequence[i])
        dp[1].push(-sequence[i])
    }
    
    let result = Math.max(dp[0][0], dp[1][0])
    for (let i = 1; i < n; i++){
        dp[0][i] = Math.max(dp[0][i], dp[0][i] + dp[1][i-1])
        dp[1][i] = Math.max(dp[1][i], dp[1][i] + dp[0][i-1])
        result = Math.max(result, dp[0][i], dp[1][i])
    }
    
    return result
    // 아래와 같이 진행되면 메모리를 상당히 많이 먹는것 같다.
    // ...연산자를 사용시 새로운 리스트를 만들기에 그러는듯
    // return Math.max(...dp[0],...dp[1])
}