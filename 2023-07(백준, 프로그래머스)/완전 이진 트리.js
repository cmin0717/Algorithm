const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const h = Number(input.shift())
const nums = input.shift().split(' ').map(Number)
const n = nums.length-1

const tree = new Map()
const result = Array.from(Array(h), () => [])

const dfs = (s,e,idx, cost) => {
    result[cost].push(nums[idx])

    if (s === e && s === idx){
        tree.set(nums[idx], [cost])
        return
    }

    const left = Math.floor((idx-s) /2) + s
    const right = Math.floor((e-idx) /2) + idx+1

    tree.set(nums[idx], [cost, nums[left], nums[right]])

    dfs(s,idx-1,left, cost+1)
    dfs(idx+1,e,right, cost+1)
}
const root = Math.floor(n/2) 
dfs(0, n, root, 0)

// const pos = (node) => {
//     if (tree.get(node).length === 1){
//         const h = tree.get(node)
//         result[h].push(node)
//         return
//     }

//     const [h, l, r] = tree.get(node)
//     result[h].push(node)
//     if (tree.has(l)){
//         pos(l)
//     }
//     if (tree.has(r)){
//         pos(r)
//     }
// }
// pos(nums[root])

result.forEach((i) => console.log(...i))