const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const nums = [0].concat(input[1].split(' ').map((num) => Number(num)))

const vator = (x,y,i,j) => {
    return (y-j)/(x-i)
}

let result = 0
for (let i=1;i<=n;i++){
    let [left, right, count] = [Infinity, -Infinity, 0]

    for (let j=i-1; j > 0; j--){
        let num = vator(i,nums[i],j,nums[j])
        if (left > num){
            left = num
            count++
        }
    }
    for (let j=i+1; j <= n; j++){
        let num = vator(i,nums[i],j,nums[j])
        if (right < num){
            right = num
            count++
        }
    }
    result = Math.max(result, count)
}
console.log(result)