// import sys
// input = sys.stdin.readline

// def dfs(idx, money):
//     global check
//     tp, cost, links = rooms[idx]
    
//     if check:
//         return

//     if tp == 'E' or tp == 'L':
//         money = money if tp == 'E' else max(cost, money)
//     else:
//         if money >= cost:
//             money -= cost
//         else:
//             return
        
//     if idx == n:
//         check = True
//         return

//     visit[idx] = max(visit[idx], money)
//     for room in links:
//         if money > visit[room]:
//             dfs(room, money)

// while True:
//     n = int(input())
//     if n == 0:break

//     rooms = [[]]
//     for i in range(1,n+1):
//         tp, cost, *link = list(input().split())
//         cost = int(cost)
//         link.pop()
//         link = list(map(int, link))
//         rooms.append([tp, cost, link])
    
//     visit = [-1] * (n+1)
//     check = False
//     dfs(1, 0)
//     if check:
//         print('Yes')
//     else:
//         print('No')

const path = process.platform === 'win32' ? 'input.txt' : 'dev/stdin'
const splitType = process.platform === 'win32' ? '\r\n' : '\n'
const input = require('fs').readFileSync(path).toString().trim().split(splitType)

const dfs = async (idx, money) => {
    if (check) return
    const [tp, cost, link] = rooms[idx]

    if (tp === 'E' || tp === 'L'){
        money = tp === 'E' ? money : Math.max(money, cost)
    }else{
        if (money >= cost){
            money -= cost
        }else{
            return
        }
    }

    if (idx === n){
        check = true
        return
    }

    visit[idx] = Math.max(visit[idx], money)
    for (let i of link){
        if (money > visit[i]){
            dfs(i, money)
        }
    }
}

let [check, rooms, visit, n] = [false, [], [], 0]
while (true){
    n = Number(input.shift())
    if (n === 0) break

    rooms = [[]]
    for (let i=0;i<n;i++){
        let [tp, cost, ...link] = input.shift().split(' ')
        cost = Number(cost)
        link = link.map(Number)
        rooms.push([tp, cost, link])
    }

    visit = new Array(n+1).fill(-1)
    dfs(1,0)
    console.log(check ? 'Yes' : 'No')
    check = false
}