function solution(gems) {
    const n = new Set(gems).size
    const m = gems.length
    // Object말고 map를 사용해야한다.
    let map = new Map()
    map.set(gems[0], 1)
    let result = [1, 100000]
    let l = 0
    let r = 0
    
    while (l <= r && r < m){
        if (map.size === n){
            if (result[1] - result[0] > r-l){
                result = [l+1, r+1]
            }
            map.set(gems[l], map.get(gems[l])-1)
            if (map.get(gems[l]) === 0){
                map.delete(gems[l])
            }
            l += 1
        }else{
            r += 1
            if (r === m) break
            if (!map.has(gems[r])){
                map.set(gems[r], 0)
            }
            map.set(gems[r], map.get(gems[r])+1)
        }
    }
    return result
}
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])