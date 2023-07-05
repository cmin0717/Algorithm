const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const nums = Array.from(Array(n), (v,i) => Number(input[i+1]))

const dp = new Array(n).fill(1)

for (let i = 0; i<n; i++){
    for (let j=0; j<i; j++){
        if (nums[j] < nums[i]){
            dp[i] = Math.max(dp[i], dp[j]+1)
        }
    }
}

console.log(n-Math.max(...dp))

let range = {from: 1, to: 5} // 이터러블 객체

range[Symbol.iterator] = function () {

    // 이터레이터 객체
    return {
        now: this.from,
        last: this.to,

        next(){
            if (this.now <= this.last){
                return {done: false, value: this.now++}
            }else{
                return {done: true}
            }
        }
    }
}
for (let i of range){
    console.log(i)
}