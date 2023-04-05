function solution(nums) {
    let num = {}
    for (let i of nums){
        if(num[i] == undefined){
            num[i] = 1
        }else{
            num[i]++
        }
    }
    let max_num = 0
    for (let i of Object.keys(num)){
        n = Number(i)
        if (num[i] === n){
            max_num = Math.max(max_num, n)
        }
    }
    return max_num
}