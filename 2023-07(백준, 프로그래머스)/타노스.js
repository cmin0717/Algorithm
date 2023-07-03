const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const arr = input[0].split('')

let [c0, c1] = [0, 0]
let [arr_0, arr_1] = [[], []]

arr.forEach((num, i) => {
    if (num === '0'){
        c0++
        arr_0.push(i)
    }else{
        c1++
        arr_1.push(i)
    }   
})

for (let i=0; i<c0/2; i++){
    arr_0.pop()
}
for (let i=0; i<c1/2; i++){
    arr_1.shift()
}

const nums = [...arr_0, ...arr_1].sort((a,b) => a-b)
console.log(nums.map(i => arr[i]).join(''))

