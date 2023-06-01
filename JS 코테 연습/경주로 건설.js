function solution(board) {
    const n = board.length
    let visit = [...Array(2).keys()].map(_ => [...Array(n).keys()].map(_ => [...Array(n).keys()].map(i => Infinity)))
    let q = [[0,0,0,0], [0,0,0,1]]
    
    while( q.length !== 0){
        let [x,y,cnt,d] = q.shift()
        
        if (x === n-1 && y === n-1){
            visit[d][x][y] = Math.min(visit[d][x][y], cnt)
            continue
        }
        
        for (let [z,i,j] of [[1,x+1,y],[1,x-1,y],[0,x,y+1],[0,x,y-1]]){
            if (0 <= i && i < n && 0 <= j && j < n && board[i][j] !== 1){
                if (z === d){
                    if (visit[z][i][j] > cnt+100){
                        visit[z][i][j] = cnt+100
                        q.push([i, j, cnt+100, z])
                    }
                }else{
                    if (visit[z][i][j] > cnt+600){
                        visit[z][i][j] = cnt+600
                        q.push([i, j, cnt+600, z])
                    }
                }
            }
        }
    }
    return Math.min(visit[0][n-1][n-1], visit[1][n-1][n-1])
}
solution(	[[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
