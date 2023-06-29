// import sys
// input = sys.stdin.readline

// n, m = map(int,input().split())
// days = [list(map(int, input().split())) for _ in range(m)]

// total = n*2-1
// board = [0] * total

// for z,o,t in days:
//     if o != 0:
//         board[total-(o+t)] += 1
//         if t != 0:
//             board[total-t] += 1
//     else:
//         if t != 0:
//             board[total-t] += 2

// board[0] += 1
// for i in range(1,n*2-1):
//     board[i] += board[i-1]

// temp = board[n:]
// for i in range(n-1,-1,-1):
//     print(board[i], *temp)

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n,m] = input[0].split(' ').map(Number)
const total = n*2-1
const board = new Array(total).fill(0)

for (let i =0; i<m; i++){
    const [z,o,t] = input[i+1].split(' ').map(Number)
    if (o !== 0){
        board[total-(o+t)] += 1
        if (t !== 0){
            board[total-t] += 1
        }
    }else{
        if (t !== 0){
            board[total-t] += 2
        }
    }
}

board[0] += 1
for (let i=1; i<total; i++){
    board[i] += board[i-1]
}

const temp = board.splice(n)
for (let i=n-1; i >= 0; i--){
    console.log(board[i],...temp)
}