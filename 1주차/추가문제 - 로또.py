# from itertools import *

# dsf를 이용한 완전탐색
lotto = []
def lotto_nums(x): # 어디까지 넣어서 줬는지 파악
    if len(lotto) == 6: # lotto가 6자리가 되면 출력
        print(*lotto)
        return
    for j in range(x,n): # 함수에 넣어준 x부터 n까지 확인 하면된다.
        lotto.append(lotto_num[j+1]) # 로또 번호의 맨앞자리는 숫자의 개수를 파악하는 용도이기에 인덱스에 +1을 해주어야한다
        lotto_nums(j+1)
        lotto.pop()

while True:
    lotto_num = list(map(int, input().split()))
    n = lotto_num[0] 
    if n == 0:break
    for i in range(n-5): # 로또가 무조건 6자리는 되어야 하기에 0 ~ (n-5)번 인덱스까지만 확인하면 된다.
        lotto.append(lotto_num[i+1]) # lotto_num[0]은 필요없는 숫자이기에 +1 해준다.
        lotto_nums(i+1)
        lotto.pop()
    print()

# combinations를 이용한 풀이
# def lotto_num(li):
#     num_li = list(combinations(li,6))
#     for i in num_li:
#         print(*list(i))
#     return

# while True:
#     lotto = list(map(int,input().split()))
#     n = lotto[0]
#     if len(lotto) == 1 and n == 0:
#         break
#     lotto_num(lotto[1:])
#     print()

