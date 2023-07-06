const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

function solution(num){
    const [x, y] = num.split(' ').map(Number)
    let range = Math.max(x*2, y*2)
    range = Math.min(range, 100001)
    const line = Array(range).fill(Infinity)
    line[x] = 0
    const q = [[x,0]]
    
    while (q.length !== 0){
        const [idx, cost] = q.shift()
    
        if (line[idx] < cost) continue

        if (idx === y){
            console.log(cost)
            break
        }
    
        if (idx*2 < range && line[idx*2] > cost){
            q.unshift([idx*2, cost])
            line[idx*2] = cost
        }
        if (idx-1 >= 0 && line[idx-1] > cost+1){
            q.push([idx-1, cost+1])
            line[idx-1] = cost+1
        }
        if (idx+1 < range && line[idx+1] > cost+1){
            q.push([idx+1, cost+1])
            line[idx+1] = cost+1
        }
    }
}

input.forEach((num) => {
    solution(num)
})

