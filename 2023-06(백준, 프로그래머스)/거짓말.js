// import sys
// from collections import deque
// input = sys.stdin.readline

// n,m = map(int, input().split())
// truth = list(map(int, input().split()))[1:]
// party = [list(map(int, input().split()))[1:] for _ in range(m)]
// visit = [True] * (n+1)
// link = [[] for _ in range(n+1)]

// for i in truth:
//     visit[i] = False

// for p in party:
//     if len(p) == 1:
//         continue

//     for i in range(len(p)):
//         for j in range(i+1, len(p)):
//             x,y = p[i],p[j]
//             link[x].append(y)
//             link[y].append(x)

// q = deque(truth)
// while q:
//     idx = q.popleft()

//     for i in link[idx]:
//         if visit[i]:
//             visit[i] = False
//             q.append(i)

// result = 0
// for p in party:
//     for i in p:
//         if not visit[i]:
//             break
//     else:
//         result += 1
// print(result)

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n,m] = input[0].split(' ').map(Number)
const truth = input[1].split(' ').splice(1).map(Number)
const party = []
input.splice(2).forEach((p) => {
    party.push(p.split(' ').splice(1).map(Number))
})

const link = Array.from(Array(n+1), () => [])

party.forEach((p) => {
    for (let i =0;i<p.length; i++){
        for (let j = i+1; j < p.length; j++){
            const [x,y] = [p[i], p[j]]
            link[x].push(y)
            link[y].push(x)
        }
    }
})

const visit = new Array(n+1).fill(true)
truth.forEach((v) => {
    visit[v] = false
})

while (truth.length !== 0){
    idx = truth.shift()

    for (let i of link[idx]){
        if (visit[i]){
            visit[i] = false
            truth.push(i)
        }
    }
}

let result = 0
party.forEach((p) => {
    let check = true
    for (let i of p){
        if (!visit[i]){
            check = false
            break
        }
    }
    if (check) result++
})
console.log(result)
