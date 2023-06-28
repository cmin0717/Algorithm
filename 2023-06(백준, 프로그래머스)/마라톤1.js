const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const arr = Array.from(Array(n), (v,i) => input[i+1].split(' ').map(Number))

const check = (idx) => {
    const [x,y] = arr[idx]
    const [x1,y1] = arr[idx-1]
    const [x2,y2] = arr[idx+1]
    let later = Math.abs(x1-x) + Math.abs(y1-y)
    let next = Math.abs(x2-x) + Math.abs(y2-y)
    let del = Math.abs(x1-x2) + Math.abs(y1-y2)

    return [later, next, del]
}

const result = []
let [idx, cost, total] = [0,0,0] 
for (let i = 1; i<n-1; i++){
    const [l, nt, d] = check(i)
    if (l+nt-d > cost){
        idx = i
        cost = l+nt-d
    }
    total += i !== n-2 ? l : l+nt
    result.push(d-nt-l)
}
console.log(total + result[idx-1])
