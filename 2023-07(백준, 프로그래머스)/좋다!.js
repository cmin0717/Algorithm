const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const nums = input[1].split(' ').map(Number)
const kind = new Map()

nums.forEach((num, i) => {
    if (kind.has(num)){
        kind.set(num, [...kind.get(num), i])
    }else{
        kind.set(num, [i])
    }
})

let result = new Set()
for (let i=0;i<n;i++){
    for (let j=i+1;j<n;j++){
        const num = nums[i] + nums[j]
        if (kind.has(num)){
            const temp = []
            kind.get(num).forEach((m) => {
                if (m !== i && m !== j){
                    result.add(m)
                }else{
                    temp.push(m)
                }
            })
            kind.set(num, temp)
        }
    }
}

console.log(result.size)