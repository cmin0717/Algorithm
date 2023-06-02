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