const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const link = Array.from(Array(n+1), () => [])
let visit, count

for (let i=1;i<=m;i++){
    const [a, b] = input[i].split(' ').map(Number)
    link[b].push(a)
}

function dfs(idx){
    count++
    for (let i=0;i<link[idx].length;i++){
        let num = link[idx][i]
        if (!visit[num]){
            visit[num] = true
            dfs(num)
        }
    }
    return
}

let max = 0, result = []
for (let i=1;i<=n;i++){
    visit = Array(n+1).fill(false)
    visit[i] = true
    count = 0
    dfs(i)
    
    if (max < count){
        max = count
        result = [i]
    }else if (max === count){
        result.push(i)
    }
}

console.log(result.join(' '))

// import sys
// from collections import deque
// input = sys.stdin.readline

// n,m = map(int,input().split())

// link = [[] for _ in range(n+1)]

// for _ in range(m):
//     s,e = map(int,input().split())
//     link[e].append(s)

// def bfs(idx):
//     q = deque([idx])
//     visit, cnt = [False] * (n+1), 0
//     visit[idx] = True
    
//     while q:
//         i = q.popleft()
//         cnt += 1

//         for num in link[i]:
//             if not visit[num]:
//                 visit[num] = True
//                 q.append(num)
//     return cnt

// count, max_num = [0] *(n+1), 0
// for i in range(1,n+1):
//     count[i] = bfs(i)
//     max_num = max(max_num, count[i])

// print(*[i for i in range(1,n+1) if count[i] == max_num])