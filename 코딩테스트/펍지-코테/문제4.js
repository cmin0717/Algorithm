function solution(S) {
    let check = {}
    let result = -1

    for (let i =0;i<S.length-1;i++){
        let word = S[i] + S[i+1]

        if (check[word] === undefined){
            check[word] = [i]
        }else{
            check[word].push(i)
            result = Math.max(result, i - check[word][0])
        }
    }
    
    return result
}