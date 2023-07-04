const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const link = Array.from(Array(n+1), () => [])

for (let i=1;i<=m;i++){
    const [s,e,cost] = input[i].split(' ').map(Number)
    link[s].push([e,cost])
    link[e].push([s,cost])
}

const dist = Array(n+1).fill(Infinity)
const q = [[1,0]]
dist[1] = 0

while (q.length !== 0){
    const [idx, cost] = q.shift()

    if (dist[idx] < cost) continue

    for (let [next, c] of link[idx]){
        const new_cost = dist[idx] + c
        if (dist[next] > new_cost){
            dist[next] = new_cost
            q.push([next, new_cost])
        }
    }
}
console.log(dist[n])