const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const build = Array.from(Array(n+1), () => [Infinity, Infinity])
const height = [0, ...input[1].split(' ').map(Number)]

let check = []
for (let i=1;i<=n;i++){
    if (check.length === 0){
        check.push([i, height[i]])
        continue
    }

    while (check.length !== 0){
        if (check[check.length-1][1] > height[i]){
            build[i][0] = check[check.length-1][0]
            break
        }else if (check[check.length-1][1] <= height[i]) {
            const [idx, h] = check.pop()
            build[idx][1] = i
        }
    }
    check.push([i, height[i]])
}

const left = new Array(n+1).fill(0)
const right = new Array(n+1).fill(0)

for (let i=1;i<=n;i++){
    const [b_i_0, b_n_i_1] = [build[i][0], build[n+1-i][1]]
    if (b_i_0 !== Infinity){
        left[i] = left[b_i_0] + 1
    }
    if (b_n_i_1 !== Infinity ){
        if (height[n+1-i] !== height[b_n_i_1]){
            right[n+1-i] = right[b_n_i_1] + 1
        }else{
            right[n+1-i] = right[b_n_i_1]
            build[n+1-i][1] = build[b_n_i_1][1]
        }
    }
    
}

for (let i=1;i<=n;i++){
    if (left[i]+right[i] !== 0){
        const [x,y] = build[i]
        const num = Math.abs(x-i) <= Math.abs(y-i) ? x : y
        console.log(left[i]+right[i], num)
    }else{
        console.log(0)
    }
}