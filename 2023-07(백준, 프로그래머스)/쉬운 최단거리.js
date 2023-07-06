const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input.shift().split(' ').map(Number)
const board = Array.from(Array(n), () => [])
let start = []

input.forEach((line, i) => {
    line = line.split(' ').map(Number)
    board[i] = line
    line.forEach((num, j) => {
        if (num === 2){
            start.push([i,j,0])
        }
    })
})

const visit = Array.from(Array(n), () => Array(m).fill(false))
visit[start[0][0]][start[0][1]] = true

while (start.length !== 0){
    const [x,y,cost] = start.shift()
    board[x][y] = cost

    const arr = [[x,y+1],[x,y-1],[x-1,y],[x+1,y]]
    for (let idx=0;idx<4;idx++){
        const [i,j] = arr[idx]
        if (0 <= i && i < n && 0 <= j && j < m){
            if (board[i][j] !== 0 && !visit[i][j]){
                visit[i][j] = true
                start.push([i,j,cost+1])
            }
        }
    }
}

for (let i=0;i<n;i++){
    for (let j=0; j<m;j++){
        if (board[i][j] === 1 && !visit[i][j]){
            board[i][j] = -1
        }
    }
    console.log(board[i])
}
