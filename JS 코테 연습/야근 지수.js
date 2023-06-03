function solution(n, works) {
    let tt = works.reduce((a,b) => a+b)
    if (tt <= n) return 0
    
    let avg = Math.floor((tt-n)/works.length)
    let arr = works.filter(w => w <= avg)
    
    let rest = tt-n
    for (let i of arr){
        rest -= i
    }
    
    let p = works.length - arr.length
    let [div, mod] = [Math.floor(rest/p), rest%p]
    
    let arr2 = [...Array(p-mod).keys()].map(_ => div)
    let arr3 = [...Array(mod).keys()].map(_ => div+1)
    
    let result = [...arr, ...arr2, ...arr3]
    let cnt = 0
    for (let i of result){
        cnt += Math.pow(i, 2)
    }
    return cnt
}
solution(	5, [2, 3, 10])

// heapq 안쓰고 풀고 있는데 아무리봐도 이거 답임.
// 반박시 내말이 다 맞음 시발.....
// 도저히 반레를 못찾겠다...

// 그냥 최대값을 하나씩 빼는 완탐으로 구현했다.
function solution(n, works) {
    
    if (works.reduce((a,b) => a+b) <= n) return 0
    
    while (n !== 0){
        
        let [max, idx] = [0, 0]
        for (let i = 0; i<works.length; i++){
            if (max < works[i]){
                max = works[i]
                idx = i
            }
        }
        n -= 1
        works[idx] -= 1
    }
    
    let result = 0
    for (let i of works){
        result += i**2
    }
    return result
}



// 파이썬 heapq 사용 풀이
// from heapq import *

// def solution(n, works):
    
//     h = [-w for w in works]
//     heapify(h)
    
//     while h and n != 0:
//         num = heappop(h)
//         n -= 1
//         if (num + 1) < 0:
//             heappush(h, num+1)
    
//     return sum([i**2 for i in h])