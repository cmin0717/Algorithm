function solution(distance, rocks, n) {
    rocks = [0, ...rocks, distance]
    rocks.sort((a, b) => a - b)
    
    let [start, end] = [0, distance]
    
    while(start <= end){
        // 이분 탐색으로 바위간의 거리를 기준으로 잡는다.
        let mid = Math.floor((start+end)/2)
        
        // 해당 거리보다 이하인 돌들은 삭제
        let del_rock = new Set()
        for (let i = 0; i < rocks.length-1; i++){
            if (del_rock.has(i)) continue
            for (let j = i+1; j < rocks.length; j++){
                if ((rocks[j] - rocks[i]) >= mid){
                    break
                }else{
                    del_rock.add(j)
                }
            }
        }
        
        // 삭제한 돌이 n개 기준으로 값을 재정의하고 다시 탐색 
        if (del_rock.size <= n){
            start = mid + 1
        }else{
            end = mid - 1
        }
    }
    return end
}