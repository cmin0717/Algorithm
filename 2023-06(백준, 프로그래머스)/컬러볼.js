// import sys
// from collections import deque
// input = sys.stdin.readline

// n = int(input())
// correction = [deque([0]) for _ in range(n+1)]
// balls = [list(map(int, input().split())) for _ in range(n)]
// sort_ball = sorted(balls, key= lambda x: x[1])


// for c,s in sort_ball:
//     correction[c].append(correction[c][-1]+s)

// result = {}
// q, now, check, c_c = deque(sort_ball), 0, 0, 0
// while q:
//     c,s = q.popleft()
//     if s == check:
//         if result.get((c,s)) != None:
//             correction[c].popleft()
//         else:
//             result[(c,s)] = now-correction[c].popleft() - (check*c_c)
//         c_c += 1
//     else:
//         result[(c,s)] = now-correction[c].popleft()
//         check = s
//         c_c = 1
//     now += s

// for c,s in balls:
//     print(result[(c,s)])

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const balls = []
for (let i=0;i < n;i++){
    balls.push([...input[i+1].split(' ').map(Number), i])

}
balls.sort((a,b) => a[1] - b[1] || a[0] - b[0])

const color = new Array(n+1).fill(0)
const num = new Array(n).fill(0)
color[balls[0][0]] = balls[0][1]

let [now, check, c_c] = [balls[0][1], balls[0][1], 1];
for (let i=1;i<n;i++){
    let[c, s, idx] = balls[i]
    let[pc,ps,pi] = balls[i-1]
    
    if (c === pc && s === ps){
        num[idx] = num[pi]
        c_c++
    }else if (s === ps){
        num[idx] = now - color[c] - (check*c_c)
        c_c++
    }else{
        num[idx] = now - color[c]
        check = s
        c_c = 1
    }
    color[c] += s
    now += s
}

for (let i=0;i<n;i++){
    console.log(num[i])
}