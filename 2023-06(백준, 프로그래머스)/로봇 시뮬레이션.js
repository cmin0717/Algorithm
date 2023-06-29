const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [m, n] = input[0].split(' ').map(Number)
const [a, b] = input[1].split(' ').map(Number)
const board = Array.from(Array(n+1), () => Array(m+1).fill(0))
const robots = new Map()

input.splice(2,a).forEach((robot, i) => {
    let [y, x, d] = robot.split(' ')
    x = n-Number(x)+1
    y = Number(y)
    robots.set(i+1, [x,y,d])
    board[x][y] = i+1
})

const dict = {'N': [-1, 0], 'W': [0, -1], 'S': [1,0], 'E': [0,1]}
const [L, R] = [['N', 'W', 'S', 'E'], ['N', 'E', 'S', 'W']]

const try_L = (r, t) => {
    let [x,y,d] = robots.get(r)
    let new_d = (L.indexOf(d) + t) % 4
    robots.set(r, [x,y, L[new_d]])
}
const try_R = (r, t) => {
    let [x,y,d] = robots.get(r)
    let new_d = (R.indexOf(d) + t) % 4
    robots.set(r, [x,y, R[new_d]])
}
const try_F = (r, t) => {
    let [x,y,d] = robots.get(r)
    board[x][y] = 0
    let [dx, dy] = dict[d]

    for (let i=0;i<t;i++){
        x += dx
        y += dy
        if (x === 0 || x > n || y === 0 || y > m){
            return `Robot ${r} crashes into the wall`
        }
        if (board[x][y] !== 0){
            return `Robot ${r} crashes into robot ${board[x][y]}`
        }
    }
    board[x][y] = r
    robots.set(r, [x,y,d])
    return ''
}

let result = 'OK'
for (let i = 2; i < input.length; i++){
    let [robot, co, t] = input[i].split(' ')
    robot = Number(robot)
    t = Number(t)

    if (co === 'L'){
        try_L(robot, t)
    }
    else if (co === 'R'){
        try_R(robot, t)
    }else{
        let check = try_F(robot, t)
        if (check.length !== 0){
            result = check
            break
        }
    }
}
console.log(result)

// import sys
// input = sys.stdin.readline

// m, n = map(int, input().split())
// a, b = map(int, input().split())
// board = [[0] * (m+1) for _ in range(n+1)]
// robots = {}

// for i in range(a):
//     y,x,d = input().split()
//     x,y = n-int(x)+1, int(y)
//     robots[i+1] = [x,y,d]
//     board[x][y] = i+1

// dict = {'N': [-1, 0], 'W': [0, -1], 'S': [1,0], 'E': [0,1]}
// L = ['N', 'W', 'S', 'E']
// R = ['N', 'E', 'S', 'W']

// def try_L(r, t):
//     d = robots[r][2]
//     new_d = (L.index(d) + t) % 4
//     robots[r][2] = L[new_d]

// def try_R(r, t):
//     d = robots[r][2]
//     new_d = (R.index(d) + t) % 4
//     robots[r][2] = R[new_d]

// def try_F(r, t):
//     x,y,d = robots[r]
//     board[x][y] = 0
//     dx,dy = dict[d]
//     for _ in range(t):
//         x += dx
//         y += dy
//         if 0 == x or x > n or 0 == y or y > m:
//             return f'Robot {r} crashes into the wall'
//         if board[x][y] != 0:
//             return f'Robot {r} crashes into robot {board[x][y]}'
//     board[x][y] = r
//     robots[r] = [x,y,d]
//     return ''

// commends = [input().split() for _ in range(b)]
// for commend in commends:
//     robot, co, t = commend
//     robot, t = int(robot), int(t)
//     if co == 'L':
//         try_L(robot, t)
//     elif co == 'R':
//         try_R(robot, t)
//     else:
//         check = try_F(robot, t)
//         if len(check) != 0:
//             print(check)
//             break
// else:
//     print('OK')