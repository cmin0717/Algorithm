import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    day = int(input())
    price = list(map(int,input().split()))
    top = price.pop() # 맨뒤의값
    pay = [] # 주식을 구매한 날에 주가
    money = 0 # 총 익절한 돈

    while price:
        m = price.pop() # 뒤에서 부터 하나씩 빼온다.
        if m <= top: # 현재까지의 주가보다 싸다면
            pay.append(m) # 구매
        else: # 여태까지 값중 제일 큰값보다도 더 크다면
            money += top * len(pay) - sum(pay) # 익절 금액을 더해주고
            pay = [] # 주식을 다 팔았으니 리스트 초기화
            top = m # 현재 고점을 변경 
    else:
        money += top * len(pay) - sum(pay)
    print(money)    
    
    
    # max 함수 사용 (91% 시간초과)
    # for i in range(day):
    #     if price[i] == top:
    #         money += price[i] * cnt
    #         top = max(price[i+1:])
    #         cnt = 0
    #     else:
    #         cnt += 1
    #         pay += price[i]

    # print(money-pay)