// import sys
// input = sys.stdin.readline

// n = int(input())
// members = list(map(int, input().split()))
// link = [[] for _ in range(n)]
// time = [0] * n

// for i in range(1, len(members)):
//     link[members[i]].append(i)

// def dfs(idx):
//     arr = []

//     if not link[idx]:
//         arr.append(0)
//     else:
//         for i in link[idx]:
//             dfs(i)
//             arr.append(time[i])
    
//     arr.sort(reverse=True)
//     arr = [arr[i]+i+1 for i in range(len(arr))]
//     time[idx] = max(arr)

// dfs(0)
// print(time[0]-1)

const input = require('fs').readFileSync('input.txt').toString().trim().split('\r\n')
const n = Number(input[0])
const members = input[1].split(' ').map(Number)
const link = Array.from(Array(n), () => [])
const time = Array(n).fill(0)

for (let i = 1;i<n;i++){
    link[members[i]].push(i)
}

const dfs = (idx) => {
    let arr = []

    if (link[idx].length === 0){
        arr.push(0)
    }else{
        for (let i of link[idx]){
            dfs(i)
            arr.push(time[i])
        }
    }

    arr.sort((a,b) => b - a)
    arr = Array.from(Array(arr.length), (v, i) => arr[i]+i+1)
    time[idx] = Math.max(...arr)
}

dfs(0)
console.log(time[0]-1)