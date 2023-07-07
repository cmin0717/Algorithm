const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const cnt = (arr) => {
    let c = 0
    arr.forEach((num) => {
        if (Number(num) % 2 !== 0){
            c++
        }
    })
    return c
}

const check = (arr, s, m, e) => {
    s = Number(s.join(''))
    m = Number(m.join(''))
    e = Number(e.join(''))
    return [(s+m+e).toString().split(''), cnt(arr)]
}

const dfs = (arr, count) => {
    const n = arr.length
    if (n === 1){
        result.push(count + cnt(arr))
        return
    }

    if (n == 2){
        const [num, c] = check(arr, [arr[0]],[],[arr[1]])
        dfs(num, count+c)
        return
    }

    for (let i=0;i<n-1;i++){
        for (let j=i+1;j<n-1;j++){
            let new_num = [...arr]
            let [s,m,e] = [new_num.slice(0,i+1), new_num.slice(i+1,j+1), new_num.slice(j+1)]
            const [num, c] = check(new_num, s,m,e)
            dfs(num, count+c)
        }
    }
}

let result
function solution(num){
    result = []
    dfs(num, 0)
    console.log(Math.min(...result), Math.max(...result))
}

input.forEach((num) => {
    solution(num.split(''))
})