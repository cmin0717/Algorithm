const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n,m] = input[0].split(' ').map(Number)
const board = Array.from(Array(n), () => [])
let [jihoon, fire] = [[],[]]

for (let i =1; i<input.length; i++){
    const line = input[i].split('')
    board[i-1] = line

    line.forEach((v,j) => {
        if (v === 'J'){
            jihoon.push([i-1,j,0])
        }else if (v === 'F'){
            fire.push([i-1,j])
        }
    })
}

let result = Infinity

const move_jihoon = (arr) => {
    const new_jihoon = []
    arr.forEach((v) => {
        let [x,y,cost] = v

        if (board[x][y] === 'J'){
            let check = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
            check.forEach((v2) => {
                let [i,j] = v2
                if (0 <= i && i < n && 0 <= j && j < m){
                    if (board[i][j] === '.'){
                        new_jihoon.push([i,j,cost+1])
                        board[i][j] = 'J'
                    }
                }else{
                    result = Math.min(result, cost+1)
                }
            })
        }
    })
    return new_jihoon
}

const move_fire = (arr) => {
    const new_fire = []
    arr.forEach((v) => {
        let [x,y] = v
        let check = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        check.forEach((v2) => {
            let [i,j] = v2
            if (0 <= i && i < n && 0 <= j && j < m){
                if (board[i][j] === '.' || board[i][j] === 'J'){
                    new_fire.push([i,j])
                    board[i][j] = 'F'
                }
            }
        })
    })
    return new_fire
}

while (jihoon.length !== 0){
    jihoon = move_jihoon(jihoon)
    fire = move_fire(fire)
}
console.log(result !== Infinity ? result : 'IMPOSSIBLE')