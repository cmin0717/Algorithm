function solution(n,a,b)
{
    let cnt = 0
    while (a !== b){
        cnt++
        a = a % 2 === 0 ? Math.floor(a/2) : Math.floor(a/2)+1
        b = b % 2 === 0 ? Math.floor(b/2) : Math.floor(b/2)+1
    }
    return cnt
}