const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const link = Array.from(Array(n+1), () => [])
const [start, end] = input[m+1].split(' ').map(Number)

for (let i=1;i<=m;i++){
    const [s,e] = input[i].split(' ').map(Number)
    link[s].push(e)
    link[e].push(s)
}

link.map((i) => i.sort((a,b) => a-b))
  
const find = (start, end) => {
    let q = [[start, [start], end]]
    let visit = new Set([start])
    while (q.length !== 0){
        let [now, v, result] = q.shift()
        
        if (now === result){
            if (result === end){
                visit = new Set(v)
                visit.delete(start)
                result = start
                q = []
            }else{
                return v.length-1
            }
        }
    
        for (let i=0;i<link[now].length;i++){
            const next = link[now][i]
            if (!visit.has(next)){
                q.push([next, v.concat(next), result])
                visit.add(next)
            }
        }
    }
}

console.log(find(start, end))