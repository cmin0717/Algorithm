function solution(ex) {
    let op = []
    
    for (let i =0; i < ex.length; i++){
        if (ex[i] === '-' || ex[i] === '+' || ex[i] =='*'){
            op.push(ex[i])
        }
    }
    op = [...new Set(op)]
    
    for (i of op){
        ex = ex.replaceAll(i, `,${i},`)
    }
    ex = ex.split(',')

    if (op.length === 3){
        op = [['-', '+', '*'],['-', '*', '+'],['*', '+', '-'],['*', '-', '+'],['+', '-', '*'],['+', '*', '-']]
    }else if (op.length === 2){
        op = [op, [op[1], op[0]]]
    }
    
    // JS에서 무한대 값 넣기
    let result = -Infinity
    for (i of op){
        // map매서드를 이용한 깊은 복사
        let copy = [...Array(ex.length).keys()].map(n => ex[n])
        for (j of i){
            let check = []
            while (copy.length !== 0){
                let p = copy.shift()
                if (p === j && p === '+'){
                    check.push(Number(check.pop()) + Number(copy.shift()))
                }else if(p === j && p === '-'){
                    check.push(Number(check.pop()) - Number(copy.shift()))
                }else if(p === j && p === '*'){
                    check.push(Number(check.pop()) * Number(copy.shift()))
                }else{
                    check.push(p)
                }
            }
            copy = check
        }
        result = Math.max(result, Math.abs(copy[0]))
    }
    
    return result
}
solution("100-200*300-500+20")