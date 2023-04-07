function solution(M, N) {
    let total = M + N*4
    let max = Math.floor(total**0.5)
    
    for (let i = max;i>=0;i--){
        let s = i**2
        let cnt_n = 0

        if (i%2 !== 0){
            let max_n = Math.floor(i / 2)**2
            cnt_n = N > max_n ? max_n : N
        }else{
            cnt_n = N > (i/2)**2 ? (i/2)**2 : N
        }
        
        if (s <= (cnt_n*4)+M) return i
    }
}

console.log(solution(0,18))