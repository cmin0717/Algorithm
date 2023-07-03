const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const link = new Map()

for (let i=0; i<n; i++){
    const [s, e, cost] = input[i+1].split(' ').map(Number)
    if (link.has(s)){
        let temp = link.get(s)
        temp.push([e,cost])
        link.set(s, temp)
    }else{
        link.set(s,[[e,cost]])
    }
}

let q = [[0,0]]
const visit = new Array(m+1).fill(Infinity)
visit[0] = 0

while (q.length !== 0){
    let [now, cost] = q.shift()

    if (now >= m) continue

    if (link.has(now)){
        for (let [i,c] of link.get(now)){
            if (visit[i] > cost+c){
                q.push([i, cost+c])
                visit[i] = cost+c
            }
        }
    }
    if (visit[now+1] > cost+1){
        q.push([now+1, cost+1])
        visit[now+1] = cost+1
    }
}
console.log(visit[m])