const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input.shift())
const days = Array(367).fill(0)

for (let i=0;i<n;i++){
    const [s,e] = input[i].split(' ').map(Number)
    days[s] += 1
    days[e+1] -= 1
}

const task = []
let [check, s] = [false, 0]
for (let i=1; i<=365;i++){
    days[i] += days[i-1]

    if (!check && days[i] !== 0){
        s = i
        check = true
    }
    else if (check && days[i] === 0){
        task.push([s,i])
        check = false
    }
}
if (check){
    task.push([s,366])
}

let result = 0
task.forEach((t) => {
    const [s,e] = t
    result += (e-s) * Math.max(...days.slice(s,e))
})
console.log(result)

