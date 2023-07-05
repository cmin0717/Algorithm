const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n,m] = input[0].split(' ').map(Number)
const board = Array.from(Array(n), (v,i) => input[i+1].split(' ').map(Number))
const visit = Array.from(Array(n), () => Array(m).fill(true))
let result = 0

const change = (x,y,x1,y1,x2,y2) => {
    visit[x][y] = visit[x][y] ? false : true
    visit[x1][y1] = visit[x1][y1] ? false : true
    visit[x2][y2] = visit[x2][y2] ? false : true
}

const check = (i,j,cost) => {
    const arr = [[1,0,0,-1],[0,-1,-1,0],[0,1,-1,0],[1,0,0,1]]
    for (let [dx,dy,dx2,dy2] of arr){
        const [x,y,x2,y2] = [i+dx, j+dy, i+dx2, j+dy2]
        if (0 <= x && x < n && 0 <= x2 && x2 < n && 0 <= y && y < m && 0 <= y2 && y2 < m){
            if (visit[x][y] && visit[x2][y2]){
                const new_cost = board[i][j]*2 + board[x][y] + board[x2][y2]
                change(i,j,x,y,x2,y2)
                dfs(i,j, cost + new_cost)
                change(i,j,x,y,x2,y2)
            }
        }
    }
}

function dfs(x, y, cost) {
    for (let i=x;i<n;i++){
        for (let j= i===x ? y : 0;j<m;j++){
            if (visit[i][j]){
                check(i,j,cost)
            }
        }
    }
    result = Math.max(result, cost)
}

dfs(0,0,0)
console.log(result)