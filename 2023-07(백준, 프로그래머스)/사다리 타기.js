const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input.shift())
const m = Number(input.shift())
let [start, end] = [input[0].split('').sort().map((s,i) => [s,0,i]) ,input.shift().split('').map((s,i) => [s,m-1,i])]
const board = []
let secret

for (let i=0;i<m;i++){
    const line = input[i].split('')
    if (line[0] === '?'){
        secret = i
    }
    board.push(line)
}

const make = (d,arr) => {
    const dx = d === 'U' ? 1 : -1
    const idx = d === 'U' ? 0 : m-1

    for (let i=idx;i !== secret;i += dx){
        for (let j=0;j<n;j++){
            const [s,x,y] = arr[j]
            if (y-1 >= 0 && board[x][y-1] === '-'){
                arr[j] = [s, x+dx, y-1]
            }else if (board[x][y] === '-'){
                arr[j] = [s, x+dx, y+1]
            }else{
                arr[j] = [s, x+dx, y]
            }
        }
    }
    const line = Array(n).fill('')
    arr.forEach((info) => {
        const [s,x,y] = info
        line[y] = s
    })
    return line
}

const up = make('U', start)
const down = make('D', end)

let result = []
for (let i=0;i<n-1;i++){
    if (up[i] === down[i]){
        result.push('*')
    }else if (up[i] === down[i+1]){
        result.push('-')
        const temp = up[i+1]
        up[i+1] = up[i]
        up[i] = temp
    }else{
        result = Array(n-1).fill('x')
        break
    }
}
console.log(result.join(''))