function solution(price, money, count) {
    const m = [...Array(count).keys()].map(a => price*(a+1)).reduce((a,b) => a+b)
    return m - money > 0 ? m-money : 0
}