from itertools import *

n = int(input())
num = []
# dsf 풀이법
def dsf():
    if len(num) == n: # len(num) == n이 되면 숫자를 다 넣었기에 출력
        print(*num)
        return
    for j in range(1,n+1): # 1 ~ n까지 숫자를 for문으로 돌림
        if j in num: # j가 이미 num에 있다면 continue
            continue
        num.append(j) 
        dsf()
        num.pop()
dsf()

# permutations 이용한 풀이법
# n_li = list(permutations([i for i in range(1,n+1)], n))
# for i in n_li:
#     print(*list(i))