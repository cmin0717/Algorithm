// import sys
// from collections import deque
// input = sys.stdin.readline

// n = int(input())
// m = int(input())

// link = [[] for _ in range(n+1)]
// link2 = [[] for _ in range(n+1)]

// for _ in range(m):
//     s,e = map(int,input().split())
//     link[s].append(e)
//     link2[e].append(s)

// def check(idx):
//     count, q, visit = 0, deque([[idx, True], [idx, False]]), set()

//     while q:
//         i, d = q.popleft()

//         arr = link if d  else link2

//         for num in arr[i]:
//             if num not in visit:
//                 count += 1
//                 q.append([num,d])
//                 visit.add(num)
//     return count

// for i in range(1,n+1):
//     print(n - check(i) -1)

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = [input[0], input[1]].map(Number)
const link = Array.from(Array(n+1), () => [])
const link2 = Array.from(Array(n+1), () => [])

for (let i=2; i<m+2; i++){
    const [s,e] = input[i].split(' ').map(Number)
    link[s].push(e)
    link2[e].push(s)
}

const check = (idx) => {
    let [count, q, visit] = [0, [[idx, true], [idx, false]], new Set()]

    while (q.length !== 0){
        const [i, d] = q.shift()

        let arr = d ? link : link2

        for (let num of arr[i]){
            if (!visit.has(num)){
                visit.add(num)
                q.push([num, d])
                count++
            }
        }
    }
    return count
}

for (let i=1; i<= n;i++){
    console.log(n-check(i)-1)
}