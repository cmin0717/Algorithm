const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])
const bolls = input[1].split('')

const find = (s,e,d) => {
    let standard = bolls[s]
    let [rb, check] = [{'R':0, 'B':0}, e]

    for (s; s != e; s += d){
        if (check && bolls[s] === standard){
            continue
        }
        if (check && bolls[s] !== standard){
            check = s
            break
        }
    }

    for (let i=check;i != e;i += d){
        rb[bolls[i]] += 1
    }
    return Math.min(rb.B, rb.R)
}
console.log(Math.min(find(n-1, -1, -1), find(0,n,1)))


// import sys
// input = sys.stdin.readline

// n = int(input())
// bolls = list(input().rstrip())

// def find(s,e,d):
//     rb, check, standard = {'R':0,'B':0}, e, bolls[s]
//     for i in range(s,e,d):
//         if check and bolls[i] == standard:
//             continue
//         if bolls[i] != standard:
//             check = i
//             break

//     for i in range(check,e,d):
//         rb[bolls[i]] += 1
//     return min(rb.values())

// print(min(find(n-1,-1,-1), find(0,n,1)))