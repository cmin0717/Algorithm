const input = require('fs').readFileSync('input.txt').toString().split('\n').map(a => a.trim())
const [n,m,k] = input[0].split(' ').map(Number)
let board = Array.from(Array(n), (v,i) => input[i+1].split(''))
// for (let i=1; i < n+1; i++){
//     board.push(input[i].split(''))
// }
board[n-1][0] = 1

const dfs = (x,y,b,cost,result) => {
    if (x === 0 && y === m-1 && cost === k){
        return 1
    }
    if (cost >= k){
        return 0
    }

    const arr = [[x+1, y],[x-1,y],[x,y+1],[x,y-1]]
    for (let [i,j] of arr){
        if (0 <= i && i < n && 0 <= j && j < m && b[i][j] === '.'){
            b[i][j] = cost+1
            result += dfs(i,j,b,cost+1,0)
            b[i][j] = '.'
        }
    }
    return result
}

console.log(dfs(n-1, 0, board, 1, 0))
// import sys
// input = sys.stdin.readline

// n,m,k = map(int,input().split())

// board = [list(input().rstrip()) for _ in range(n)]
// board[n-1][0] = 1


// def dfs(x,y,b,cost,result):
//     if x == 0 and y == m-1 and cost == k:
//         return 1
//     if cost >= k:
//         return 0

//     for i,j in [x+1,y],[x-1,y],[x,y+1],[x,y-1]:
//         if 0 <= i < n and 0 <= j < m and b[i][j] == '.':
//             b[i][j] = cost+1
//             result += dfs(i,j,b,cost+1,0)
//             b[i][j] = '.'
//     return result

// print(dfs(n-1,0,board,1,0))