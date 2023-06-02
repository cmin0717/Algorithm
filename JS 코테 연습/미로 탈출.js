function solution(n, start, end, roads, traps) {
    
    function made(idx, road) {
        let new_link = [...Array(n+1).keys()].map(_ => [])
        for (let i = 0; i < road.length; i++){
            if (road[i][0] === idx){
                road[i][0] = road[i][1]
                road[i][1] = idx
            }else if (road[i][1] === idx){
                road[i][1] = road[i][0]
                road[i][0] = idx
            }
            let [s,e,c] = road[i]
            new_link[s].push([e,c])
        }
        return [new_link, road]
    }
    
    let link = made('', roads)[0]
    traps = new Set(traps)
    
    let q = [[start, 0, link, roads, []]]
    let result = Infinity
    while(q.length !== 0){
        
        let [now, cnt, arr, road, visit] = q.shift()
        
        if (now === end){
            result = Math.min(cnt, result)
            continue
        }
        if (result < cnt) continue
        
        for (let [idx,c] of arr[now]){
            let check = `${now}.${idx}`
            if (visit.includes(check)) continue
            if (traps.has(idx)){
                let [new_arr, new_road] = made(idx, road)
                q.push([idx, cnt+c, new_arr, new_road, [check, ...visit]])
            }else{
                q.push([idx, cnt+c, arr, road, [check, ...visit]])
            }
        }
    }
    return result
}
// 어렵다... 테스트케이스 7정도 틀렸는데 뭐가 틀린지 모르겠다...
// 빡세네