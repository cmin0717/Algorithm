// import sys
// input = sys.stdin.readline

// n,m,h = map(int,input().split())
// students = [list(map(int, input().split())) for _ in range(n)]

// dp = [0] * (h+1)
// dp[0] = 1
// for student in students:
//     check = {}
//     for s in student:
//         for i in range(h):
//             if dp[i] != 0 and i+s <= h:
//                 check.setdefault(i+s, 0)
//                 check[i+s] += dp[i]
//             if i+s > h:
//                 break
//     for k,v in check.items():
//         dp[k] += v

// print(dp[h] % 10007)

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n,m,h] = input[0].split(' ').map(Number)
const students = Array.from(Array(n), (v,i) => input[i+1].split(' ').map(Number))
const dp = new Array(h+1).fill(0)
dp[0] = 1

students.forEach((student) => {
    const check = new Map()
    student.forEach((s) => {
        for (let i =0;i <h; i++){
            if (dp[i] !== 0 && i+s <= h){
                if (check.has(i+s)){
                    check.set(i+s, check.get(i+s) + dp[i])
                }else{
                    check.set(i+s, dp[i])
                }
            }
            if (i+s > h) break
        }
    })
    for (const [k,v] of check.entries()){
        dp[k] = (dp[k]+v) % 10007
    }
})

console.log(dp[h])