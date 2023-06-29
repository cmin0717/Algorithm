const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const boards = Array.from(Array(n), (v,i) => input[i+1].split(' ').map(Number))
const sharks = []

boards.forEach((board, i) => {
    board.forEach((b, j) => {
        if (b === 1){
            sharks.push([i,j])
        }
    })
})

let count = 0
boards.forEach((board, i) => {
    board.forEach((b, j) => {
        let check = Infinity
        sharks.forEach((shark) => {
            const [x, y] = shark
            const dist = Math.max(Math.abs(i-x), Math.abs(j-y))
            check = Math.min(check, dist)
        })
        count = Math.max(count, check)
    })
})
console.log(count)

// import sys
// from collections import deque
// input = sys.stdin.readline

// n,m = map(int, input().split())
// board = [list(map(int, input().split())) for _ in range(n)]
// visit = [[True] * m for _ in range(n)]
// sharks = []
// for i in range(n):
//     for j in range(m):
//         if board[i][j] == 1:
//             sharks.append([i,j])
//             visit[i][j] = False
            
// q = deque(sharks)
// while q:
//     x,y = q.popleft()
    
//     for i,j in [x+1,y],[x+1,y+1],[x+1,y-1],[x-1,y],[x-1,y-1],[x-1,y+1],[x,y-1],[x,y+1]:
//         if 0 <= i < n and 0 <= j < m and visit[i][j] and board[i][j] < board[x][y]:
//             board[i][j] = board[x][y]+1
//             visit[i][j] = False
//             q.append([i,j])

// count = 0
// for i in range(n):
//     for j in range(m):
//         count = max(count, board[i][j])
// print(count-1)