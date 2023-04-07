function solution(A) {
    let dic = {}
    let max = 0
    for (let i of A){
        max = Math.max(max, Number(i))
        if (dic[i] === undefined){
            dic[i] = 1
        }else{
            dic[i]++
        }
    }
    
    let result = 1
    for (let i of Object.keys(dic)){
        if (Number(i) !== max){
            result += dic[i] > 1 ? 2 : 1
        }
    }
    return result
}
