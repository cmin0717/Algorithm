def solution(c):
    c = sorted(c,reverse=True) + [-1]
    result = 0
    for i in range(len(c)):
        if c[i] < i+1:
            return i
            
# 문제 설명이 이상함...거의 수수께끼임..