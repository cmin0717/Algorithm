function solution(s){   
    
    // 시작점을 주어주면 팰린드롬를 찾는 함수
    const find = (left, right, n) => {
        let result = 1
        while (0 <= left && right < n){
            if (s[left] !== s[right]) break
            result = Math.max(result, right-left+1)
            left -= 1
            right += 1
        }
        return result
    }
    
    let n = s.length
    let result = 1
    for (let i = 0; i < n-1; i++){
        // 홀수 팰린드롬
        result = Math.max(result, find(i-1, i+1, n))
        // 짝수 팰린드롬
        if (s[i] === s[i+1]){
            result = Math.max(result, find(i-1, i+2, n))
        }
    }
    return result
}