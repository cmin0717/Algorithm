const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

input.forEach((i) => {
    const [n, x, y] = i.split(' ').map(Number)
    let arr = []
    
    if (x+y-1 > n){
        console.log(-1)
    }else{
        const rest = Array(n-x-y+1).fill(1)
        if (x === 1){
            arr = [y, ...rest, ...Array.from(Array(y-1), (v,i) => i+1).reverse()]
        }else if (x <= y){
            arr = [...rest,...Array.from(Array(x-1), (v,i) => i+1), ...Array.from(Array(y), (v,i) => i+1).reverse()]
        }else{
            arr = [...rest,...Array.from(Array(x), (v,i) => i+1), ...Array.from(Array(y-1), (v,i) => i+1).reverse()]
        }
        console.log(...arr)
    } 
})