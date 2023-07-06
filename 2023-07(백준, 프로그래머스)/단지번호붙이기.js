const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input.shift())
const board = Array.from(Array(n), (v,i) => input[i].split('').map(Number))
const visit = Array.from(Array(n), () => Array(n).fill(false))

const dfs = (i,j) => {
    const stack = [[i,j]]
    let cnt = 1
    visit[i][j] = true

    while (stack.length !== 0){
        const [x, y] = stack.pop()

        const arr = [[x,y+1],[x,y-1],[x-1,y],[x+1,y]]
        for (let idx=0; idx<4;idx++){
            const [a,b] = arr[idx]
            if (0 <= a && a < n && 0 <= b && b < n && board[a][b] === 1 && !visit[a][b]){
                visit[a][b] = true
                stack.push([a,b])
                cnt++
            }

        }
    }
    return cnt
}

const result = []
for (let i=0;i<n;i++){
    for (let j=0;j<n;j++){
        if (board[i][j] !== 0 && !visit[i][j]){
            result.push(dfs(i,j))
        }
    }
}
console.log(result.length)
result.sort((a,b) => a-b).forEach((num) => console.log(num))