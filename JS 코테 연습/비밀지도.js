function solution(n, arr1, arr2) {
    const result = []
    
    for (let i = 0; i < n; i++){
        // toString를 이용하여 2진수로 변환시킨다.
        // parseInt(<변수명>, <해당진수>) : 변수와 변수에 해당하는 진수를 10진수로 변환시켜준다.
        let b = (arr1[i] | arr2[i]).toString(2)
        b = '0'.repeat(n-b.length) + b
        result.push([...b].map(s => (s === '1' ? '#' : ' ')).join(''))
    }
    return result
}