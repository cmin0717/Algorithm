// import sys
// input = sys.stdin.readline

// n = int(input())
// now = list(map(int, list(input().rstrip())))
// next = list(map(int, list(input().rstrip())))

// def switch(arr):
//     t = 0
//     for i in range(1,n):
//         if arr[i-1] != next[i-1]:
//             t += 1
//             for j in range(i-1, i+2):
//                 if j < n:
//                     arr[j] = (arr[j]+1) % 2
//     return t if arr == next else float('inf')

// first = switch(now[:])
// now[0] = (now[0]+1) % 2
// now[1] = (now[1]+1) % 2
// second = switch(now[:]) + 1

// result = min(first, second)
// if result != float('inf'):
//     print(result)
// else:
//     print(-1)

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
let now = input[1].split('').map(Number)
const next = input[2].split('').map(Number)

const button = (arr) => {
    let t = 0
    for (let i = 1; i < n; i++){
        if (arr[i-1] !== next[i-1]){
            t++
            for (let j = i-1;j < i+2; j++){
                if (j < n){
                    arr[j] = (arr[j] + 1) % 2
                }
            }
        }
    }
    return `${arr}` === `${next}` ? t : Infinity
}

const first = button([...now])
now[0] = (now[0] + 1) % 2
now[1] = (now[1] + 1) % 2
const second = button([...now]) + 1

if (Math.min(first, second) !== Infinity){
    console.log(Math.min(first, second))
}else{
    console.log(-1)
}