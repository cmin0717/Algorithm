from itertools import product

def solution(users, emoticons):
    result,m = [], len(emoticons)
    sales = [10,20,30,40]
    
    # 완.탐
    def check(arr):
        
        cnt,money = 0,0
        for u in users:
            limit,tm = u
            for e in range(m):
                if limit <= arr[e]:
                    tm -= emoticons[e]*(100-arr[e]) // 100
            # 돈이 남았다면 매출액에 +
            if tm > 0:
                money += u[1]-tm
            # 돈이 다 떨어졋다면 플러스 상품 구입
            else:
                cnt += 1
        return [cnt,money]
    
    for i in product(sales, repeat=m): # product를 사용하여 할인률을 데카르트의곱에 해당하는 모든 조합을 가져온다.
        result.append(check(i))

    return sorted(result, reverse=True)[0]