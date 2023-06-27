const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const dic = {0: [1,1,1,1],1: [0,1,1,1], 2: [1,1,0,1], 4: [1,0,1,1], 8: [1,1,1,0], 14: [1,0,0,0],
       3: [0,1,0,1], 5: [0,0,1,1], 9: [0,1,1,0], 7: [0,0,0,1], 12: [1,0,1,0],
       11: [0,1,0,0], 13: [0,0,1,0], 10: [1,1,0,0], 6: [1,0,0,1], 15: [0,0,0,0]}
const dict = [[0,-1],[0,1],[-1,0],[1,0]]

const board = Array.from(Array(m), (v,i) => input[i+1].split(' ').map(a => dic[Number(a)]))
const visit = Array.from(Array(m), () => Array(n).fill(true))

const find = (x,y) => {
    const q = [[x,y]]
    const rooms = new Set()
    visit[x][y] = false

    while (q.length !== 0){
        const [i, j] = q.shift()
        rooms.add(`${i}-${j}`)

        for (let idx = 0; idx < 4; idx++){
            if (board[i][j][idx] !== 0){
                const [a,b] = [i + dict[idx][0], j+ dict[idx][1]]
                if (0 <= a && a < m && 0 <= b && b < n && visit[a][b]){
                    q.push([a,b])
                    visit[a][b] = false
                }
            }
        }
    }
    return rooms
}

let [rooms, num, maxr] = [new Map(), 0, 0]
for (let i = 0; i < m;i++){
    for (let j = 0;j < n;j++){
        if (visit[i][j]){
            num++
            const room = find(i,j)
            rooms.set(num, room)
            maxr = Math.max(maxr, room.size)
        }
    }
}

const find_room = (x,y) => {
    for (let [k,v] of rooms.entries()){
        if (v.has(`${x}-${y}`)){
            return k
        }
    }
}

const check = (i,j) => {
    const now_room = find_room(i,j)
    let check = 0
    for (let idx = 0; idx < 4;idx++){
        if (board[i][j][idx] === 0){
            const [a, b] = [i + dict[idx][0], j+ dict[idx][1]]
            if (0 <= a && a < m && 0 <= b && b < n){
                const next_room = find_room(a,b)
                if (now_room !== next_room){
                    check = Math.max(check, rooms.get(now_room).size + rooms.get(next_room).size)
                }
            }
        }
    }
    return check
}

let union = 0
for (let i = 0; i < m;i++){
    for (let j = 0;j < n;j++){
        union = Math.max(union, check(i,j))
    }
}
console.log(`${num}\n${maxr}\n${union}`)

// import sys
// from collections import deque
// input = sys.stdin.readline

// n,m = map(int,input().split())

// dic = {0: [1,1,1,1],1: [0,1,1,1], 2: [1,1,0,1], 4: [1,0,1,1], 8: [1,1,1,0], 14: [1,0,0,0],
//        3: [0,1,0,1], 5: [0,0,1,1], 9: [0,1,1,0], 7: [0,0,0,1], 12: [1,0,1,0],
//        11: [0,1,0,0], 13: [0,0,1,0], 10: [1,1,0,0], 6: [1,0,0,1], 15: [0,0,0,0]}
// dict = [[0,-1],[0,1],[-1,0],[1,0]]

// board = [[dic[i] for i in list(map(int, input().split()))] for _ in range(m)]
// visit = [[True] * n for _ in range(m)]

// def find(x,y):
//     q = deque([[x,y]])
//     rooms = set()
//     visit[x][y] = False

//     while q:
//         i,j = q.popleft()
//         rooms.add((i,j))

//         for idx in range(4):
//             if board[i][j][idx] != 0:
//                 a, b = i + dict[idx][0], j + dict[idx][1]
//                 if 0 <= a < m and 0 <= b < n and visit[a][b]:
//                     q.append([a,b])
//                     visit[a][b] = False
//     return rooms

// rooms = {}
// num, maxr = 0, 0
// for i in range(m):
//     for j in range(n):
//         if visit[i][j]:
//             num += 1
//             room = find(i,j)
//             maxr = max(maxr, len(room))
//             rooms[num] = room

// def find_room(x,y):
//     for k,v in rooms.items():
//         if (x,y) in v:
//             return k

// def check(i,j):
//     now_room = find_room(i,j)
//     check = 0
//     for idx in range(4):
//         if board[i][j][idx] == 0:
//             a, b = i + dict[idx][0], j + dict[idx][1]
//             if 0 <= a < m and 0 <= b < n:
//                 next_room = find_room(a,b)
//                 if now_room != next_room:
//                     check = max(check, len(rooms[now_room]) + len(rooms[next_room]))
//     return check
            
// union = 0
// for i in range(m):
//     for j in range(n):
//         union = max(union, check(i,j))
// print(num, maxr, union, sep='\n')
