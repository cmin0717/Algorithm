function solution(word) {
    let list = []

    let check = word[0]
    let cnt = 1
    for (let i =1;i<word.length;i++){
        if (word[i] === check){
            cnt++
        }else{
            list.push(check === 'A' ? [0,cnt] : [1,cnt])
            cnt = 1
            check = word[i]
        }
    }
    list.push(check === 'A' ? [0,cnt] : [1,cnt])
    
    let result = 0
    let len = list.length
    for(let i = 1;i<len;i++){
        if (list[i][0] === 0){
            let n = 0
            if (list[i-1][0] === 1){
                n += list[i-1][1]
            }
            if (i+1 < len && list[i+1][0] === 1){
                n += list[i+1][1]
            }
            if (n > list[i][1]){
                result += list[i][1]
                if (i+1<len) list[i+1][1] = n
            }else{
                result += list[i-1][1]
            }
        }
    }
    return result
}

solution('BBABAA')