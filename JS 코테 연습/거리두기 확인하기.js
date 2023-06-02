function solution(places) {
    
    function check (board, q) {
        let temp = true
        
        while (q.length !== 0){
            let [x, y, cnt, visit] = q.shift()
            
            if (cnt === 3) continue
            
            if (cnt > 0 && board[x][y] === 'P'){
                temp = false
                break
            }
            
            for (let [i,j] of [[x+1,y], [x-1,y], [x,y+1], [x,y-1]]){
                let new_p = `${i}-${j}`
                if (0 <= i && i < 5 && 0 <= j && j < 5 && board[i][j] !== 'X' && !visit.includes(new_p)){
                    // 리스트에 추가시 ...를 사용하자
                    q.push([i,j,cnt+1, [new_p, ...visit]])
                }
            }
        }
        return temp
    }
    
    
    let result = []
    for (let place of places){
        let board = [...Array(5).keys()].map(_ => [...Array(5).keys()].map(l => 0))
        let position = []
        for (let i =0 ; i < 5; i++){
            for (let j=0; j < 5; j++){
                board[i][j] = place[i][j]
                if (place[i][j] === 'P'){
                    position.push([i, j, 0, [`${i}-${j}`]])
                }
            }
        }
        result.push(check(board, position) ? 1 : 0)
    }
    
    return result
}
solution(	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])