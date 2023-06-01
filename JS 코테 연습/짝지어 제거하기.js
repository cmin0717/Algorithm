function solution(s)
{
    s = [...s]
    const arr = []
    
    for (let i = 0; i < s.length; i++){
        s[i] === arr[arr.length -1] ? arr.pop() : arr.push(s[i])
    }
    // 아래는 시간초과가 나왔다 for문에서 of사용시 특정 로직이 돌아가서 더 느려지는것 같다.
    // for (i of s){
    //     s[i] === arr[arr.length -1] ? arr.pop() : arr.push(s[i])
    // }
    
    return arr[0] ? 0 : 1
    // length을 사용하는것이 더 느리다.
    // return arr.length === 0 ? 1 : 0
}