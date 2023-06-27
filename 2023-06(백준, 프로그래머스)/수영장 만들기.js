const input = require('fs').readFileSync('input.txt').toString().split('\n').map(i => i.trim())

const [n,m] = input[0].split(' ').map(Number)
let pool = Array.from(Array(n), (v,i) => input[i+1].split('').map(Number))
let result = 0

const check_pool = (x, y) => {
    let visit = Array.from(Array(n), () => Array(m).fill(true))
    visit[x][y] = false
    let [store, h, q] = [[], 10, [[x,y]]]

    while (q.length !== 0) {
        const [i,j] = q.shift()
        store.push([i,j])

        const arr = [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]
        for (let [a,b] of arr){
            if (0 <= a && a < n && 0 <= b && b < m){
                if (visit[a][b] && pool[x][y] >= pool[a][b]){
                    visit[a][b] = false
                    q.push([a,b])
                }
                if (pool[a][b] > pool[x][y]){
                    h = Math.min(h, pool[a][b])
                }
            }else{
                return [false, [], 0]
            }
        }
    }
    return [true, store, h]
}

const fill_pool = (arr, h) => {
    let cost = 0

    for (let [i,j] of arr){
        cost += h - pool[i][j]
        pool[i][j] = h
    }
    return cost
}

for (let i =0; i<n;i++){
    for (let j=0; j<m;j++){
        const [temp, arr, h] = check_pool(i,j)
        if (temp){
            result += fill_pool(arr, h)
        }
    }
}
console.log(result)



// import sys
// from collections import deque
// input = sys.stdin.readline

// n,m = map(int, input().split())
// pool = [list(map(int, input().rstrip())) for _ in range(n)]
// result = 0

// def check_pool(x,y):
//     visit = [[True] * m for _ in range(n)]
//     visit[x][y] = False
//     store, h = [], 10
//     q = deque([[x,y]])

//     while q:
//         i,j = q.popleft()
//         store.append([i,j])

//         for a,b in [i+1,j],[i-1,j],[i,j+1],[i,j-1]:
//             if 0 <= a < n and 0 <= b < m:
//                 if visit[a][b] and pool[x][y] >= pool[a][b]:
//                     visit[a][b] = False
//                     q.append([a,b])
//                 if pool[a][b] > pool[x][y]:
//                     h = min(h, pool[a][b])
//             else:
//                 return False, [], 0
    
//     return True, store, h

// def fill_pool(arr, h):
//     global result

//     for x,y in arr:
//         result += h - pool[x][y]
//         pool[x][y] = h

// def find_pool():
//     for i in range(n):
//         for j in range(m):
//             temp, fill, h = check_pool(i,j)
//             if temp:
//                 fill_pool(fill, h)

// find_pool()
// print(result)
