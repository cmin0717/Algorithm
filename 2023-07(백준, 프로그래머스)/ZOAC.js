const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const origin = input[0].split('')
const n = origin.length
const result = Array(n).fill('')

const dfs = (start, arr) => {
    if (arr.length === 0) return

    const ws = [...arr].sort()
    const idx = arr.indexOf(ws[0])
    result[start+idx] = ws[0]

    console.log(result.join(''))
    dfs(start+idx+1, arr.splice(idx+1))
    dfs(start, arr.splice(0,idx))
}
dfs(0, origin)
