const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input.shift().split(' ').map(Number)
const train = Array.from(Array(n+1), () => Array(21).fill(false))

for (let i=0;i<m;i++){
    const [cmd, t, s] = input[i].split(' ').map(Number)

    if (cmd === 1){
        train[t][s] = true
    }else if (cmd === 2){
        train[t][s] = false
    }else if (cmd === 3){
        let temp = false
        for (let j=1;j<=20;j++){
            [train[t][j], temp] = [temp, train[t][j]]
        }
    }else{
        let temp = false
        for (let j=20;j>=1;j--){
            [train[t][j], temp] = [temp, train[t][j]]
        }
    }
}

let result = new Set()
for (let i=1;i<n+1;i++){
    const check = []
    for (let j=1;j<21;j++){
        if (train[i][j]) check.push(j)
    }
    if (check.length !== 0){
        result.add(check.join('-'))
    }else{
        result.add('nobody')
    }
}
console.log(result.size)