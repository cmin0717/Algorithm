const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const boards = Array.from(Array(n), () => Array(m).fill(0))

input[1].split(' ').map(Number).forEach((v,idx) => {
    for(let i=n-1;i >= n-v;i--){
        boards[i][idx] = 2
    }
})

const check = (i,j) => {
    let cnt = 0
    for (let y=j;y<m;y++){
        if (boards[i][y] === 2){
            return cnt
        }else{
            cnt++
        }
    }
    return 0
}

let result = 0
boards.forEach((board,i) => {
    board.forEach((b,j) => {
        if(b === 2 && j !== m-1){
            result += check(i,j+1)
        }
    })
})

console.log(result)