const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = [input[0], input[1]].map(Number)
let link = Array.from(Array(n+1), () => [])
let board = Array.from(Array(n+1), () => Array(n+1).fill(Infinity))

for (let i = 2; i<input.length-1; i++){
    input[i].split(' ').filter((v,idx) => {
        if (v !== '0'){
            link[i-1].push(idx+1)
            link[idx+1].push(i-1)
            board[i-1][idx+1] = 0
        }
    })
    board[i-1][i-1] = 0
}

for (let k = 1; k <= n; k++){
    for (let i =1;i <= n; i++){
        for (let j =1;j <= n; j++){
            board[i][j] = Math.min(board[i][j], board[i][k]+board[k][j])
        }
    }
}

const arr = input[input.length-1].split(' ').map(Number)
let result = true
for (let i =0;i < arr.length-1; i++){
    if (board[arr[i]][arr[i+1]] === Infinity){
        result = false
        break
    }
}
console.log(result ? 'YES' : 'NO')
