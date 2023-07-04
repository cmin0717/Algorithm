const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const water = input[1].split(' ').map(Number)

let [left, right] = [0, n-1]
let result = [water[left], water[right]]
let standard = Math.abs(result.reduce((a,b) => a+b))

while (left !== right){
    const mid = water[left] + water[right]

    if (Math.abs(mid) < standard){
        standard = Math.abs(mid)
        result = [water[left], water[right]]
        if (standard === 0) break
    }

    if (mid < 0){
        left += 1
    }else{
        right -= 1
    }
}

console.log(...result)