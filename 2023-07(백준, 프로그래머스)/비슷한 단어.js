const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const n = Number(input[0])

const words = new Map()
const arr = []
let front = ['', []]

for (let i =1; i<= n;i++){
    const word = input[i]
    arr.push(word)

    let check = ''
    word.split('').forEach((w) => {
        check += w
        if (words.has(check)){
            if (front[0].length < check.length){
                front = [check, words.get(check)[0]]
            }else if (front[0].length == check.length && words.get(check)[0] < front[1]){
                front = [check, words.get(check)[0]]
            }
            words.set(check, [...words.get(check), i])
        }else{
            words.set(check, [i])
        }
    })
}

words.get(front[0]).splice(0,2).forEach((v) => {
    console.log(arr[v-1])
})

// import sys
// input = sys.stdin.readline

// n = int(input())
// words, arr, front = {}, [], ['', float('inf')]

// for i in range(n):
//     word = input().rstrip()
//     arr.append(word)

//     check = ''
//     for w in word:
//         check += w
//         if check in words:
//             f_l, c_l, word_i = len(front[0]), len(check), words[check][1][0]
//             if (f_l < c_l) or (f_l == c_l and word_i < front[1]):
//                 front = [check, word_i]
//             words[check][1].append(i)
//         else:
//             words[check] = [check, [i]]

// for i in words[front[0]][1][:2]:
//     print(arr[i])