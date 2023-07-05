const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const [n, m] = input[0].split(' ').map(Number)
const rooms = [[]]
const people = Array.from(Array(n), (v,i) => input[i+1].split(' '))

const check = (lv) => {
    for (let i=1;i<rooms.length;i++){
        const [min, max] = rooms[i][0]
        if (min <= lv && lv <= max && rooms[i].length <= m){
            return i
        }
    }
    return false
}

while (people.length !== 0){
    let [lv, name] = people.shift()
    lv = Number(lv)

    let room = check(lv)
    if (!room){
        rooms.push([[lv-10, lv+10], [lv,name]])
        continue
    }

    rooms[room].push([lv, name])
}

rooms.splice(1).forEach((room) => {
    if (room.length === m+1){
        console.log('Started!')
    }else{
        console.log('Waiting!')
    }
    room.splice(1).sort((a,b) => a[1] > b[1] ? 1 : -1).forEach((member) => {
        console.log(member[0], member[1])
    })
})