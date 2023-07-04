const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const nums = Array.from(Array(n), (v,i) => Number(input[i+1]))
let result = 0

const custom_sort = (arr) => {
    if (arr.length <= 1) return

    const mid = Math.floor((Math.min(...arr) + Math.max(...arr)) / 2)
    const idx = arr.indexOf(mid)
    let [left, right] = [[...arr.splice(0,idx)], [...arr.splice(1)]]
    left = left.filter((num) => {
        if (num < mid){
            return true
        }else{
            result++
        }
    })
    right = right.filter((num) => {
        if (num > mid){
            return true
        }else{
            result++
        }
    })
    custom_sort(left)
    custom_sort(right)
}

custom_sort(nums)
console.log(result)