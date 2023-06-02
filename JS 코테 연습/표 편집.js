function solution(n, k, cmd) {
    let cursor = k
    let link = [...Array(n).keys()].map(i => [i-1, i+1])
    let del_list = []
    
    for (let c of cmd){
        c = c.split(' ')
        switch (c[0]){
            case 'U':
                for (let i =0; i < c[1]; i++){
                    cursor = link[cursor][0]
                }
                break
            case 'D':
                for (let i =0; i < c[1]; i++){
                    cursor = link[cursor][1]
                }
                break
            case 'C':
                let t = link[cursor]
                del_list.push([cursor, t])
                if (t[0] !== -1) {
                    link[t[0]][1] = t[1]
                }
                if (t[1] !== n) {
                    link[t[1]][0] = t[0]
                }
                cursor = t[1] === n ? t[0] : t[1]
                break
            case 'Z':
                let [cur, lr] = del_list.pop()
                if (lr[0] !== -1) {
                    link[lr[0]][1] = cur
                }
                if (lr[1] !== n) {
                    link[lr[1]][0] = cur
                }
                break
        }
    }

    let result = [...Array(n).keys()].map(_ => 'O')
    for (let i of del_list){
        result[i[0]] = 'X'
    }
    return result.join('')
}