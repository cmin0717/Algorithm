function solution(n, cores) {
    if (cores.length >= n){
        return cores[n-1]
    }else{
        n -= cores.length
    }
    
    // 이분 탐색으로 몇시간을 작업하는지 구한다.
    let [start, end] = [0, n*Math.max(...cores)]
    
    while (start <= end){
        let mid = Math.floor((start+end)/2)
        
        let time = 0
        for (let core of cores){
            time += Math.floor(mid/core)
        }
        
        if (time < n){
            start = mid + 1
        }else{
            end = mid - 1
        }
    }
    
    // 작업해야할 시간-1 시간 만큼 작업한 작업량을 구한다.
    for (let core of cores){
        n -= Math.floor((start-1)/core)
    }
    // 마지막 시간에 작업할수있는 cpu를 구하고 작업량이 0이되는 cpu를 리턴
    for (let i = 0; i < cores.length; i++){
        if (start % cores[i] === 0){
            n--
            if (n === 0){
                return i+1
            }
        }
    }
}