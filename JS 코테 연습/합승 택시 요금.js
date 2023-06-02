function solution(n, s, a, b, fares) {
    let dist = [...Array(n+1).keys()].map(_ => [...Array(n+1).keys()].map(i => Infinity))

    for (let i = 1; i <= n; i++){
        dist[i][i] = 0
    }
    for (let [s,e,cost] of fares){
        dist[s][e] = cost
        dist[e][s] = cost
    }
    
    for (let k = 1; k <= n; k++){
        for (let i = 1; i <= n; i++){
            for (let j = 1; j <= n; j++){
                dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j])
            }
        }
    }
    
    let result = Infinity
    for (let i = 1; i <= n ; i++){
        result = Math.min(result, dist[s][i] + dist[i][a] + dist[i][b])
    }
    return result
}