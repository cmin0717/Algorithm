function solution(n, s) {
    let [num, rest] = [Math.floor(s/n), s%n]
    if (num === 0){
        return [-1]
    }
    
    num = [...Array(n-rest).keys()].map(_ => num)
    rest = [...Array(rest).keys()].map(_ => num[0]+1)
    return [...num, ...rest]
}