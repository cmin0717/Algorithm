// import sys
// input = sys.stdin.readline

// n, m = map(int,input().split())
// count = int(input())
// boxs = [list(map(int, input().split())) for _ in range(count)]
// boxs.sort(key=lambda x: x[1])

// truck = [m] * (n+1)
// total = 0

// for s,e,w in boxs:
//     check = m+1
//     for i in range(s,e):
//         num = truck[i] if truck[i]-w < 0 else w
//         check = min(check, num)
//     for i in range(s,e):
//         truck[i] -= check
//     total += check

// print(total)

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const count = Number(input[1])
const boxs = Array.from(Array(count), (v,i) => input[i+2].split(' ').map(Number))
boxs.sort((a,b) => a[1] - b[1] || a[0] - b[0])

const truck = new Array(n+1).fill(m)
let total = 0

boxs.forEach((box) => {
    const [s, e, w] = box
    let check = m+1
    for (let i=s;i<e;i++){
        const num = truck[i] - w >= 0 ? w : truck[i]
        check = Math.min(check, num)
    }
    for (let i=s;i<e;i++){
        truck[i] -= check
    }
    total += check
})
console.log(total)