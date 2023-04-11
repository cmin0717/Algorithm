from itertools import permutations
from collections import deque
from copy import deepcopy

def solution(ex):
    op = []
    for i in ['-','+','*']:
        if i in ex:
            op.append(i)
            ex = ex.replace(i,f',{i},')
    ex = ex.split(',')
    
    result = 0
    for items in permutations(op,len(op)):
        q = deque(deepcopy(ex))
        for item in items:
            check = []
            while q:
                n = q.popleft()
                if n == item and n == '-':
                    check.append(str(int(check.pop()) - int(q.popleft())))
                elif n == item and n == '+':
                    check.append(str(int(check.pop()) + int(q.popleft())))
                elif n == item and n == '*':
                    check.append(str(int(check.pop()) * int(q.popleft())))
                else:
                    check.append(n)
            q = deque(check)
        result = max(result, abs(int(q.pop())))
    return result

# 파이썬에는 eval이라는 함수가 있다.
# eval('5+5') = 10 // 수식이 문자열로 이루어져도 실행가능하게 해준다.(알고있으면 좋을듯 하다.)