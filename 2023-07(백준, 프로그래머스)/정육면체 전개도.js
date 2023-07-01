// import sys
// input = sys.stdin.readline

// arr = []
// check = []

// for i in range(18):
//     line = list(map(int, input().split()))
//     for j in range(6):
//         if line[j] != 0:
//             check.append(((i % 6)+1, j+1))

//     if (i+1) % 6 == 0:
//         arr.append(check)
//         check = []

// def find(x,y,arr):
//     max_x, min_x = max(x.keys()), min(x.keys())
//     max_y, min_y = max(y.keys()), min(y.keys())
    
//     test = [[min_x+1, min_y+1],[max_x-1,min_y+1]] if len(x) > len(y) else [[min_x+1,max_y-1], [min_x+1,min_y+1]]
//     for i,j in test:
//         if (i,j) not in arr:
//             return 'no'
//     return 'yes'

// def find2(x,y):
//     arr = list(x.values()) + list(y.values())
//     for v in arr:
//         if v > 4:
//             return 'no'
//     return 'yes'

// for s in range(3):
//     x, y = {}, {}
//     for i,j in arr[s]:
//         x.setdefault(i, 0)
//         y.setdefault(j, 0)
//         x[i] += 1
//         y[j] += 1

//     mx, my = len(x), len(y)
//     if (mx == 3 and my == 4) or (mx == 4 and my == 3):
//         print(find(x,y, arr[s]))
//     elif (mx == 2 and my == 5) or (mx == 5 and my == 2):
//         print(find2(x,y))
//     else:
//         print('no')

// # 정육면체를 만들기 위해서는 4, 3 형태로 주어지거나 5, 2형태중에 한가지 케이스만 가능하다.
// # 4,3 형태일때에도 4*3 직사각형의 가운데 2곳을 모두 채우고 있어야지만 정육면체를 만들수있다.

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

let [arr, check] = [[], []]

input.forEach((lines, i) => {
    lines.split(' ').map(Number).forEach((line, j) => {
        if (line !== 0){
            check.push([(i%6)+1,j+1])
        }
    })
    if ((i+1) % 6 === 0){
        arr.push(check)
        check = []
    }
})

const find = (x,y,arr) => {
    const [ax, ix] = [Math.max(...x.keys()), Math.min(...x.keys())]
    const [ay, iy] = [Math.max(...y.keys()), Math.min(...y.keys())]

    let check = x.size > y.size ? [[ax-1, ay-1],[ix+1, ay-1]] : [[ax-1,ay-1],[ax-1,iy+1]]
    let temp = 0
    for (let [i,j] of check){
        for (let [a,b] of arr){
            if (i === a && j === b){
                temp += 1
            }
        }
    }
    return temp === 2 ? 'yes' : 'no'
}

const find2 = (x,y) => {
    const check = [...x.values(), ...y.values()]
    for (let num of check){
        if (num > 4){
            return 'no'
        }
    }
    return 'yes'
}

for (let s=0; s<3; s++){
    const [x,y] = [new Map(), new Map()]
    for (let [i,j] of arr[s]){
        x.set(i, x.has(i) ? x.get(i)+1 : 1)
        y.set(j, y.has(j) ? y.get(j)+1 : 1)
    }
    const [cx, cy] = [x.size, y.size]
    if ((cx === 4 && cy === 3) || (cx === 3 && cy === 4)){
        console.log(find(x,y,arr[s]))
    }else if ((cx === 2 && cy === 5) || (cx === 5 && cy === 2)){
        console.log(find2(x,y))
    }else{
        console.log('no')
    }
}